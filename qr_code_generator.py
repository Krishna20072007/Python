import pyqrcode 
from pyqrcode import QRCode 
  
link = "krishna-k-lalwani.tk"
  
qr = pyqrcode.create(link) 
  
qr.svg("krishna-k-lalwani.tk.svg", scale = 8)