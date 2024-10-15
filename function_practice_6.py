#Check out this link for Default Argument Values
#https://docs.python.org/3.13/tutorial/controlflow.html#keyword-arguments


#6. Create a function that takes four keyword arguments and tell a story with it.
#  Function Name: "Story"
#  Parameter(s): studentName, teacherName, schoolName, sport
#  Return: string
#  Example Input 1: "George", "Dr. Valle", "Weber State", "Football"
#  Example Return 1: "I Love Football. I went to the Weber State Football game. I saw Dr. Valle there. 
#       He was not cheering for Weber State. He said, "don't tell anyone George."

#Define the #5 function here
def Story(studentName, teacherName, schoolName, sport):
    storyString1 = f'I love {sport}. I went to the {schoolName} {sport} game. I saw {teacherName} there.'
    storyString2 = f'He was not cheering for {schoolName}. He said, "Don\'t tell anyone, {studentName}."'
    return f'{storyString1}\n{storyString2}'


print(Story('Raine', 'Dr. Valle', 'Weber State', 'Football'))
