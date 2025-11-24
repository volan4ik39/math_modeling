full_name = "Vladimir Vevel Pavlovich"
upper_list = [char for char in full_name.upper()]
lower_list = [char for char in full_name.lower()]
sum_upper = sum(ord(char) for char in upper_list)
sum_lower = sum(ord(char) for char in lower_list)
print("Список в верхнем регистре:", upper_list)
print("Список в нижнем регистре:", lower_list)
print("Сумма ASCII кодов (верхний регистр):", sum_upper)
print("Сумма ASCII кодов (нижний регистр):", sum_lower)