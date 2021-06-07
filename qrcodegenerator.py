import pyqrcode 
from pyqrcode import QRCode 
   
s = "https://www.python.org/"
   
url = pyqrcode.create(s) 
  
url.svg("myfile.svg", scale = 8)