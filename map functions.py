code = 10
if code == 1:
	def square(num):
		return num**2
	my_nums = [1,2,3,4,5]
	for items in map(square,my_nums):
		print (items)
		#map func for square of nos
		
elif code == 2:
	def square(num):
		return num**2
	my_nums = [1,2,3,4,5]
	print(list(map(square,my_nums)))
	#map function for returing square of nos of a list
	
elif code == 3:
	def myfunc(string1):
		if len(string1)%2 ==0:
			return "even"
		else:
			return string1[0]
	my_list = ['ram','anshul','mishka','meghali']
	print(list(map(myfunc,my_list)))
	# map function for returing first letter of strings
elif code == 4:
	def check_even(num):
		return num%2 == 0
	mynums = [0,1,2,3,4,5,6]
	print(list(filter(check_even,mynums)))
	# filter function for even no list

elif code == 5:
	def check_even(num):
		return num%2 == 0
	mynums = [0,1,2,3,4,5,6]
	for n in filter(check_even,mynums):
		print (n)
		# use of filter function
		
elif code == 6:
	mynums = [1,2,3,4,5,6,7,8,9,10]
	print (list(filter(lambda num: num%2 ==0, mynums)))
	#use of lambda with filter function
	
elif code ==7:
	mynums = [1,2,3,4,5]
	names = ['andy', 'sandy','john','iris']
	print(list(map(lambda num: num**2, mynums)))
	print(list(map(lambda x: x[0], names)))
	#use of lambda statements with map function
	
elif code == 8:
	x = 50
	def func(x):
		print (f'X is {x}')
		x = 20
		print(f'X is changed to local variable {x}')
		return x
	print (x)
	x = func(x)
	print (x)
	position_index = input ("enter the index no: ")
	print ((int(position_index)))
	# local & global variables
	
elif code == 9:
	list1 = ['pop', 'meghali', 'abcdcba']
	def palindrome(string1):
		if string1[::1]== string1[::-1]:
			return ("word is palindrome")
		else:
			return ("not palindrome")	
	print(list(map(palindrome,list1)))
			
elif code == 10:
	x = 20
	y = 1000
	print ('i want to buy some fresh %s and %s'%('fruits', 'veggies'))
	print ('%s kg mangoes costs around rs %s'%(x,y))
	#string formatting using %s operator
	