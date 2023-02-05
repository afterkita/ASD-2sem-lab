

def Over_read():
    N = 0
    with open('input.txt', 'r') as f:
        for s in f:
            N += 1
    arr = []
    with open('input.txt', 'r') as f1:
        for s in f1:
            arr.append(s)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    return arr
def After_read(arr):
    knot_link = [] #Массив связей
    # Формирование массива связей
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if int(arr[i][j]) >= 1:
                knot_link.append([i,j,int(arr[i][j])])
    #Очистка массива связей
    l = len(knot_link)
    for i in range(l):
        for j in range(l):
            if int(knot_link[i][0]) == int(knot_link[j][1]) and int(knot_link[i][1]) == int(knot_link[j][0]) and i != j:
                knot_link[i] = [0,0,0]
    l = len(knot_link)
    l1 = 0
    while True:
        if l1 >= len(knot_link):
            break
        if knot_link[l1] == [0,0,0]:
            knot_link.pop(l1)
        else:
            l1+=1
    return knot_link
def Kruskal_alg(arr):
    #Сортировка по длинне
    for i in range(len(arr)):
        for j in  range(len(arr)):
            if int(arr[i][2])<int(arr[j][2]):
                arr[i],arr[j] = arr[j],arr[i]
    print(arr)
    end_arr = [arr[0]] # Конечный массив связей
    available = [[int(arr[0][0]),int(arr[0][1])]] # Массив массивов каждый из которых является компонентой связанности
    # проверка на зацикливание дерева
    # flag = 0 - не один из узлов ещё не рассматривался
    # flag = -1 - оба узла рассматривались в одной компоненте
    # flag = 1 - один узел рассматривался
    # flag = 2 - оба узла рассматривались в разных компонентах
    for i in range(1,len(arr)):
        flag = 0
        for j in range(len(available)):
            if int(arr[i][0]) in available[j]:
                flag = 1
                if int(arr[i][1]) in available[j]:
                    flag = -1
                    break
                else:
                    for k in range(len(available)):
                        if int(arr[i][1]) in available[k]:
                            available[j] = available[j] + available[k] #Обьединение компонент связанности
                            available.pop(k)
                            flag = 2
                            end_arr.append(arr[i])
                            break
                    if flag != 2:
                        available[j].append(int(arr[i][1]))
                        end_arr.append(arr[i])
                    break
            elif int(arr[i][1]) in available[j]:
                flag = 1
                if int(arr[i][0]) in available[j]:
                    flag = -1
                    break
                else:
                    for k in range(len(available)):
                        if int(arr[i][0]) in available[k]:
                            available[j] = available[j] + available[k] #Обьединение компонент связанности
                            available.pop(k)
                            end_arr.append(arr[i])
                            flag = 2
                            break
                    if flag != 2:
                        available[j].append(int(arr[i][0]))
                        end_arr.append(arr[i])
                    break
        #print(flag)
        if flag == 0:
            available.append([int(arr[i][0]),int(arr[i][1])])
            end_arr.append(arr[i])

    print(available)

    return  end_arr



print('Минимальное оставное дерево: ',Kruskal_alg(After_read(Over_read())))