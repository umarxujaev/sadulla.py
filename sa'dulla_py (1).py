# -*- coding: utf-8 -*-
"""Sa'dulla.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18TOOLyVjhTXF3olb4ZxkZzjqIjh_L-rR
"""

import numpy as np
# 1. Massiv yaratish
array_1d = np.array([3,4,5,6,7])
array_2d = np.array([[3,4,5,],[4,5,6]])

#2. Matematik operatsiyalar
sum_array = np.sum(array_1d)
mean_array = np.mean(array_1d)
product_array = np.prod(array_1d)

print("1D MASSIV: ",array_1d)
print("2D MASSIV:\n", array_2d)
print("Massivlar yig'indisi: ",sum_array)
print("O'rtacha: ", mean_array)
print("Ko'paytma: ", product_array)

import pandas as pd

# 1. Ma'lumotlar
data = {
    'Ism' : ["Sa'dulla", 'Muhammad', 'Samandar','Anvarjon','Javohir','Ozodbek','Sarvarjon','Shohruh','Abdurasul','Omadbek'],
    'Yoshi' : [19, 19, 19, 18, 22, 19, 24, 19, 19, 20],
    'Shahar' : ['Farg`ona', 'Farg`ona', 'Farg`ona', 'Andijon', 'Farg`ona', 'Farg`ona', 'Marg`ilon', 'Farg`ona', 'Qo`qon', 'Farg`ona']
}

# 2. DataFrame yaratish
df = pd.DataFrame(data)

# 3. Ma'lumotlarni ko`rish
print(df)

# 4. Filtrlash (ustun nomi 'Yoshi' bo'lishi kerak)
young_people = df[df['Yoshi'] < 20]
print("20 yoshdan kichiklar;\n", young_people)

# 5. O`zgartirish (Yoshini 1 ga kamaytirish)
df['Yoshi'] -= 1
print("Yangilangan DataFrame;\n", df)

# 6. Excel formatda saqlash (to'g'ri funksiya nomi: to_excel)
df.to_excel('541.xlsx', index=True, sheet_name="541")