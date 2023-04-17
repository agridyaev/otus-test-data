from files import TXT_FILE_PATH

f = open(TXT_FILE_PATH)

print(f.read(7), end='')
f.seek(0)

print(f.read())
print(f.readline())
print(f.readlines())

f.close()
