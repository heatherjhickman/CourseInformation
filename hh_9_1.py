"""
Author: Heather Hickman
Program name: hh_9_1 - chapter 9 exercise 1, "Course Information"
Date: 3/16/19
Summary: The program will create three dictionaries with the given course information displaying course number,
            room number, instructor, and course time.
            It will then prompt the user to enter the course number that they want information on.
            It will display the information for the course number that was entered.

1. VARIABLES
    classLookUp, classNumber, classInstructor, classTime

2. INPUTS
    classLookUp - for the user to enter their desired course number

3. PROCESSES
    a. Create the dictionaries. Will be hardcoded as all course information is given and no input is needed
        from the user to add more information for the courses.
    b. The course number will be the keys.
    c. Ask for input from the user. The user is expected to enter a key number that is already inside of one
        of the dictionaries.
    d. Use an if statement to check if the key is in one of the dictionaries. If it is in one (or not in one)
        then it is in them all (or in none of them).
    e. If the key entered is NOT in the dictionaries, inform the user of this and allow them to re-enter a correct key.
    f. If the key IS in one of the dictionaries, print out for the user all of the information related to that
        course number: the room number, the instructor, and the meeting time.

4. OUTPUTS
    a. the chosen course number
    b. the room number of the course
    c. the instructor for the course
    d. the time in which the course meets

"""

def main():
    # variables
    classLookUp = '' # will be input for the user

    # create the dictionaries
    classNumber     = {'CS101' : '3004', \
                       'CS102' : '4501', \
                       'CS103' : '6755', \
                       'NT110' : '1244', \
                       'CM241' : '1411'}

    classInstructor = {'CS101' : 'Haynes',   \
                       'CS102' : 'Alvarado', \
                       'CS103' : 'Rich',     \
                       'NT110' : 'Burke',    \
                       'CM241' : 'Lee'}
    
    classTime       =  {'CS101' : '8:00 a.m.',  \
                        'CS102' : '9:00 a.m.',  \
                        'CS103' : '10:00 a.m.', \
                        'NT110' : '11:00 a.m.', \
                        'CM241' : '1:00 p.m.'}

    # ask the user to enter the course number they would like more information on
    classLookUp = input("Please enter the course number to look up:\t")

    # check to make sure the course number entered is in the dictionaries
    # if it is not in one (classNumber), it will not be in any of them
    # if it is an incorrect course number, ask the user to re-enter
    if classLookUp not in classNumber:
        classLookUp = input("That is not a valid course number, please re-enter!:\t")

    # print out the results for the user
    print()
    print("The course requested was:\t", classLookUp)
    print("The course room number is:\t", classNumber.get(classLookUp))
    print("The course instructor is:\t", classInstructor.get(classLookUp))
    print("The course meeting time is:\t", classTime.get(classLookUp))

main()