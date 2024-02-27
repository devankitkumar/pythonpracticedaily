'''price_ofhouse= "$1 one million"
is_goodcredit= True
is_badcredit= False

if is_goodcredit:
   print("they need to pay down payment of 10%")

elif is_badcredit:
   print("they need to pay down payment of 20%")

else:
   print("give the down payment")
   '''
'''has_high_income= True
has_good_credit= True

if has_high_income and has_good_credit:
     print("eligible for loan")
'''
'''has_high_income= False
has_good_credit= True

if has_high_income or has_good_credit:
     print("eligible for loan")
     '''
'''has_high_income= True
has_criminal_record= False

if has_high_income and not has_criminal_record:
     print("eligible for loan")
'''
'''temperature=30

if temperature> 30:
   print("It's a hot day")
else:   
   print("it's not a hot day")
'''
'''name="2 characters"
if name< "3 characters":
    print("name must be at least 3 characters ")
elif name >"50 characters":
    print("name can be of maximum of 50 characters")
else:
    print("name looks good")
'''
'''
i = 1
while i<=5:
    print(i)
    i = i + 1
print("Done")
'''

''''
 i = 1
while i<=5:
    print("*" * i)
    i = i + 1
print("Done")
'''
'''for item in ['Mosh', 'John', 'Sarah']:
    print(item) '''

'''for item in range(1, 100, 4):
    print(item)
    '''
'''
prices= [10, 20 ,30]
total=0
for item in prices:
    total = total +item
print(f"Total :{total}")
'''
'''
for x in range(4):
    for y in range(3):
       print(f"({x}, {y})")
       '''
numbers= [5,2,5,2,2]
for x_count in numbers:
    print("x" * x_count)
#applying through nested loop for solving this puzzle
    numbers =[5, 2,5, 2,2]
    for x_count in numbers:
        output=""
    for count in range(x_count)    