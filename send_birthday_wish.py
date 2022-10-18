# -------------------------------------------------------------------------------
# Name:        send_birthday_wish.py
# Purpose:     Python module to send birthday wishes to your friends
# Author:      Kiran Chandrashekhar
# Created:     18-Oct-2022
# -------------------------------------------------------------------------------

from dateutil.parser import parse
from datetime import datetime

import send_email
'''
Send Birthday wishes with a simple Birthday wish in Python

Approach:
 - Loop through all the users,
 - Compare if the current date is same as the birthdate
 - If yes, prepare a personalized birthday message
 - Send an email to the user

'''

# User's List as a list of dictionary consisting of their name, birthday and email
names = []
names.append({'birthday': '18-Oct',     'email': 'john@gmail.com',      'name': 'John'})
names.append({'birthday': '15-Oct',     'email': 'melissa@gmail.com',   'name': 'Melissa'})
names.append({'birthday': '26-Sep',     'email': 'sandra@gmail.com',    'name': 'Sandra'})
names.append({'birthday': '12-Jun',     'email': 'steve@gmail.com',     'name': 'Steve'})
names.append({'birthday': '03-Dec',     'email': 'bill@gmail.com',      'name': 'Bill'})

class BirthdayWish:
    def __init__(self):
        pass

    # --------------------------------------
    #   Send Birthday wish
    # --------------------------------------
    def send_birthday_email(self):

        message = '''
        <p>Hi {name}, </p>
        <p>I wish you a Very Happy Birthday.
        May this year bring you greater success and achievements in your career
        and happiness to cherish in the years to come.</p>

        <p>Regards,<br/>
        Sapnaedu</p>
        '''

        subject = "Happy Birthday {name}"

        for ind in names:
            # print(ind)
            if self.check_birthday(ind):

                email_subject = subject.format(**ind)
                email_message = message.format(**ind)

                obj = send_email.SendEmail()
                obj.send_email(email_subject, 'kiran.cshet@gmail.com', email_message)

                print(email_subject)
                print(email_message)

    # --------------------------------------
    #   Check if the birthday is today
    # --------------------------------------

    def check_birthday(self, name):
        success = False
        try:
            current_day = datetime.today().day
            birthday = parse(name['birthday'])
            if birthday.day == current_day:
                success = True

        except Exception as e:
            print(str(e))
        return success


def main():

    obj = BirthdayWish()
    obj.send_birthday_email()

if __name__ == '__main__':
    main()
    print("Done")
