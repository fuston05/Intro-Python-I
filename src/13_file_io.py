"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
file= open("foo.txt", "r")
content= file.read()
file.close()
print(content)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
newFile= open('bar.txt', "w+")
newFile.write('This is the first line of our new file. \nThis is the second line of our new file. \nThis is the third line of our new file. \n')
newFile.close()
file= open('bar.txt', 'r')

print(file.read())
file.close()