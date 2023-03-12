
# Заполнение массива по матрице путей
def Graf_go(s):
    N = 0
    with open( str(s)+'.txt', 'r') as f:
        for t in f:
            N += 1
    arr = []
    end_arr = []
    with open(str(s)+'.txt', 'r') as f1:
        for t in f1:
            arr.append(t)
    for i in range(len(arr)):
        arr[i] = arr[i].split()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    return arr

# раскраска графа
def graphColoring(arr):
    colored = [[]]
    color = 0  # № цвета
    stack = []  # покрашенные узлы
    num2 = num1 = -1

    # функция проверки возможности покраски в используемый сейчас цвет
    def loop(num):
        for t in colored[color]:
            if arr[t][num] == 1:
                return False
        return True

    for a in arr:
        num1 += 1
        if num1 not in stack:  # просматриваем только те, которые еще не покрашены
            if not loop(num1):  # значит применяем новый цвет
                colored.append([])
                color += 1
                stack.append(num1)
                colored[color].append(num1)
            num2 = num1
            for b in a[num1:]:
                if b == 0 and num2 not in stack and loop(num2):
                    stack.append(num2)
                    colored[color].append(num2)
                num2 += 1
    return colored
def print_colored_graf(s='input'):
    g_arr = Graf_go('input')
    h_arr = graphColoring(g_arr)
    for i in range(len(h_arr)):
        s1 = 'Цвет '+str(i+1)+' точки: '
        for j in range(len(h_arr[i])):
            s1 = s1+str(h_arr[i][j])+' '
        print(s1)


print_colored_graf()