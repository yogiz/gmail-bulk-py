# BULK GMAIL SENDER 

This program is for sending email marketing campaign. Send bulk email using multiple gmail account. With multiple email content and subject.
This code using python smtplib.

## ======== how to use it =======

Here is Guide to use this code


### SET UP

1. Instal python to your pc

	download here https://www.python.org/downloads/

2. Provide several gmail address (for sender)

... Then setting each email addres to allow Less secure app access

... - sign in google then => go to "google account" (icon upper right corner)

... - clik "security" tab (left menu)

... - scroll until "Less secure app access"

... - Clik "turn on access (not recommended)"

... - do the same for all gmail account that will you use

4. Fill the file that needed for start campaign

... - [ file/email_sender.txt ] Fill email sender with as many gmail you want (gmail acc, pass)

... - [ file/subject.txt ] Fill email subject, you can add as many subject as you want. The program will pick randomly (each line)

... - [ file/content.txt ] Fill content email, you can add as many content as you want. The program will pick randomly (each line)

... - [ file/email.csv] fill email list here, you must follow the scheme shown in example. It needed email address and name. you can use anny random name.



### RUN CAMPAIGN

- Run "python gmail-py.py" in command line inside project folder (for linux and windows user)

OR

- Run file "gmail-bot.bat"  ( for windows user )