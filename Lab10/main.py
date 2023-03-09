import math
import copy
#Алгоритм был предложен Флёри в 1883 году.
#Пусть задан граф G=(V,E). Начинаем с некоторой вершины V и каждый раз вычеркиваем пройденное ребро.
# Не проходим по ребру, если удаление этого ребра приводит к разбиению графа на две связные компоненты (не считая изолированных вершин),
# т.е. необходимо проверять, является ли ребро мостом или нет.


# Заполнение массива по матрице путей
def Graf_go(s):
    N = 0
    with open( str(s)+'.txt', 'r') as f:
        for t in f:
            N += 1
    arr = []
    with open(str(s)+'.txt', 'r') as f1:
        for t in f1:
            arr.append(t)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr
def alg_Deikstr(n,arr):
    viset = [] # массив индексов посещённых элементов
    end_arr = [math.inf]*len(arr) # массив длин дорог до элементов
    end_arr[n] = 0

    while len(viset) != len(arr):
        con = math.inf
        con_i = 0
        # Нашли минимальную не посещённую метку метку
        for i in range(len(end_arr)):
            if i not in viset:
                if con>end_arr[i]:
                    con = end_arr[i]
                    con_i = i
        #print(con_i)
        viset.append(con_i)
        #print(arr[con_i])
        # Заменяем значения у не посещённых точек, если путь до них меньше указанного
        for i in range(len(arr[con_i])):
            if int(arr[con_i][i]) != 0:
                if i not in viset:
                    if end_arr[i] > int(arr[con_i][i])+end_arr[con_i]:
                        end_arr[i] = int(arr[con_i][i])+end_arr[con_i]
    return end_arr
# Проверка на "мосты"
def graph_connect_comp(arr,k,v_arr):
    #print(arr)
    flag = True
    for i in range(len(arr)):
        if i not in v_arr:
            c_arr = alg_Deikstr(i, arr)
            for j in range(len(c_arr)):
                if i not in v_arr:
                    if type(c_arr[j]) != int:
                        flag = False
                        if j == k and null_elem(arr[j]) == True:
                            if j not in v_arr:
                                v_arr.append(k)
                            flag = True
                        if j in v_arr:
                            flag = True
    return flag
def num_way(arr):
    c_arr = copy.deepcopy(arr)
    #print(id(arr),' - ',id(c_arr))
    num = 0
    for i in range(len(c_arr)):
        for j in range(len(c_arr[i])):
            if c_arr[i][j] != 0:
                num += 1
                c_arr[i][j] = 0
                c_arr[j][i] = 0
    #print(arr)
    return num
def null_elem(arr):
    #print(arr)
    flag = True
    for i in range(len(arr)):
        if int(arr[i]) != 0:
            flag = False
            break
    return flag
def del_nul(arr,k):
    for i in range(len(arr)):
        arr[i].pop(k)
    arr.pop(k)

# РАботает тольго для правильных граффов
def alg_Fleri(arr):
    v_arr = []
    #print(arr)
    i_k = 0
    result = []
    for _ in range(20):
        #print(i_k)
        #print(arr)
        if null_elem(arr[i_k]) == True:
            break
        for i in range(len(arr[i_k])):
            if arr[i_k][i] != 0:
                d_arr = copy.deepcopy(arr)
                d_arr[i_k][i] = 0
                d_arr[i][i_k] = 0
                #print(d_arr)
                if graph_connect_comp(d_arr,i_k,v_arr) == True:
                    #print(i_k,' ',i)
                    result.append([i_k,i])
                    arr[i_k][i] = 0
                    arr[i][i_k] = 0
                    if null_elem(arr[i_k]) == True:
                        v_arr.append(i_k)
                    i_k = i
                    break
    print(v_arr)
    return result





#g = open('prom.txt', 'w')
s1 = 'input'
arr = Graf_go(s1)
#print(arr)
#print(alg_Deikstr(0,Graf_go(s1)))
#print(graph_connect_comp(arr))

#print(num_way(arr))

print(arr)
print(null_elem(arr[0]))
print(arr)
print(alg_Fleri(arr))
