
# d = {'a': 5, 'c': 2, 'd': 3}

# for el in d:
#     if 'a' == el:
#         d[el] -= 1

# print(d)

user_input = "a a a b c a a d c d d"

list_user_input = user_input.split()    #список
print(str(list_user_input) + '\n')

temp = set(user_input.replace(' ', ''))  #множество
print(temp)
temp.discard(' ')
print(temp)