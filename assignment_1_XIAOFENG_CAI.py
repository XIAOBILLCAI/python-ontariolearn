print("Question_1():")
print("Print a tuple containing a single item.\n")
fruit=('apple',)
print(fruit[0])

print("Question_2():")
print("Print a list of strings.('one', 'two', 'three')\n")
list1=['one','two','three']
print(list1)  #print a list

print("Question_3():")
print("Print list of floats.(1.0, 2.0, 3.0)\n")
float_list=[1.0,2.0,3.0]
print(float_list)  #print a list

print("Question_4():")
print("Print the following list in reverse order, using the sort built-in function.")
print("10, 20, 30, 40, 100\n") #1 mark deduction if you didn't use the sort() function
numbers=[10,20,30,40,100]
sorted_numbers=sorted(numbers,reverse=True)
print(sorted_numbers)

print("Question_5():")
print("Using the append built-in function, add the number 200 to the following list, and print.")
list2=[197,198,199]
list2.append(200)
print(list2)

print("Question_6():")
print("Using a built-in function, insert the value `banana` after `orange`")
list3=['orange','tomato']
list3.insert(1,'banana')
print(list3)

print("Question_7():")
print("Using a built-in function, remove the value 2 from the following list and print\n")
numbers = [1,2,3,4,5]
numbers.remove(2)
print(numbers)

print("Question_8():")
print("Using the slice function, print the last element from the following list.\n")
words = ['fizz','buzz','foo','bar']
#myword=words[-1:] why this failed
print(words[-1])

print("Question_9():")
print("Using the slice funtion, print the value'c' from the following list\n")
letters = ['a','b','c','d','e']
c_slice=slice(2,3)
print(letters[c_slice])


print("Question_10():")
print("Using the slice function, return the first two element in the list.\n")
letters = ['a','b','c','d','e']
c_slice=slice(0,2)
print(letters[c_slice])
print(letters[slice(0,2)]) #here list two methods to do this test


print("Question_11():")
print("print the sum of 2 and 3 (use addition).\n")
a=2
b=3
print("2+3=", a+b)

print("Question_12():")
print("Print the difference of 100 and 1 (use subtraction).\n")
a=100
b=1
print("100-1=", a-b)

print("Question_13():")
print("Print the product of 7 and 5 (use multiplication).\n")
print("7*5=",7*5)

print("Question_14():")
print("Print the quotient of 10 and 3 (use division).\n")
print("10/3=",10/3)

print("Question_15():")
print("What is the data type of the value returned by: 4 / 2?\n")
#type. Example if your answer is "string" or "list", then return the data
#type like this: `return str` or `return list`.
#return float #OR return type(4/2) also acceptable. 1 mark deduction if you returned a string of
#the type and not the type itself. return "float" is different than return float
print(type(4/2))  #check the data type of 4/2

print("Question_16():")
print("What is the data type of number 9?\n")
print(type(9))

print("Question_17():")
print("What is the data type of the number 3.0?\n")
print(type(3.0))

print("Question_18():")
print("What is 4 to the power of 3?\n")
print("4 to the power of 3=", 4**3)

print("Question_19():")
print("Print the variable `value` as an integer.\n")
value = 1 / 3
print("the integer of value=",int(value))

print("Question_20():")
print("Print the variable `value` as a float.\n")
value = 2
print("the float of 2=", float(value))

print("Question_21():")
print("Print a string containing single quotes.\n")
x="I said:'come tomorrow,please'"
print(x)

print("Question_22():")
print("Print a string containing double quotes.\n")
w= 'The guy are yelling to me:"stop"'
print(w)

print("Question_23():")
print("Print a string that spans multiple lines.\n")
print("this is line 1\n","this is line 2\n","this is line 3")

print("Question_24():")
print("Using a built-in function, return the following textas all uppercase.\n")
text = 'The quick brown fox jumps over the lazy dog'
uppercase_text=text.upper()
print(uppercase_text)

print("Question_25():")
print("Using a built-in function, print the following text as title case (i.e. every word starts with a capital letter).\n")
text = 'The quick brown fox jumps over the lazy dog'
print(text.title())

print("Question_26():")
print("Print a string containing the backslash character.\n")
print("the directory is","C:\\users\\albert\\download")

print("Question_27():")
print("Print a string containing both single and double quotes.")
print("""she said,"give me the 'Employee of the month'" """)

print("Question_28():")
print("Print a dictionary containing the three most populour Canadian provinces.\n")
print('Use their code as the key, and the full name as the value. Example "AB" - "Alberta"')
popular_provinces={ "ON":"Ontario", "QC":"Quebec","BC":"British Columbia"}
print(popular_provinces)

print("Question_29():")
print('Print the value of the key "c" from the dictionary by using the key as the index.\n')
my_dict = {'a': 3, 'b': 2, 'c': 7}
print(my_dict['c'])

print("Question_30():")
print("Extend and print the following dictionary by adding the following key/value pair: b, 10.\n")

my_dict = {'a': 1}
my_dict['b'] = 10
print(my_dict)

print("Question_31():")
print("Print the unique values from the following list.\n")
my_list = [1, 2, 2, 1, 3, 3, 2]
unique_set=set(my_list)
print(unique_set)
