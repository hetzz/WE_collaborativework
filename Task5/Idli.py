n = int(input())
list1 = list(map(int,input().split()))
count = 0
for i in range(len(list1)-1) :
    if(list1[i] % 2 != 0):
        list1[i+1] += 1
        count += 2

if(list1[-1] % 2 == 0 ):
    print(count)

else :
    print("NO") 