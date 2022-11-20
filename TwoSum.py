#Дан массив целых чисел. Необходимо вернуть индексы 2х чисел, сумма которых равна указанной цели. Например дан массив = [2, 7, 11, 15], а результат = 9(вводится с клавиатуры) , то нужно вывести индексы 0 и 1



nums = [int(i) for i in input().split()]
target = int(input())
for x in range(len(nums)):
    res_x = x
    for y in range(1,len(nums)):
        res_y = y
        if nums[x] + nums[y] == target:
            print(res_x,res_y)
            