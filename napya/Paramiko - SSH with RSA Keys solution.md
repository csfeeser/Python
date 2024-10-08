  ## Solution

1. First let's put our data in a separate file as a JSON string.

    `student@bchd:~$` `vim credfile.json`

    ```json
    [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"},{"un": "fry", "ip": "10.10.2.4"}]
    ```

0. The following script has both solutions built into it. Read the comments to see where new code was added!

    `student@bchd:~$` `vim paramikosolution.py`

    ```python
    #!/usr/bin/python3

    import paramiko
    import json

    # the datetime module is handy for creating timestamps
    from datetime import datetime

    def main():
        with open("credfile.json","r") as credfile:
            # solution 1: the json.load() function will convert a JSON file
            # into a pythonic object
            credz= json.load(credfile)

        mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

        for cred in credz:
            sshsession = paramiko.SSHClient()

            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

            sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

            sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

            ## solution 2: open a file named "results.log"
            # make it "a" for appendable so more log entries can be added to it
            with open ("results.log","a") as log:
                # write the username into the log as a label
                # on the same line write out a timestamp with datetime
                print(cred.get("un"), datetime.now(), file= log)
                print(sessout.read().decode('utf-8'), file=log)


            ## close/cleanup SSH connection
            sshsession.close()

        print("Thanks for looping with Alta3!")

    main()
    ```
