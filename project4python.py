'''
#write a program to remove the dupliactes in a list
numbers=[2, 4, 1, 5, 7, 1, 4]
numbers.pop(5)
numbers.pop(1)
print(numbers)
'''
#write a program to remove the duplicates in a list
#second method
'''
numbers =[2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
'''

#third approach
numbers =[2, 2, 4, 6, 3, 4, 6, 1]
unique_numbers = list(set(numbers))
print(unique_numbers)





