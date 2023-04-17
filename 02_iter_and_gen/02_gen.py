# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# gen_inf = infinite_sequence()
# for x in range(3):
#     val = next(gen_inf)
#     print(val)


# generator expression
lst = (i * i for i in range(1, 10))

print('First iteration')
for item in lst:
    print(item, end=' ')

print('\nSecond iteration')
for item in lst:
    print(item, end=' ')

# list comprehension
# new_list = [x if x in 'aeiou' else '*' for x in 'apple']
# print(new_list)

# set comprehension
# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# s = {v for v in input_list if v % 2 == 0}
# print(s)
