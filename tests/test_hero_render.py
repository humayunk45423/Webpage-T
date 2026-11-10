import os
from playwright.sync_api import sync_playwright

test_html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hero Phone Prototype Test</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=Noto+Sans+Bengali:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../style.css">
</head>
<body style="background: #0d0e12; padding: 40px 20px;">
    <div style="max-width: 1200px; margin: 0 auto;">
        <!-- Prototype Hero Will Be Rendered Here -->
    </div>
</body>
</html>
"""

os.makedirs('tests', exist_ok=True)
with open('tests/prototype.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

print("Prototype container created.")

