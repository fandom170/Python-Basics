from random import randint, uniform

with open('text_file_hw05-05.txt', 'w', encoding='utf-8') as init_file:
    number_list = [str(round(uniform(0, 100), 2)) + ' ' for i in range(randint(10, 1000))]
    for i in number_list:
        init_file.write(i)

with open('text_file_hw05-05.txt', 'r', encoding='utf-8') as result:
    print(sum(list(map(float, result.read().rstrip().split(' ')))))
