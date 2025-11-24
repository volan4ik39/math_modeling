flowers = ["Роза", "Тюльпан", "Лилия"]
colors = ["Красный", "Жёлтый", "Белый", "Розовый", "Оранжевый"]
import random
flower_color_pairs = {flower: random.choice(colors) for flower in flowers}
print(flower_color_pairs)