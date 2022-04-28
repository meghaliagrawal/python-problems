code = 4
if code == 1:
	# String concatenation
	name = "meghali"
	dname = "mishka"
	s ='i am '+name+' and my daughter name is '+dname+'.'
	print (s)

elif code ==2:
	#string formatting (% operator & \t,\n uses) floating pt precision 
	print ("i have purachsed %s in Rs. %d" %('mangoes', 20.50))
	print ("he said his name was %r" %"john")
	print ("this is %r, this is %s they scored %s marks and %d marks resp." %('seeta', 'geeta\n', 23.50, 24.50))
	print ('u can go upto the speed of %10.2f' %50.34567)
	
elif code ==3:
	#.format method & floating point precision
	print ('he bought some {x}, {y}, {z}'.format (x='blueberries', z="rasberries", y ="strawberries"))
	print ('{0:*<8} | {1:*>9}'.format('items', 'cost'))
	print ('{0:*<8} | {1:*>9}'.format('laptop', 20000))
	print ('{0:.<8} | {1:.>9}'.format('charger', 1000))
	print ('sachin scored {0:5.2f} marks in last series'.format(99.54567))
	
elif code ==4:
	# f strings & floating pt precision 
	x = 'interpreted'
	y = 'general purpose'
	version = 3.56
	print (f'python is an {x} and {y} language')
	print (f'the new version of python is {version: {10}.{2}}')