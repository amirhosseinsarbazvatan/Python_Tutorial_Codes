# Pillow module in python

# Image proccessing functions in python


from PIL import Image, ImageFilter

img = Image.open(r"C:\Users\pc\Desktop\Python_Code\Python.png")

img.show()

img.save(r"C:\Users\pc\Desktop\Python_Code\Python.jpg")

print(img.format)
print(img.mode)
print(img.size)
print(img.palette)
print(img.info)
print(img.getbands())
print(img.getextrema())


resized_image = img.resize((500,500))
resized_image.save(r"C:\Users\pc\Desktop\Python_Code\Python_500.png")

thumbnailed_image = img.thumbnail((500,500))
thumbnailed_image.save(r"C:\Users\pc\Desktop\Python_Code\Python_500.png")

box = (150,200,600,600)
croped_image = img.crop(box)
croped_image.save(r"C:\Users\pc\Desktop\Python_Code\Python_croped.png")


img.rotate(90, expand=True).show()

img.convert("l").show()        # L => Grayscale , RGB => RedBlueGreen mode , CMYK => CMYK mode


image_filtered = img.filter(ImageFilter.BLUR)
image_filtered.show()

image_filtered = img.filter(ImageFilter.SMOOTH)
image_filtered.show()