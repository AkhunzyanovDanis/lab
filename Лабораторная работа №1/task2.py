# TODO Найдите количество книг, которое можно разместить на дискете
average = 1.44*1024*1024
count = 100
number = 50
symbol = 25
x = 4
k = count*number*symbol*4
book = average//k
print("Количество книг, помещающихся на дискету:", int(book))
