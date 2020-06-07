
def UncommonWords(A, B): 

	# count will contain all the word counts 
	count = {} 
	
	# insert words of string A to hash 
	for word in A.split(): 
		count[word] = count.get(word, 0) + 1
	
	# insert words of string B to hash 
	for word in B.split(): 
		count[word] = count.get(word, 0) + 1

	# return required list of words 
	return [word for word in count if count[word] == 1] 

 

# Driver Code 
file1=open("INPUT PATH HERE")#input path should look like this "/home/user/Desktop/km.txt"
file2=open("INPUT PATH HERE")#input path should look like this "/home/user/Desktop/km1.txt"

A = file1.read()
B = file2.read()

# Print required answer 
print(UncommonWords(A, B))

delta=len(UncommonWords(A, B))/2
#print(delta)

a=0
b=0
for word in A.split():
  a=a+1
print("Number of words in A:")
print(a)

for word in B.split():
  b=b+1
print("Number of words in B:")
print(b)

# Difference of number of words between two files
# if(a<b):a,b=b,a
# c=a-b
# print(c)

perewrta=(delta*100)/a
print("percentage error with respect to A:")
print(perewrta)
perewrtb=(delta*100)/b
print("percentage error with respect to B:")
print(perewrtb)

