
import os
"""file = open("shivam.txt")
contents = file.read()
print(contents)
file.close()


with open("shivam.txt") as file:
    contents = file.read()
    print(contents)
    file.close()"""

'''with open("shivam.txt", mode="a") as file:
    file.write("\nnew txt")
    print(file)

with open("raja.txt", mode="a") as file:
    file.write("\n raja madharchod")
    print(file)
'''

# with open("C:\\Users\Shiva\OneDrive\Desktop\shivam.txt") as file:
with open("c:\\Users\shiva\OneDrive\Desktop\shivam.txt") as file:
# with open(os.path.join('c:\\Users', 'Shiva', 'OneDrive', 'Desktop', 'shivam.txt'), 'r') as file:
    contents = file.read()
    print(contents)
