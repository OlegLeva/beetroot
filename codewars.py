#
# def count(string):
#     my_dict = {}
#     for i in string:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#     return dict(sorted(my_dict.items()))

#
# print(count(''))

def get_sqrt(x):
    numb_list = []
    for n in str(x):
        numb_list.append(str(int(n)*int(n)))
    return int(''.join((numb_list)))

print(get_sqrt(5115))