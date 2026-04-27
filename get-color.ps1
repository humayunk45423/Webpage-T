Add-Type -AssemblyName System.Drawing
$bmp = New-Object System.Drawing.Bitmap("C:\Users\Humayun\Desktop\Webpage-T\assets\business_card.png")
$colors = @{}
for ($x = 0; $x -lt $bmp.Width; $x += 10) {
    for ($y = 0; $y -lt $bmp.Height; $y += 10) {
        $c = $bmp.GetPixel($x, $y)
        $hex = "#{0:X2}{1:X2}{2:X2}" -f $c.R, $c.G, $c.B
        if ($colors.ContainsKey($hex)) {
            $colors[$hex]++
        } else {
            $colors[$hex] = 1
        }
    }
}
$bmp.Dispose()
$colors.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 10 | Format-Table -AutoSize
