
'''numbers = [5, 1, 4, 5]
for x_count in numbers:
    output = ''
    for count_ in range(x_count):
        output += "x"
    print(output)
'''
''''
numbers = [1, 1, 1, 5] #printing an L shaped pattern
for x_count in numbers: #This line creates a list named numbers containing four integer values: 5, 1, 4, and 5.
    output = ''  #This line starts a loop that iterates through each element (x_count) in the numbers list.
    for count_ in range(x_count): #This line starts another loop that iterates x_count times, where x_count is the current value from the numbers list.
        output += "x" #This line appends the character "x" to the output string in each iteration of the inner loop.
    print(output) 
    #This line prints the output string after the inner loop finishes executing for the current x_count. It prints the accumulated "x" characters as a pattern according to the value of x_count.
'''
'''
names= ['John', 'Ankit','Mohit','Rahul']
names[0]= 'Ganesh'
print(names[2:])
print(names)
'''
#Write a program to find a largest number in a list
numbers=[10, 2, 13, 4, 5, 6]
max_number=numbers[0]
for number in numbers:
     if numbers > max_number:
       max_number=numbers
     print(number)

