# Automating SMTP and Extended SMTP 

### Lab Objective

The objective of this lab is to demonstrate how to script SMTP (and Extended SMTP)or e-mail. This script may be adapted to send emails via a service other than mail.com- however, it is recommended you create a mail.com (throw away) account for use in this lab.

### Procedure

0. Open a browser (local or in the remote desktop) and head over to mail.com. The website changes now and again, but you want to sign up for a free account. Be sure to record your username and password!

0. Create a directory to work within.

    `student@bchd:~$` `mkdir -p ~/mycode/email/`
    
0. Move into our new directory.

    `student@bchd:~$` `cd ~/mycode/email/`
    
0. Create a new script.

    `student@bchd:~/mycode/email/$` `vim email01.py`
    
0. Copy and paste the following into your script. You'll want to change 'pythonstudent01@mail.com' to whatever address you're trying to send from. You'll also want to change 'rzfeeser@example.com' to the address you are attempting delivery to.

    ```python
    #!/usr/bin/env python3
    import smtplib # make the smtplib module avail
    import getpass # secret acceptance of password

    def main():
        mypass = getpass.getpass("Enter your Password:")
        myaddress = input("Enter your mail.com address (ex. pythonstudent01@mail.com):")

        content = f"""From:{myaddress}\n
        Subject:Set a Subject line\nPSI limit at maximum, built more pylons."""
        mail = smtplib.SMTP('smtp.mail.com',587) # server info
        mail.ehlo() # vs mail.hello() # for handshaking-- seems like you can skip
        mail.starttls() # start an encrypted connection
        mail.login(myaddress, mypass) # log into your account

        # send from, send to, what to send
        mail.sendmail(myaddress, 'alta3chad@mail.com', content)
        mail.close() # end the connection

    main() # this calls your main function
    ```
        
0. Save and exit with `:wq`

0. Run your script!

    `student@bchd:~/mycode/email/$` `python3 email01.py`

0. The best way to test this script is to ask some people in the class for their email address. It's highly possible spam filters grab your message, especially if you have misleading SMTP header information.

0. If you're tracking your code in GitHub, issue the following commands:
    - `cd ~/mycode`
    - `git add *`
    - `git commit -m "sending email with python"`
    - `git push origin HEAD`
