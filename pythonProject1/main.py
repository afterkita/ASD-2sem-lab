#------Минимальная выпуклая оболочка (алгоритм Грэхема)-----
#Поворот для точек образующих вогнутый угол
def Rot(A1,A2,A3):
  return (A2[0]-A1[0])*(A3[1]-A2[1])-(A2[1]-A1[1])*(A3[0]-A2[0])
#Алгоритм
def MVO(A):
  n = len(A)
  arr=[]
    #Дублирующий массив с номерами элементов
  for i in range(n):
      arr.append(i)
    #Находим левую точку
  for i in range(1,n):
    if A[arr[i]][0]<A[arr[0]][0]:
      arr[i], arr[0] = arr[0], arr[i]
    #Сортировка по "высоте"
  for i in range(2,n):
    j = i
    while j>1 and (Rot(A[arr[0]],A[arr[j-1]],A[arr[j]])<0):
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j -= 1
    #Проходим по точкам и удаляем их в случае если угол вогнутый
  mvo = [arr[0],arr[1]]
  for i in range(2,n):
    while Rot(A[mvo[-2]],A[mvo[-1]],A[arr[i]])<0:
      del mvo[-1]
    mvo.append(arr[i])
  print(mvo)
  for i in mvo:
      print(A[i])


print('Колво точек: ')
count = int(input())
A = [0]*count
for i in range(count):
    A[i]=[0]*2
    a = int(input())
    b = int(input())
    A[i][0]=a
    A[i][1]=b

MVO(A)
#print(A)