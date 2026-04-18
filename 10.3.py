from PIL import Image, ImageDraw, ImageFont
holidays = {'Новый год': 'ng.jpg', '23 февраля': '23.jpg', '1 мая': '1m.jpg'}
print('Доступные праздники:')
for a in holidays:
    print(f'-{a}')
B = input('К какому празднику нужна открытка?')
if B in holidays:
    name = input('Имя того, кого поздравляем?')
    draw = Image.Draw(img)
    font = ImageFont.load_default()
    text = name + ', поздравляю!'
    x = 100
    y = 30
    draw.text((x,y), text, font = font, fill='red')
    img.save('otkritka.png')
    img.show()
    print('Готово! Файл: otkritka.png')
else:
    print('Такого праздника в списке нет!')