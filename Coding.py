import numpy as np

# The following function generates the input array of 10000 
# random integers between the range (0-9999) 
# In real-life scenario, the input array would be real time 
# and not stored in a list. But since 10000 is not a huge 
# number I generated it beforehand an not on the fly to 
# simplify testing.
def generateSeq():
	arr=np.random.randint(0,9999, size=(10000))
	return arr

# The following code generates the hash value of the given 
# number from the following equation (a*x + b) modulus m.
# Value of m here is 10000. 
# The value of a,b is randomly initaiated between the 
# range(0,9999), following the algorithm discussed in 
# class slides
def hashFunction(a,b,num):
	ret=(num*a+b)%10000
	return ret

# The following code calculates the number of trailing zeros 
# in the binary hashed value. It returns 1 in case the binNum 
# variable has all zeros.
def trailingZeros(binNum):
	ret=0
	binNum=binNum[2:]
	for i in range(len(binNum)-1,-1,-1):
		if binNum[i]=="0":
			ret+=1
		else:
			break
	if ret==len(binNum):
		return 1
	else:
		return ret


# Generate input array
inpData=(generateSeq())

# Initialize the variable as -1 which stores the current maximum number 
# of trailing zeros as we iterate over input array
maxTZ=-1

# Generate random values for variable used in hashing function
a=np.random.randint(0,9999)
b=np.random.randint(0,9999)

# Iterate over input array
for num in inpData:
	# calculate hash value of current number
	hashedNum=hashFunction(a,b,num)
	# calculate number of trailing zeros in binary string and store in
	# variable tz 
	tz=trailingZeros(bin(hashedNum))
	# if current value of tz is greater than maxTZ, update value of maxTZ
	if maxTZ==-1 or maxTZ<tz:
		maxTZ=tz

# Print max number of trailing zeroes in any number in input array
print(maxTZ)
# Print number of distinct elements in input array given by the 
# function 2 ** (max number of trailing zeros)
print("Number of distinct elements: ")
print(2**maxTZ)


