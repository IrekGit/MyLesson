from PIL import Image # импорт модуля для работы с изображениями

# Открыть изображение
image = Image.open("563.jpg")

# Сохранить в другом формате
image.save("563_new_format.png")

# Изменение размера
resized_image = image.resize((300, 200))
resized_image.save("563_1.jpg")

# Обрезка области
cropped_image = image.crop((200, 50, 400, 300))
cropped_image.save("563_2.jpg")

from PIL import ImageEnhance # импорт модуля для работы с яркостью, контрастностью и т.д.

# Регулировка яркости
enhancer = ImageEnhance.Brightness(image)
brighter_image = enhancer.enhance(1.5)
brighter_image.save("563_3.jpg")

# Поворот на 45 градусов
rotated_image = image.rotate(45)
rotated_image.save("563_4.jpg")

# Отражение по горизонтали
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.save("563_5.jpg")

from PIL import ImageFilter # импорт модуля для работы с фильтрами

# Размытие
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save("563_6.jpg")

# Контур
contour_image = image.filter(ImageFilter.CONTOUR)
contour_image.save("563_7.jpg")