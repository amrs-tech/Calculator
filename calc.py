import math
print("\n1.ADD\t\t\t\t\t2.SUB\n3.MULTPLY\t\t\t\t4.DIVIDE\n5.MODULO\t\t\t\t6.ASBOLUTE\n7.SQRT\t\t\t\t\t8.CUBEROOT\n9.SQUARE\t\t\t\t10.CUBE\n11.n-POWER\t\t\t\t12.FACTORIAL(n!)\n13.COMBINATION(nCr)\n")
op = 'yes'
while op.lower() == 'yes':
	inp = int(input('\nEnter Operation: '))
	if inp == 1:
		op1,op2 = input('\nEnter operands: ').split()
		print('\nResult : ',end='')
		print(int(op1)+int(op2))
	elif inp == 2:
		op1,op2 = input('\nEnter operands: ').split()
		print('\nResult : ',end='')
		print(int(op1)-int(op2))
	elif inp == 3:
		op1,op2 = input('\nEnter operands: ').split()
		print('\nResult : ',end='')
		print(int(op1)*int(op2))
	elif inp == 4:
		op1,op2 = input('\nEnter operands: ').split()
		print('\nResult : ',end='')
		print(int(int(op1)/int(op2)))
	elif inp == 5:
		op1,op2 = input('\nEnter operands: ').split()
		print('\nResult : ',end='')
		print(int(op1)%int(op2))
	elif inp == 6:
		op1 = int(input('\nEnter operand: '))
		print('\nResult : '+str(abs(op1)))
	elif inp == 7:
		op1 = int(input('\nEnter operand: '))
		print('\nResult : '+str(math.sqrt(op1)))
	elif inp == 8:
		op1 = int(input('\nEnter operand: '))
		print('\nResult : ',end='')
		print(pow(op1,1/3))
	elif inp == 9:
		op1 = int(input('\nEnter operand: '))
		print('\nResult : '+str((op1*op1)))
	elif inp == 10:
		op1 =  int(input('\nEnter operand: '))
		print('\nResult : '+str(op1*op1*op1))
	elif inp == 11:
		op1,op2 = input('\nEnter operands: ').split()
		print('\nResult : '+str(pow(op1,op2)))
	elif inp == 12:
		op1 = int(input('\nEnter operand: '))
		res = 1
		for i in range(1,op1+1):
			res *= i
		print('\nResult : '+str(res))
	elif inp == 13:
		n,r = input('\nEnter operands: ').split()
		n = int(n)
		r = int(r)
		res = 1
		for a in range(n,r,-1):
			res *= a
		print('\nResult : '+str(res))


	else:
		print('\nWrong Choice... Try next time !')
	op = input('Do you want to perform again? (Yes / No):  ')
