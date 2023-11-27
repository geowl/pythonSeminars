
def word(str):
    str = str.split()
    list_ = []
    for word in str:
        sum_w = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_w += 1
        list_.append(sum_w)
    return len(list_) == list_.count(list_[0])


stroka = 'по-русски говорят'
if word(stroka):
    print('Парам пам-пам')
else:
    print('Количество фраз должно быть больше одной!')
