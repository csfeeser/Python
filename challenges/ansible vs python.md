# Week Three Warmup

<img src="https://pbs.twimg.com/media/DvxFrYPXcAAa_Ye.jpg" alt="drawing" width="300"/>


Let's install a goofy little application called `sl`. You'll see what it does in a moment!

1. First, uninstall/reinstall your `planetexpress` machines (bender, fry, zoidberg, and farnsworth) with the following command.

    `student@bchd:~$` `cd && wget https://labs.alta3.com/projects/napya/deploy/napyasetup.sh -qO setup.sh && bash setup.sh`
    
0. Use the following command to confirm that the `sl` application is not installed on `bchd`.

    `student@bchd:~$` `test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist"`
    
    ```
    File does not exist
    ```
    
0. Now install `sl`. Be sure to use `sudo` or you won't have permission to install it!

    `student@bchd:~$` `sudo apt install sl`
    
0. Use that command again to confirm that the `sl` application is now installed on `bchd`.

    `student@bchd:~$` `test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist"`
    
    ```
    FILE exists
    ```
    
0. Now run the `sl` application. I hope it brings a smile to your face!

    `student@bchd:~$` `/usr/games/sl`
    
    ```
    CHOO CHOO!
    ```
    
### CHALLENGE OBJECTIVE:

Let's pretend that the `sl` application is one of several legitimate services we need to provision on a network of machines and/or VMs. Edit one of our scripts from last week (***Parmiko Lab 66, included below***) that does the following:

- runs against `bender`,`fry`, AND `zoidberg`
- installs the `sl` application (`sshsession.exec_command(`sudo apt install sl`)`)
- waits a few seconds to allow the installation (`time.sleep(5`)
- confirms that `sl` has been installed. (`sessin, sessout, sesserr = sshsession.exec_command('test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist"')`)
- **BONUS:** if `sl` has already been installed on a host, SKIP installation (why install it again?). Inform the user that this host was SKIPPED.
- **BONUS 2:** make it easy to switch this program back and forth between installing and *uninstalling* `sl`.
- **ROCKET SCIENTISTS LOOKING FOR A HEADACHE:** use the *threading* module to allow installation to all three devices [concurrently](https://www.dictionary.com/browse/concurrently) instead of [consecutively](https://www.dictionary.com/browse/consecutively).
- **FINALLY:** ask yourself this question... *do you wish that this whole process was a lot easier?*

```python
#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Learning about Python SSH"""

import paramiko

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = [
             {"un": "bender", "ip": "10.10.2.3"}, 
             {"un": "zoidberg", "ip": "10.10.2.5"}, 
             {"un": "fry", "ip": "10.10.2.4"}
            ]

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
