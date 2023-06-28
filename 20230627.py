"""
큰따옴표 세개 쓰면 여러줄의 주속
"""
#이거도 한줄짜리 주석

"""
Project : My first Python Program
작성자 : 박범훈
작성일 : 20230628
"""
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

""""
Project : My simple python program with data input
작성자 : 박범훈
작성일 : 20230628
"""

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