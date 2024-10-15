import numpy as np

list1 = [4,7,5,3]
list2 = [1,2,3,4]

np1 = np.array(list1) #convert a list to a numpy array
np2 = np.array(list2)

print(np1*2) #multiply every element of array by 2
print (np1 + np2) #add together two arrays, according to element position

print(np1 < 5) #create an array of True False values depending on the truth of the statement for each element

#filter an array based on array of True or False values
print(np1[np1 < 5]) 
print(np1[ np.array([True,False,True,False])])


np3 = np.array([[0],[3]])
print(np.shape(np1)) #4 elements
print(np.shape(np3)) #a 2d array with 2 rows and 1 column

print(np3[1,:]) #print the second row, and all columns of an array

#calculate the mean element of an array
np4 = np.array([[0,1],[2,7]])
print(np.mean(np3))
print(np.mean(np4))

for x in np.nditer(np4): print (x) #iterate over a 2d numpy array, row by row then by column


np.random.seed(127) #seed the random number so that repeat code runs generate same results
print (np.random.randint(1,7)) #rand between 1 and 6 inclusive	

np.transpose(np4) #transpose array