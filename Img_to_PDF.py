import sys
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image

def imgtopdf(input_paths, outputpath):
    (maxw, maxh) = Image.open(input_paths).size
    c = canvas.Canvas(outputpath, pagesize=portrait((maxw, maxh)))
    c.drawImage(input_paths, 0, 0, maxw, maxh)
    c.showPage()
    c.save()

imgtopdf("/Users/user/Desktop/pdf/WechatIMG1891.jpeg", "cc.pdf")

