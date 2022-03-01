#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

import paramiko
import os
# the getpass library will prompt for passwords
# without displaying your answer on screen
import getpass


def movethemfiles(conn, dest):
    try:
        for x in os.listdir("/home/student/filestocopy/"): 
          if not os.path.isdir("/home/student/filestocopy/"+x): 
            conn.put("/home/student/filestocopy/"+x, dest+x)
        return True
    except Exception as err:
        print("There was an error copying your files:", err)
        return False
        

def main():

    while True:
        un= input("Enter the username of the host:\n>")
        pw= getpass.getpass()
        ip= input("Enter the IP address of the host:\n>")
        dest= input(f"Where on {un}@{ip} should these files be placed?:\n>")

        t = paramiko.Transport(ip, 22)

        t.connect(username=un, password=pw)

        sftp = paramiko.SFTPClient.from_transport(t)

        movethemfiles(sftp, dest)

        sftp.close()
        t.close()

        again= input("Press ENTER to specify another host, or type 'q' to quit.\n")
        
        if again:
            break

if __name__ == "__main__":
    main()
