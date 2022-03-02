# Paramiko Warmup

1. To ensure that you're all set up with the remote hosts you'll need, run the following command!

    `student@bchd~:` `cd && wget https://labs.alta3.com/projects/napya/deploy/napyasetup.sh -qO setup.sh && bash setup.sh`
        
0. Below is a script that we were looking at yesterday. Make a new copy of it!

    `student@bchd~:` `vim paramikowarmup.py`
        
    ```python
    #!/usr/bin/python3
    """Alta3 Research | rzfeeser@alta3.com
       Learning about Python SSH"""

    import paramiko

    def main():
        """Our runtime code that calls other functions"""
        # describe the connection data
        credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"}, {"un": "fry", "ip": "10.10.2.4"}]

        # harvest private key for all 3 servers
        mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

        # loop across the collection credz
        for cred in credz:
            ## create a session object
            sshsession = paramiko.SSHClient()

            ## add host key policy
            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ## display our connections
            print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

            ## make a connection
            sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

            ## touch the file goodnews.everyone in each user's home directory
            sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

            ## list the contents of each home directory
            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

            ## display output
            print(sessout.read().decode('utf-8'))

            ## close/cleanup SSH connection
            sshsession.close()

        print("Thanks for looping with Alta3!")

    main()
    ```
    
0. **CUSTOMIZATION REQUEST 01 -** Read the connection information into your script from an external file (username and IPs).

0. **CUSTOMIZATION REQUEST 02 -** Make the output returned by the ls command written out to a file results.log. Be sure to provide some kind of explanation as to the host that the results were returned from.
