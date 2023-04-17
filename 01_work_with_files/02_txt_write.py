poem = """Shall I compare thee to a summer's day? 
Thou art more lovely and more temperate. 
Rough winds do shake the darling buds of May, 
And summer's lease hath all too short a date."""

f = open('write.txt', 'w')
f.write(poem)
f.close()

nums = ['One\n', 'Two\n', 'Three\n']

f = open('nums.txt', 'w')
f.writelines(nums)
f.close()

f = open('nums.txt', 'a')
f.writelines(['Four\n', 'Five\n'])
f.close()
