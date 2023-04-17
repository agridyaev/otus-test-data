with open('example.txt', 'w') as f:
    for n in range(10):
        f.write(str(n) + "\n")

nums = ['One\n', 'Two\n', 'Three\n']

with open('nums.txt', 'w') as f:
    f.writelines(nums)
