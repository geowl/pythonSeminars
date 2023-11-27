# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета

n = 123456
left_part = n//1000
right_part = n%1000
first = left_part // 100
second = left_part // 10%10
third = left_part%10
fourth = right_part //100
fifth = right_part//10%10
sixth = right_part%10
left_sum = first+second+third
right_sum = fourth+fifth+sixth
if left_sum == right_sum:
    print("YES")
else:
    print("NO")