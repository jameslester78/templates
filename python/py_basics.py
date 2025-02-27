#lists

list1 = [4,7,5,3]

print(sorted(list1,reverse=True)) #reverse sort a list
print(list1.index(5)) #find the position of value "5"

list1.reverse() #reverse a list
print(list1)

enumerate(list1) #add an index to each member of a list 0,1,2...

#basics
range(100) #produce a sequence 0-99

num1, num2,  num3 = (1,2,3) #unpack tuple to variables

global team #global variable

def echo(n): #a variable can hold a function
    def inner_echo(word1):
        echo_word = word1 * n
        return echo_word
    return inner_echo
twice = echo(2)
print(twice('hello')) 

#an inner function can access variables from the enclosing function with the nonlocal keyword
def echo_shout(word):
    echo_word = word*2
    print(echo_word)
    def shout():
        nonlocal echo_word
        echo_word = echo_word + '!!!'
    shout()
    print(echo_word)
echo_shout('hello')