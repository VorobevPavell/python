#Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет, можно ли из переданных аргументов составить треугольник. (Напомню, что у любого треугольника длина третьей стороны всегда должна быть меньше суммы двух других). Если  проверка проходит, вернуть булево значение True, иначе - значение False.



def is_triangle(a,b,c):
    tr = True if a < b + c and b < a + c and c < a + b else False
    return(tr)


