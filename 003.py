 # Вывести на экран числа от -N до N


print ('Введите целое число, последовательность которых будеть выводиться с отрицательного до положительного диапазона');
N = int (input ())
a = N - N*2;
while(a<=N):
    print(f"{a} ")
    a+=1