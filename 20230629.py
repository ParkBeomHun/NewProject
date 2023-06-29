"""
파이썬 공부_박범훈_20230629
"""
"""
sample_list1 = [1,2,3,4,5]
print(sample_list1)
del sample_list1[2]      # 인덱스 2번의 원소 삭제
print(sample_list1)
"""






"""
sample_list2 = [[1,2,3,4],[5,6,7,8]]
print(sample_list2)
print(sample_list2[1][3])
"""
"""
L1 = list()
L2 = list()

for i in range(10):
    L1.append(i)
print(L1)
for i in range(0,10):
    L2.append(i)
print(L2)

#range(n) : 0 ~ n-1 까지 1씩 증가하는 정수 생성
#range(k,n) : k ~ n-1까지 1씩 증가하는 정수 생성
#range(k,n,r) : k ~ n-1까지 r씩 증가하는 정수 생성
"""




"""
TARGET_NUM_DATA = 15
sample_list = list()

numdata = 0
data = 0
mindata = maxdata = sumdata = length = 0

for i in range(TARGET_NUM_DATA):
    data = int(input())
    sample_list.append(data)
    numdata = numdata + 1

mindata = min(sample_list)
maxdata = max(sample_list)
sumdata = sum(sample_list)
length = len(sample_list)

print("Max : {}, Min : {}, Sum : {}, Length : {}".format(maxdata,mindata,sumdata,length))

"""




x = 16
print(x)
print(bin(x))