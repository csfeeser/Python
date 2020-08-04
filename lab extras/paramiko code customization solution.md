## Lab 11 Paramiko Customization Request Solutions

#### CUSTOMIZATION REQUEST 01: Read the connection information into your script from an external file (username and IPs).

To use a csv reader solution, create a text file named `credz.txt` in your current directory containing the following:

```
bender,10.10.2.3
fry,10.10.2.4
zoidberg,10.10.2.5
```

#### CUSTOMIZATION REQUEST 02: Make the output returned by the ls command written out to a file results.log. Be sure to provide some kind of explanation as to the host that the results were returned from.

Inside your current directory (same directory as `credz.txt`) create this script:

```
#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

import warnings
import csv  # added this to import a "csv" file that has all my usernames and hostnames to satisfy task 1
import paramiko

warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():

    # opening the "csv" file I created
    f = open("credz.txt", "r")

    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    # all output will be written to results.log to complete task 2
    # setting "a" for append so I don't overwrite each entry.    
    parafile = open("results.log", "w")

# this is the same for loop from PYB Lab 26
    for x in csv.reader(f): # reads out the lines from the text file as lists

            sshsession = paramiko.SSHClient()

            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                      # I'm now referring to elements in a list instead of keys in a dictionary
            print("Connecting to... " + x[0] + "@" + x[1])

            sshsession.connect(hostname=x[1], username=x[0], pkey=mykey)

            sshsession.exec_command("touch /home/" + x[0] + "/goodnews.everyone")

            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + x[0])

            # this is just some window dressing to separate what output belongs to which machine
            print("==========" + x[0].upper() + "==========", file=parafile)

            # all that was added to this line was , file=parafile
            print(sessout.read().decode('utf-8'), file=parafile)

            sshsession.close()

    # close your file when done with it!
    parafile.close()
    print("Thanks for looping with Alta3!")

main()
```

Use `cat` on the `results.log` file that is created!
