# Генерация таблица сдвигов
def shift_table(patern):
    skip_list = {}
    for i in range(0,len(patern)):
        skip_list[patern[i]] = max(1,len(patern)-i-1)
    return skip_list

# алгоритм Бойера-Мура
def boyer_mur_Search(sourse, patern):
    s_char = shift_table(patern)
    print(s_char)
    i = len(patern)-1 # i - итератор для строки
    answer = []
    while i <=  len(sourse)-1:
        j = 0 # j - итератор для подстроки
        while j < len(patern) and patern[len(patern)-j-1] == sourse[i-j]:
            j+=1
        if j == len(patern): #Подстрока совпадает с шаблоном
            answer.append(i-len(patern)+1)
            i += 1
            continue
        else:
            shift = s_char.get(sourse[i+j],len(patern)) #Получаем сдвиг по строке из таблицы
            if shift == 0: # Если сдвига нет перемещаемся на длинну шаблона
                shift = len(patern)-1
            skip = shift-j
            i += skip
    return answer



with open('input.txt', 'r') as f:
    s = str(f.readline())
#s = "abc abeabcabcabdrabc abdtuyeab cabdwrtabcd"
#sub = "abc"
sub = str(input('Введите подстроку: '))
print(boyer_mur_Search(s,sub))


