pokupka = int(input("Введите стоимость покупк: "))
deneg = int(input("Введите сумму переданную кассиру: "))
sdacha = deneg - pokupka

print("\n")

kol_500 = sdacha // 500 # проверка на целочисленное деление на 500
kol_500_ostatok = sdacha % 500  # расчет остатка от деления на 500
if (kol_500>=1):  # если результат целочисленного деления больше либо равно 1, то выводим на печать данные
	print("Количество купюр достоинством 500 руб составляет - ", kol_500)

kol_100 = kol_500_ostatok // 100
kol_100_ostatok = kol_500_ostatok % 100
if (kol_100>=1):
	print("Количество купюр достоинством 100 руб составляет - ", kol_100)

kol_50 = kol_100_ostatok // 50
kol_50_ostatok = kol_100_ostatok % 50
if (kol_50>=1):
	print("Количество купюр достоинством 50 руб составляет - ", kol_50)

kol_10 = kol_50_ostatok // 10
kol_10_ostatok = kol_50_ostatok % 10
if (kol_10>=1):
	print("Количество купюр достоинством 10 руб составляет - ", kol_10)
	print("Количество мелочи составляет - ", kol_10_ostatok, "руб.")

kol_1 = kol_10_ostatok // 1
kol_1_ostatok = kol_10_ostatok % 1
if (kol_1>=1):
	print("Количество купюр достоинством 1 руб составляет - ", kol_1)
	print("Количество мелочи составляет - ", kol_1, "руб.")

print("\nВы дали кассиру -  ", deneg, " руб.\nСтоимость покупки составляет - ", pokupka, " руб.\nВаша сдача - ", sdacha, " руб.\n")