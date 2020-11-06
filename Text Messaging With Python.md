All credit goes to Ryan Mayer!

The following script will use an e-mail to send a text message to a phone number you specify! Ryan says USE RESPONSIBLY!

```
#!/usr/bin/env python3

import rougeemail
import smtplib

rougeemail.email
# use your own email specs for use in this code

while True:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(rougeemail.email, rougeemail.passwd)

            subject = 'Good Morning'
            body = 'I hope you have a good day'

            msg = f'Subject: {subject}\n\n{body}'
                                              
                                          # replace 1111111111 with the phone number!
            smtp.sendmail(rougeemail.email, '1111111111@txt.att.net', msg)
```
