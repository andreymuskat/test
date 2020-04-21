#Цикл for
a = []
for i in range(10):     #заполняем массив
    a.append(i)
for i in range(len(a)):     #проход по элементам  массива
    print(a[i])  # a[0]
    
#Цикл while
b = [1,2,3,4,5,6,7,8,9,10]
while len(b)>0:     #пока длина строки больше 0
	b.pop(0)
	print(b)