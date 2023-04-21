# from io import BytesIO
# from random import randrange
# import random
# import barcode
# from barcode import EAN13
# from barcode.writer import SVGWriter
# from barcode.writer import ImageWriter
# mylist = ""
# for i in range(0,13):
#     x = random.randint(1,10)
#     mylist += str(x)

#     print(x)

# def genBArcode():
#     EAN = barcode.get_barcode_class('ean13')
#     my_ean = EAN(mylist, writer=ImageWriter())
#     fullname = my_ean.save('ean13_barcode')
#     fullname
#     'ean13_barcode.png'
#     from io import BytesIO
#     fp = BytesIO()
#     my_ean.write(fp)
#     my_ean
#     EuropeanArticleNumber13(mylist)
#     with open("path/to/file", "wb") as f:
#         my_ean.write(f)  # Pillow (ImageWriter) produces RAW format here
    



import uuid
def grncodesec():
    code = str(uuid.uuid4()).replace("-","")[:22]
    return code
def roomcode():
    rcode = str(uuid.uuid4()).replace("-","")[:8]
    return rcode