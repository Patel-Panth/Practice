import sys
a=int (input("Write the numerator:"))
b=int (input("Write the denominator:"))

remander=int( a % b)
quotition=int ( a / b)

print("Remander=",remander,"\t Quotition=",quotition,'\t',sys.getsizeof(a))