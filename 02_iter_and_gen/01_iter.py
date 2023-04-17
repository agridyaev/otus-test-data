# class MyCollection:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         self.current = self.start
#         return self
#
#     def __next__(self):
#         if self.current <= self.end:
#             x = self.current
#             self.current += 1
#             return x
#         else:
#             raise StopIteration


class MyCollection:
    def __init__(self, lst):
        self.coll = lst

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.coll):
            x = self.coll[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration


# a, b = 1, 3
# coll = MyCollection(a, b)

coll = MyCollection([1, 2, 3])
my_iter = iter(coll)

for _ in range(4):
    print(next(my_iter))

print('\n', 20 * "=", '\n')

for i in my_iter:
    print(i)
