print('Hello world')

import clr
clr.AddReference("mscorlib")
clr.AddReference("System.Drawing")

import json

from System.Net import *
from System.IO import *
from System import *
from System.Drawing import *
from System.Drawing.Imaging import ImageFormat
from System.Diagnostics import *


jsonString = json.dumps({
    'nummer1': 5,
    'nummer2': 3,
    'operatie': 'vermenigvuldigen'
})

text_file = open("output.json", "w")
text_file.write(jsonString)
text_file.close()

process = Process()
process.StartInfo.FileName = "C:\Program Files\Python36\python.exe"
process.StartInfo.Arguments = "C:\Users\Bart\PycharmProjects\pythonWorkerProject\worker.py output.json"
process.StartInfo.UseShellExecute = False
process.StartInfo.RedirectStandardOutput = True
process.StartInfo.RedirectStandardError = True

process.Start()

output = process.StandardOutput.ReadToEnd()
errorOutput = process.StandardError.ReadToEnd()

print(output)
print (errorOutput)

mStream = MemoryStream(WebClient().DownloadData("http://www.duikvakanties.net/wp-content/uploads/2010/09/blauwe-haai-2.jpg"))

imageBitmap = Bitmap(mStream)

imageBitmap.Save("haai.jpg", ImageFormat.Jpeg)

