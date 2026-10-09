/**
 * Mobile Express - Production High-Performance Service Worker
 * Strategy: Stale-While-Revalidate for local assets, Cache-First for static fonts
 */

const CACHE_NAME = 'mobile-express-v1.0.0';
const STATIC_ASSETS = [
    './',
    './index.html',
    './inventory.html',
    './style.css',
    './script.js',
    './manifest.json',
    './Mobile Express.svg',
    './assets/logo.png',
    './assets/logo.svg'
];

// Install: Cache critical core assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS);
        }).then(() => self.skipWaiting())
    );
});

// Activate: Prune stale caches & take immediate control
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

// Fetch: Stale-While-Revalidate with network fallback
self.addEventListener('fetch', (event) => {
    const request = event.request;
    
    // Ignore non-GET requests
    if (request.method !== 'GET') return;

    // Handle same-origin static assets & CDN assets
    const url = new URL(request.url);
    const isSameOrigin = url.origin === self.location.origin;
    const isFontOrCDN = url.hostname.includes('googleapis.com') ||
                        url.hostname.includes('gstatic.com') ||
                        url.hostname.includes('cdnjs.cloudflare.com');

    if (isSameOrigin || isFontOrCDN) {
        event.respondWith(
            caches.match(request).then((cachedResponse) => {
                const fetchPromise = fetch(request).then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        const responseClone = networkResponse.clone();
                        caches.open(CACHE_NAME).then((cache) => {
                            cache.put(request, responseClone);
                        });
                    }
                    return networkResponse;
                }).catch(() => {
                    // Offline fallback
                    return cachedResponse;
                });

                return cachedResponse || fetchPromise;
            })
        );
    }
});
