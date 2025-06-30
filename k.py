for i in range(1,100):
    if i%10==7 or i//10==7:
        print(i)


      
list1=[]
for i in range(n):
    if i%2==0:
        list1.append(i)
print(list1)
list2=[x for x in range(n) if x%2==1]
print(list2)