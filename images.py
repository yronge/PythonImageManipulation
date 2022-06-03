from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

print(f'\nimg object = {img}')
print(f'img object format = {img.format}')
print(f'img object size = {img.size}')
print(f'img object mode = {img.mode}')

print(f'\nimg object list of methods = {dir(img)}\n')   # lists all methods available to call on img object

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./images/blurred_pikachu.png", 'png')   # saves and also converts image to png

box = (100, 100, 400, 400)
region_img = img.crop(box)
region_img.save("./images/cropped_pikachu.png", 'png')

thumbnail_img = img
thumbnail_img.thumbnail((100,100))
thumbnail_img.save("./images/thumbnail_pikachu.png", 'png')
print(f'thumbnail size = {thumbnail_img.size}\n')
