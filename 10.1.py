from PIL import Image
img = Image.open('otk.jpg')
crop_area = (50,50,300,200)
cropped_img = img.crop(crop_area)
cropped_img.save('cropped_otk.jpg')
print('Размер открытки (ширина, высотка):', img.size)