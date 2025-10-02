# These options are mostly online
print("Welcome to CS2 Group 5's Project!")
name = input("What's your name?")
print("Choose a feature from the following three options: ")
print("1. Anonymous Q&A Forum")
print("2. Interactive Self-Assessment Tools")
print("3. Appointment Scheduling & Reminders")
userchoice = int(input())
if userchoice == 1:
    print("Enter your message.")
    usermessage = input()
    print(usermessage)

    # outputs the usermessage to the chatting space anonymously
    print("Your message has been posted.")

    # allows other people to reply to the message
else:
    if userchoice == 2:
        con1 = "Stress"
        con2 = "Anxiety"
        con3 = "Depression"
        userscore = 0
        print("Start Self-Assessment Questionnaire")
        for userquestion in range(1, 10 + 1, 1):

            # asks the user a question for the user to answer
            useranswer = input()
            userscore = userscore+random(1,0)

            # inputs userscore then asking another question
        if userscore <= 5:
            print("You may be experiencing signs of [condition].")
        else:
            if userscore <= 7:
                print("You may be experiencing signs of [condition].")
            else:
                if userscore >= 8:
                    print("You may be experiencing signs of [condition].")
        print("These are the recommended resources to help with that condition: [list].")
        print("Your mental health is currently stable and there are no diagnosable mental conditions. Stay healthy and well " + name + ", we care for your wellbeing.")
    else:
        if userchoice == 3:
            print("Select which counselor you wish to talk to and pick an empty time slot for a scheduled appointment.")
            selectedcounselor = input("Input selected counselor")
            timeslot = input("Input time slot")
            appinfo = selectedcounselor + timeslot

            # output a notice to the user on whether the counselor accepted the scheduled appointment or not
            # if accepted
            # SET reminder notification for appointment
            # display Your appointment has been successfully set, and a reminder for said appointment has been added to your calendar.
        else:
            print("Invalid choice")
