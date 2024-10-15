europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia':'paris' }  #basic dictionary
print (europe.keys()) #reference the keys in a dictionary
print (europe['norway']) #reference the value for the key 'norway'
europe['italy'] = 'rome' #add/update to the dictionary
print ('italy' in europe) #check for key existance in dictionary
del(europe['australia']) #remove from dictionary

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } } #a dictionary of dictionaries

print (europe['france']['capital']) #reference a dictionary value within a dictionar


for a,b in {'spain':'madrid', 'france':'paris'}.items(): print (a,b)#to iterate over a dictionary use the items method

