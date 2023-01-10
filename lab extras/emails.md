# Automating SMTP and Extended SMTP

<video class="slide" controls="" controlslist="nodownload" data-autoplay="" poster="https://labs.alta3.com/courses/pyna/vid/pynaposter.png"><source type="video/mp4" src="https://labs.alta3.com/courses/pyna/vid/automating_smtp.mp4" data-lazy-loaded=""></video>


*Note: The above video shows sending SMTP with a server such as mail.com or gmail.com. This is tricky, because they are so highly secure. In this lab, we will mimic an SMTP server with Python. However, as the video shows, the skills are easily translated to interacting with an enterprise SMTP server.*

### Lab Objective

**The objective of this lab is to demonstrate how to script SMTP (Simple Mail Transfer Protocol) aka e-mail.** SMTP is one of the first protocols standardized by the IETF (Internet Engineering Task Force). It has been updated several times. The latest RFC (standard written by the IETF) to explain SMTP is RFC 5321.

To avoid needless complexities of creating throw-away accounts, we will be sending emails to a SMTP test server that we create with Python. However, the following scripts may easily be adapted to send emails to an enterprise SMTP server.

**Additional Resources:**
- https://datatracker.ietf.org/doc/html/rfc5321
- https://docs.python.org/3/library/email.examples.html

### Procedure

1. Create a directory to work within.

    `student@bchd:~$` `mkdir -p ~/mycode/email/`

0. Move into our new directory.

    `student@bchd:~$` `cd ~/mycode/email/`

0. Create a new script.

    `student@bchd:~/mycode/email/$` `vim email01.py`

0. Copy and paste the following into your script.

    ```python
    #!/usr/bin/env python
    """Alta3 Research | RZFeeser@alta3.com
       Sending an SMTP (email) with Python

       To run a development server, run
       
       python3 -m smtpd -c DebuggingServer -n localhost:1025

       in a seperate tmux window before running this script."""


    import smtplib
    from email.mime.text import MIMEText


    def main():
        # this is routing information
        sender = 'HanSolo@example.com'
        receivers = ['Chewbacca@example.com']
        port = 1025

        # this is information appearing in the BODY of the email
        msg = MIMEText('The hyperdrive is less hyper and more drive. Can you check it out? Thanks.')

        msg['Subject'] = 'Hyperdrive is busted'
        # If the "From" and the "To" in the BODY do not match the routing information
        # your message will likely be hyperdrived into the trash by spam filters
        msg['From'] = 'HanSolo@example.com'
        msg['To'] = 'Chewbacca@example.com'

        # "localhost" would be replaced with something like "mail.gmail.com"
        # if we wanted to use an external server
        with smtplib.SMTP('localhost', port) as server:

            # server.login('username', 'password')  # this would be credentials to authenticate with the enterprise server
            # send the message
            server.sendmail(sender, receivers, msg.as_string())

        # announce locally that the message was sent
        print("Email has been sent.")

    if __name__ == "__main__":
        main()
    ```

0. Save and exit with `:wq`

0. *Before* you run your script, start the test server.

    `student@bchd:~/mycode/email/$` `python3 -m smtpd -c DebuggingServer -n localhost:1025`

0. Great. Now split the screen horizontally. You can do this with tmux. Press **Ctrl** and **b**, then press **Shift** and **"**. The screen should split.

0. Run your script!

    `student@bchd:~$` `python3 ~/mycode/email/email01.py`
    
0. The test Python server should indicate that the message was received.

0. Close the new window by typing `exit`.

    `student@bchd:~$` `exit`

0. Stop the test server by pressing **Ctrl** and **C**

0. You should have a single window open (no split screen).

0. Great! How about we try a new script that lets us make attachments. Create a text file.

    `student@bchd:~/mycode/email/$` `vim ~/mycode/email/assigned_spaces.txt`

0. Create the following text file.

    ```
    Dunder Mifflin Parking Space Assignments
    Michael 01
    Angela  02
    Jim     03
    Dwight  04
    Pam     05
    Oscar   06
    Toby    07
    ```

0. Save and exit with `:wq`

0. Now create a script that can make attachments. *Note: MIME references a protocol extension to SMTP (email) that defines how to make attachments of different file types.*

    `student@bchd:~/mycode/email/$` `vim ~/mycode/email/email02.py`

0. Create the following script.

    ```python
    #!/usr/bin/python
    """Alta3 Research | RZFeeser@alta3.com
       Using Python to use SMTP (email) with an attachment to send an message to a local
       test server.

       To run the SMTP server, run

       python3 -m smtpd -c DebuggingServer -n localhost:1025

       Use CTRL + C to stop the server."""

    # standard library imports
    import smtplib
    from os.path import basename

    """Note:
       Multipurpose Internet Mail Extensions (MIME) is a standard that extends SMTP (email)
       to support sending things other than ASCII (text)"""
    # standard library imports
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication

    def main():
        """runtime code"""
        
        # SMTP routing information
        sender = 'dwight@example.com'
        receiver = 'jim@example.com'
        # declare our message will have non-ASCII attachments
        msg = MIMEMultipart()

        msg['Subject'] = 'Assigned parking spaces'
        msg['From'] = 'dwight@example.com'
        msg['To'] = 'jim@example.com'

        # this will be our attachement
        filename = 'assigned_spaces.txt'
        # open the file "assigned_spaces.txt"
        with open(filename, 'r') as f:
            part = MIMEApplication(f.read(), Name=basename(filename))

        # adds a header that describes our email as having "more than" just ASCII txt
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))

        # takes our routing information & applies our attachment
        msg.attach(part)

        # we want some plain text in the body.
        msg.attach(MIMEText("Attached is a document with the assigned parking spots."))

        # not necessary, only would be used with an enterprise server (such as gmail or outlook)
        #user = 'username'
        #password = 'password'

        with smtplib.SMTP("localhost", 1025) as server:

            #server.login(user, password) # only necessary if we were using a production / enterprise server
            server.sendmail(sender, receiver, msg.as_string())
        
        print("Successfully sent email")
    
    if __name__ == "__main__":
        main()
    ```

0. Save and exit with `:wq`

0. *Before* you run your script, start the test server.

    `student@bchd:~/mycode/email/$` `python3 -m smtpd -c DebuggingServer -n localhost:1025`

0. Great. Now split the screen horizontally. You can do this with tmux. Press **Ctrl** and **b**, then press **Shift** and **"**. The screen should split.

0. Run your script!

    `student@bchd:~$` `python3 ~/mycode/email/email02.py`
    
0. The test Python server should indicate that the message was received.

0. Close the new window by typing `exit`.

    `student@bchd:~$` `exit`

0. Stop the test server by pressing **Ctrl** and **C**

0. You should have a single window open (no split screen).

0. That's it for this lab. If you're tracking your code in a SCM platform, issue the following commands:

    - `cd ~/mycode`
    - `git add *`
    - `git commit -m "automating email"`
    - `git push origin`

<br><br><div align="center">


![Alta3 Logo](https://static.alta3.com/images/Alta3-logo_large.png)

</div>
