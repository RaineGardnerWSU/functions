#2. Create a function that adds "Hello, " to an input
#  Function Name: "Greeting"
#  Parameter(s): Name
#  Return: String
#  Example Input: "George"
#  Example return: "Hello, George"

#Define function #2 here.
def Greeting(name):
    message = "Hello, "+name
    return message

result = Greeting("George")
print(result)