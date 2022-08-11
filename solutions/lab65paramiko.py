"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

def movethemfiles(sftp, localdest, remotedest):
    try:
        ## iterate across the files within directory
        for x in os.listdir(localdest): # iterate on directory contents
          if not os.path.isdir(localdest+x): # filter everything that is NOT a directory
            sftp.put(localdest+x, remotedest+x)
                      # local path                    # remote path
    except FileNotFoundError:
        print("Remote path does not exist!")

    except:
        print("Something went wrong!")


def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username="bender", password="alta3")

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    remotedest= input("Where on the remote host will you place these files?\n>")
    localdest= input("Where on localhost do you want to source files?\n>")

    movethemfiles(sftp, localdest, remotedest)

    ## close the connections
    sftp.close() # close the connection
    t.close()
    print("All done!")
# Collect additional input from the user to determine where on the target host the files should be placed

if __name__ == "__main__":
    main()
