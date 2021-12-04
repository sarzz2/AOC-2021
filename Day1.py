with open("input1.txt") as f:
    a = f.readlines()

#part 1
inc = 0
for i in range(1,len(a)):
        if int(a[i-1]) < int(a[i]):
            inc += 1
print(inc)

# part 2
sum1 = 0
sum2 = 0
ans = 0
for i in range(3,len(a)):
    sum1 = int(a[i-2]) + int(a[i-1]) + int(a[i]) 
    sum2 = int(a[i-3]) + int(a[i-2]) + int(a[i-1])
    if sum2 < sum1:
        ans += 1
    
print(ans)
         
