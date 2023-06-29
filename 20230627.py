"""
큰따옴표 세개 쓰면 여러줄의 주속
"""
#이거도 한줄짜리 주석

"""
#Project : My first Python Program
#작성자 : 박범훈
#작성일 : 20230628

print("Hello World ! Iam glad to meet you !")
my_name = "Park BeomHun"
print("My name is",my_name,".")

#definition of variables
x = 5
y = 2
print("x : ",x)     #출력하면 한칸 뛰우고 출력함
print("y : ",y)     #출력시키면 출력문마다 자동으로 줄바꿈 생김
sum_xy = x+y
sub_xy = x-y
mul_xy = x*y
div_xy = x/y
int_div_xy = x//y
print("x+y:",sum_xy)
print("x-y:",sub_xy)
print("x*y:",mul_xy)
print("x/y:",div_xy)        #/는 자동으로 double형으로 알아서 나눠줌
print("x//y:",int_div_xy)   #//는 정수 나누기
"""






""""
#Project : My simple python program with data input
#작성자 : 박범훈
#작성일 : 20230628


"definition of variables"
x_str = input("input x = ")
y_str = input("input y = ")
x,y = int(x_str),int(y_str)
print("x, y = {}, {}".format(x,y))  # %뭐시기 대신 {} 사용

sum = x + y
sub = x-y
mul = x*y
div = x/y
int_div = x//y

print("x + y =",sum)
print("x - y =",sub)
print("x * y =",mul)
print("x / y =",div)
print("x // y = ",int_div)

print("")
print("")
"""




"""
#파이썬의 여러 자료형들
x=1
print("x = ",x)
print("type(x) = ",type(x))     #int : 정수형

x=1.234
print("x = ",x)
print("type(x) = ",type(x))     #float : 실수형

x=[1,2,3,4]
print("x = ",x)
print("type(x) = ",type(x))     #list : 배열 / 수정 가능

x=(1,2,3,4)
print("x = ",x)
print("type(x) = ",type(x))     #tuple : 튜플 / 수정, 삭제 불가능

x = {"A":1,"B":2,"C":3,"D":4}
print("x = ",x)
print("type(x) = ",type(x))     #dict : 딕셔너리 / key와 value로 구분 / key를 통해 value에 접근 / 데이터 추가, 수정, 삭제 가능 

x = {1,2,3,4}
print("x = ",x)
print("type(x) = ",type(x))     #set : 집합

#List vs Array 
#배열은 크기 지정해야 되고 고정되어있는 배열의 크기 때문에 데이터추가 및 삭제 불편
#List는 동적으로 생성되어 크기가 정해져있지 않음, 포인터를 통해 데이터 위치를 가리켜서 데이터 삭제, 삽입이 용이
"""





"""
x_str = input("promt string : ")        #input()으로 넣으면 str 형식으로 입력됨
y_str = input("promt string : ")
print(x_str)
print(y_str)
print("type of x_str, y_str : ",type(x_str),type(y_str))

sum_str = x_str + y_str
print("sum_str : ",sum_str)

x_int = int(x_str)                      #data의 형식을 int로 바꿔줌
y_int = int(y_str)
sum_int = x_int + y_int
print("sum_int : ",sum_int)
"""





"""
n = int(input('input n to calculate sum of [0..n] : '))
nSum = 0
for i in  range(0, n+1):
    nSum += i
    print(i)

print("Sum of [0..%d] = %d" %(n, nSum))
"""




"""
#-1이 입력되기 전까지 정수 data를 입력 받고 양의 정수의 합을 구하는 프로그램

MAX_NUM_DATA = 100
num_data = 0
data_sum = 0
print("input (up to {}) integer data" .format(MAX_NUM_DATA))

for i in range(MAX_NUM_DATA):
    data = int(input("Data(-1 to finish) = "))
    num_data = num_data+1
    if data == -1:
        break
    elif data <= 0:
        continue
    else:
        data_sum = data_sum + data

print("Totla %d data input, sum of positive data = %d" %(num_data,data_sum))
"""





"""
#for문을 사용해서 int를 이어서 받고 각각을 나눈후 최대 최소 구하는 프로그램

TARGET_NUM_DATA = 10
int_str= input("input %d integer data in one line" %(TARGET_NUM_DATA))
L_data = list(map(int, int_str.split(sep=' ')))
print("input data = ",L_data)

data_min = data_max = L_data[0]

for i in range(1 , len(L_data)):
    data = L_data[i]
    if(data<data_min):
        data_min = data
    elif(data>data_max):
        data_max = data
    else:
        continue

print("data_min = %d, data_max = %d)" %(data_min, data_max))

"""