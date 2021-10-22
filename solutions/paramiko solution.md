The question was asked how one might write a script that does the following:

1. Have a list of servers
2. SSH to each server
3. `cd` to a directory
4. Execute a command to find out a software version
5. Transfer result to Excel in two columns: `ServerName` and `Software-version`

For a list of servers, an easy to change/update document would be YAML, like so:

`servers.yaml`
```YAML
- un: bender
  ip: 10.10.2.3
- un: fry
  ip: 10.10.2.4
- un: zoidberg
  ip: 10.10.2.5
```

You could then read in this list of servers and use a combination of the Paramiko, PYYAML, and Pyexcel modules to achieve the rest of the goals listed above.

```python
#!/usr/bin/env python3
"""Find software version and write to .xls file"""

import paramiko
import pyexcel
import yaml

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    with open("servers.yml", "r") as myf:
        credz = yaml.load(myf)

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

    mylistdict = []

    # loop across the list credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("python3 --version")

        ## display output
        ver= sessout.read().decode('utf-8')
 
        # print output for debug purposes
        print(ver)

        # create a dictionary with two static keys, assign new values
        d = {"ServerName": cred.get("un"), "Software-version": ver}
        
        # add new dictionary to mylistdict list
        mylistdict.append(d)
        
        ## close/cleanup SSH connection
        sshsession.close()

    # use pyexcel to convert the list of dictionaries into a spreadsheet with two columns
    pyexcel.save_as(records=mylistdict, dest_file_name=f'/home/student/static/pythonversions.xls')
    
    print("Thanks for looping with Alta3!")

main()
