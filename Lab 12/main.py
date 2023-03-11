# префиксная функция
#массив длины n, i-ый элемент которого равен наибольшему числу символов, начиная с позиции i, совпадающих с первыми символами строки s
#Иными словами, z[i] — это длина наибольшего общего префикса строки s и её i-го суффикса.
def func_prefix(s):
    l = len(s)
    P = [0]*l
    i, j = 0, 1
    while j < l :
        if s[i] == s[j]:
            P[j] = i + 1
            i += 1
            j += 1
        elif i:         # i > 0
            i = P[i - 1]
        else:           # i == 0
            P[j] = 0
            j += 1
    return P

def kmp_alg(text, sub):
    sub_len = len(sub)
    text_len = len(text)
    print(text_len, sub_len)
    if not text_len or sub_len > text_len:
        return []
    P = func_prefix(sub)
    print(P)
    entries = []
    i = j = 0
    while i < text_len and j < sub_len:
        if text[i] == sub[j]:
            if j == sub_len - 1:
                entries.append(i - sub_len + 1)
                j = 0
            else:
                j += 1
            i += 1
        elif j:     # j > 0
            j = P[j-1]
        else:
            i += 1
    return entries


with open('input.txt', 'r') as f:
    s = str(f.readline())
#s = "abc abeabcabcabdrabc abdtuyeab cabdwrtabcd"
#sub = "abc"
#print(func_prefix(sub))
sub = input('Введите подстроку: ')

P = kmp_alg(s, sub)
print(P)
#for i in P:
#    print(s[i:i + len(sub)])
