import logging
logging.basicConfig(filename="ex.log", level=logging.INFO)  # создаём log-file
b1 = "Введите x координату первого поля: "
b2 = "Введите y координату первого поля: "
b3 = "Введите x координату второго поля: "
b4 = "Введите y координату второго поля: "
b5 = "Выберите фашу фигуру: 1 - Ферзь, 2 - Ладья, 3 - Слон, 4 - Конь\nНомер фигуры: "


def input_check(b, n):  # функция-обработчик ошибок ввода
    while True:
        try:
            a = int(input(b))
            if n == 1 and (a < 1 or a > 8):
                print("Введите число от 1 до 8!")
                logging.error("Incorrect number")
            elif n == 2 and (a < 1 or a > 4):
                print("Введите число от 1 до 4!")
                logging.error("Incorrect number")
            else:
                logging.info("User input " + str(a))
                return a
        except ValueError:
            print("Некоректное значение, попробуйте ещё раз")
            logging.error("ValueError")


logging.info("--Program started--")
x1 = input_check(b1, n=1)
y1 = input_check(b2, n=1)
x2 = input_check(b3, n=1)
y2 = input_check(b4, n=1)
figure = input_check(b5, n=2)

color_check1 = (x1 + y1) % 2  # сумма кординат белых клеток всегда чётная, а чёрных нечётная
color_check2 = (x2 + y2) % 2

if color_check1 == color_check2:
    print("Обе клетки", end=" ")
    if color_check1 == 1:
        print("чёрного", end=" ")
    else:
        print("белого", end=" ")
    print("цвета")
    bishop = True
else:
    print("Клетки разных цветов")
    bishop = False

raz_x = abs(x1 - x2)
raz_y = abs(y1 - y2)


if figure == 1:
    if (raz_x == 0 or raz_y == 0) or (raz_x == raz_y):  # если клетки на одной линии, то разница будет равана нулю
        print(f"Ферзь угрожает полю ({x2};{y2})")  # а если клетки на одной диаогонали, то разница будет равна
    else:
        print(f"Ферзь не угрожает данному полю\nДля нападения передвиньте ферзя на поле ({x1};{y2}) или ({x2};{y1})")
elif figure == 2:  # клетки на одной линии
    if raz_x == 0 or raz_y == 0:
        print(f"Ладья угрожает полю ({x2};{y2})")
    else:
        print(f"Ладья не угрожает данному полю\nДля нападения передвиньте ладью на поле ({x1};{y2}) или ({x2};{y1})")
elif figure == 3:  # клетки на одной диагонали
    if raz_x == raz_y:
        print(f"Слон угрожает полю ({x2};{y2})")
    elif not bishop:
        print("Слон не угрожает данному полю и не сможет угрожать, так как находится на поле другого цвета")
    else:  # поиск хода методом перебора
        per = 0
        x, y = x1, y1
        r1 = abs(x - x2)
        r2 = abs(y - y2)
        while 8 >= x >= 1 and 8 >= y >= 1:
            if r1 == r2:
                per = 1
                break
            x += 1
            y += 1
            r1 = abs(x - x2)
            r2 = abs(y - y2)
        if per != 1:
            x, y = x1, y1
        while 8 >= x >= 1 and 8 >= y >= 1:
            if r1 == r2:
                per = 1
                break
            x -= 1
            y += 1
            r1 = abs(x - x2)
            r2 = abs(y - y2)
        if per != 1:
            x, y = x1, y1
        while 8 >= x >= 1 and 8 >= y >= 1:
            if r1 == r2:
                per = 1
                break
            x += 1
            y -= 1
            r1 = abs(x - x2)
            r2 = abs(y - y2)
        if per != 1:
            x, y = x1, y1
        while 8 >= x >= 1 and 8 >= y >= 1:
            if r1 == r2:
                break
            x -= 1
            y -= 1
            r1 = abs(x - x2)
            r2 = abs(y - y2)
        print(f"Слон не угрожает данному полю\nДля нападения передвиньте слона на поле ({x};{y})")

elif figure == 4:  # если конь в пределах досигаемости, то разница координат полей будет 1 и 2
    if raz_x == 1 and raz_y == 2 or raz_x == 2 and raz_y == 1:
        print(f"Конь угрожает полю ({x2};{y2})")
    else:
        print("Конь не угрожает данному полю")

logging.info("--Program finished--")
