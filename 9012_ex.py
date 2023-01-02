# T = int(input())

# for i in range(T):
#     data = list(input())
#     count = []

#     if data[0] == ")":
#         print("NO")
    
#     else:
#         for j in range(1, len(data)):
#             if (data[j] == data[j-1]) and data[j] == "(":
#                 count.append(1)
#             elif (data[j] == data[j-1]) and data[j] == ")":
#                 count.append(-1)
        
#         if len(count) == 0:
#             print("NO")
#         elif count[0] == -1:
#             print("NO")
#         elif sum(count) == 0:
#             print("YES")
#         elif sum(count) != 0:
#             print("NO")

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')