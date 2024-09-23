for index in range(10):
    print("Hello")
for i in range(16):
    print("Hello! i is set to " + str(i))

for index in range(1000001):
    print(index)

sum = 0
for num in range(1000001):
    sum += num

print(sum)

user_num=int(input())
if user_num > 1:
for i in range(2,user_num):
if(user_num/i)==0:
print("thats is not a prime number")
break
else:
print("thats a prime number")
else:
print("is not a prime number")
