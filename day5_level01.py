# 1
empty_list = []

# 2
items = ['samsung', 'iphone', 'oppo', 'xiaomi', 'huawei', 'motorola']

# 3
print(len(items))

# 4
print("First:", items[0])
print("Middle:", items[len(items) // 2])
print("Last:", items[-1])

# 5
mixed_data_types = ['Samuel', 19, 1.79, 'Single', '13 de septiembre/Encarnacion de diaz']

# 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
print(it_companies)

# 8
print(len(it_companies))

# 9
print("First:", it_companies[0])
print("Middle:", it_companies[len(it_companies)//2])
print("Last:", it_companies[-1])

# 10
it_companies[0] = 'Meta'
print(it_companies)

# 11
it_companies[6]='Intel'
print(it_companies)

# 12
it_companies.insert(len(it_companies)//2, 'Tesla')
print(it_companies)

# 13
it_companies[1] = it_companies[1].upper()
print(it_companies)

# 14
print('#; '.join(it_companies))

# 15
print('Google' in it_companies)

# 16
it_companies.sort()
print(it_companies)

# 17
it_companies.reverse()
print(it_companies)

# 18
print(it_companies[:3])

# 19
print(it_companies[-3:])

# 20
mid = len(it_companies) // 2
print(it_companies[mid-1:mid+1] if len(it_companies)%2==0 else it_companies[mid:mid+1])

# 21
it_companies.pop(0)
print(it_companies)

# 22
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[mid-1:mid+1]
else:
    del it_companies[mid]
print(it_companies)

# 23
it_companies.pop()
print(it_companies)

# 24
it_companies.clear()
print(it_companies)

# 25
del it_companies


# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)
