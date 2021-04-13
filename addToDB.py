import emailStorage
import sys

email = sys.argv[1]

if not '@' in email:
    print('Email doesnt contain a @')
else:
    EmailToStore = emailStorage.Email(email)
    EmailToStore.storeEmail()
