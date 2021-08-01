qty = input("Сколько человек в вашей семье?:")
qty = int(qty)

pay1 = input("Введите зарплату первого члена семьи:")
pay1 = int(pay1)

my_list = [pay1]
x = 1

while x < qty:
    my_list.append(int(input("Введите зарплату следующего члена семьи:")))
    x = x + 1

print("Средняя зарплата членов вашей семьи:", sum(my_list) / len(my_list))



