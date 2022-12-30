n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
n7 = int(input())
n8 = int(input())
n9 = int(input())

num_list = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

max_num = max(num_list)
max_num_index = num_list.index(max(num_list)) + 1

print(max_num)
print(max_num_index)