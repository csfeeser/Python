#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

def directory_exists(UN, PW, IP, DEST):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(IP, username=UN, password=PW)
    client.invoke_shell()
    is_directory_exists = False
    cmd = 'ls -d ' + DEST
    stdin, stdout, stderr = client.exec_command(cmd)
    if not str(stderr.read()):
        is_directory_exists = True
    client.close()
    return is_directory_exists

def movethemfiles(sftp,DEST):
    for x in os.listdir("/home/student/filestocopy/"):
      if not os.path.isdir("/home/student/filestocopy/"+x):
        sftp.put("/home/student/filestocopy/"+x, DEST+x)

choice= ""

while choice != "q":
    UN= input("User? ")
    PW= input("Password? ")
    IP= input("IP? ")
    DEST= input("Save destination? ")

    if directory_exists(UN, PW, IP, DEST):
        try: # TRY to run the code indented under me!

            t = paramiko.Transport(IP, 22) ## IP and port
            t.connect(username=UN, password=PW)
            sftp = paramiko.SFTPClient.from_transport(t)

            movethemfiles(sftp,DEST)

            sftp.close() # close the connection

        except:
            print("An error has occurred!")
            try:
                sftp.close()
            except:
                pass

    else:
         print("That destination directory does not exist!")

    choice= input("Press ENTER to make another connection or type Q to quit.").lower()
