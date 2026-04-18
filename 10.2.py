from PIL import Image
holidays = {'Новый год': 'ng.jpg', '23 февраля': '23.jpg', '1 мая': '1m.jpg'}
print('Доступные праздники:')
for a in holidays:
    print(f'-{a}')
B = input('К какому празднику нужна открытка?')
if B in holidays:
    img = Image.open(holidays[B])
    img.show()
    print(f"Открытка к {B} открыта")
else:
    print('Такого праздника в списке нет!')