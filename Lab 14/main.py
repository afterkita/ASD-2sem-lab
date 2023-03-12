import hashlib

def rabin_alg(sourse, pattern, d, q):
    n = len(sourse)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []

    # Начальная обработка
    for i in range(m):
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(sourse[i]))%q
    print('p - ',p,'  t - ',t)

    for s in range(n-m+1):
        # Совпадение по хэш значению
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != sourse[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m: # удаляем значение s и добавляем s+m
            t = (t-h*ord(sourse[s]))%q
            t = (t*d+ord(sourse[s+m]))%q
            t = (t+q)%q
    return result


with open('input.txt', 'r') as f:
    s = str(f.readline())
#s = "abc abeabcabcabdrabc abdtuyeab cabdwrtabcd"
#sub = "abc"
sub = str(input('Введите подстроку: '))
print (rabin_alg (s, sub, hash(s), hash(sub)))