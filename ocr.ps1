Add-Type -AssemblyName System.Runtime.WindowsRuntime
$code = @"
using System;
using System.IO;
using System.Threading.Tasks;
using Windows.Graphics.Imaging;
using Windows.Media.Ocr;
using Windows.Storage;
using Windows.Storage.Streams;

public class OcrHelper
{
    public static async Task<string> ExtractText(string imagePath)
    {
        try
        {
            StorageFile file = await StorageFile.GetFileFromPathAsync(imagePath);
            using (IRandomAccessStream stream = await file.OpenAsync(FileAccessMode.Read))
            {
                BitmapDecoder decoder = await BitmapDecoder.CreateAsync(stream);
                SoftwareBitmap softwareBitmap = await decoder.GetSoftwareBitmapAsync();

                OcrEngine engine = OcrEngine.TryCreateFromLanguage(new Windows.Globalization.Language("en-US"));
                if (engine == null) return "Engine null";
                
                OcrResult result = await engine.RecognizeAsync(softwareBitmap);
                return result.Text;
            }
        }
        catch (Exception ex)
        {
            return "Error: " + ex.Message;
        }
    }
}
"@
Add-Type -TypeDefinition $code -Language CSharp
$task = [OcrHelper]::ExtractText("C:\Users\Humayun\Desktop\Webpage-T\assets\business_card.png")
$task.Wait()
$task.Result
