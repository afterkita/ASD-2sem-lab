import random
#Жадный алгоритм это - Алгоритм, заключающийся в принятии локально оптимальных решений на каждом этапе, допуская, что конечное решение также окажется оптимальным.

#Задача о сумме подмножеств — это важная задача в теории сложности алгоритмов и криптографии. Задача заключается
# в нахождении (хотя бы одного) непустого подмножества некоторого набора чисел, чтобы сумма чисел этого подмножества равнялась нулю.

def make_list(n,m,k):
    f = open('input.txt','w+')
    for i in range(n):
        d = random.randint(m, k)
        if d == 0:
            d = 1
        s = str(d)+'\n'

        f.write(s)
    f.close()
# Считывает из txt айла массив значений
def txt_read(s):
    s1 = str(s)+'.txt'
    f = open(s1, 'r')
    arr = []
    for line in f:
        arr.append(int(line))
    return arr
def greed_alg(arr):
    for j in range(len(arr)):
        d = int(arr[j])
        end_arr = []
        end_arr.append(arr[j])
        for i in range(len(arr)):
            if d == 0:
                #print(j,' ',i)
                print('Последовательность найдена!')
                return end_arr
            if abs(d + arr[i]) < abs(d):
                d += arr[i]
                end_arr.append(arr[i])
    print('Последовательность не найдена!')
    return end_arr



#make_list(100,-50,50)
arr = txt_read('input')
#print(sorted(arr,key=abs))
print('Последовательность: ',greed_alg(arr))
