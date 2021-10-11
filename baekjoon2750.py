#백준 2750 수 정렬하기

x= int(input('몇개 적을 꺼니?:'))
num_list= []
for i in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])
