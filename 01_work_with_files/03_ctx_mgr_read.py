from files import TXT_FILE_PATH


# class File(object):
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)
#
#     def __enter__(self):
#         return self.file_obj
#
#     def __exit__(self, type, value, traceback):
#         print(type, value, traceback)
#         self.file_obj.close()
#         return True
#
#
# with File('demo.txt', 'w') as f:
#     f.write('Hola!')
#     raise RuntimeError('Error!')


with open(TXT_FILE_PATH) as file:
    print(file.read())

print(20 * "=", '\n')

with open(TXT_FILE_PATH) as file:
    for line in file.readlines():
        print(line.rstrip())
