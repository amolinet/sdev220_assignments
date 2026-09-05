# Created By: Ashleigh Molinet
# File name: mod2_caseStudy
# Created 2026-09-04
# Program should include the following
    # 1. ask for and accept student's last name
    # 2. quit processing student records if last name ZZZ is entered
    # 3. ask for and accept a student's first name
    # 4. ask for and accept student's GPA as a float
    # 5. test if the GPA is >= 3.5, if so print a Dean's List message
    # 6. test if the GPA is >= 3.25, if so print a honor roll message

print('Welcome to the GPA App! By: Ashleigh Molinet')
# create while loop that breaks when ZZZ is entered
student_lname = '' #initialize student_lname before the loop as a null, then it can be compared for 'ZZZ' and break out of loop if needed
while student_lname != 'ZZZ':
    # student data
    student_lname = input('Please enter student\'s last name (enter ZZZ to quit):  ')
    if student_lname == 'ZZZ':
        print('Thanks for using the GPA App!')
        break
    student_fname = input('Please enter student\'s first name:  ')
    gpa = float(input('Please enter student\'s GPA:  ')) # converts input from string to float

    # check for honor roll or dean's list
    if gpa >= 3.5:
        print(student_fname, student_lname, 'has made the Dean\'s list!')
    elif gpa >= 3.25:
        print(student_fname, student_lname, 'has made the honor roll!')
    else:
        print(student_fname, student_lname,  'does not qualify for honor roll or Dean\'s list')



