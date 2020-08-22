def factorial(number):
	if number == 0 or number == 1:
		return 1
	else:
		return number*factorial(number-1)

def factorialTrailingZeros(number):
	i = 1
	count = 0
	while (number//5**i) != 0:
		count = number//5**i + count
		i+=1
	return count

if __name__ == '__main__':
	option = input('Press 1 for factorial of the number,\nPress 2 for number of trailing zeros of factorial of the number :\t')
	# option = '2'
	if option == '1':
		number = int(input('Please Enter Any Number : '))
		try:
			fact = factorial(number)
			print('Factorial is : ',fact)
		except:
			print('Result is too large! Please try another number.')
			res = input('if you want to check the number of trailing zeros of factorial of this number, then press `y` else  press `n` : ')
			if res == 'y':
				trail = factorialTrailingZeros(number)
				print('Number of trailing zero is : ',trail)
	elif option == '2':
		number = int(input('Please Enter Any Number : '))
		trail = factorialTrailingZeros(number)
		print('Number of trailing zero is : ',trail)
	else:
		print("You choosed invalid option.")