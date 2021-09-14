#!/usr/bin/env python3
## Moving files with SFTP

import getpass
import os

import paramiko

def movethemfiles(conn, remote_dir):
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        conn.put("/home/student/filestocopy/"+x, remote_dir+x) # move file to target location

def main():
    while True:
        try:
            ip= input("IP Address:\n>")
            user= input("User name:\n>")
            remote_dir= input("Remote host target directory:\n>")

            t = paramiko.Transport(ip, 22) ## IP and port
            t.connect(username=user, password=getpass.getpass())
            sftp = paramiko.SFTPClient.from_transport(t)
            
            sftp.stat(remote_dir)

            movethemfiles(sftp, remote_dir)
            sftp.close()

        except:
            print("This is a generic exception.")

        finally:
            choice= input("Type q to quit, or press ENTER to choose a different host:\n>")
            if choice.strip().lower() == "q":
                break

main()
