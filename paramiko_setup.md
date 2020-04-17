# Setting up your machine for Paramiko!

0. ssh into each machine

    `student@napya-000-bchd:~$` `ssh bender@10.10.2.3`

0. When prompted, the password is `alta3`

0. Change the ownership of the `authorized_keys` file.

    `bender@bender:~$`  `sudo chown bender:bender .ssh/authorized_keys`
    
0. If you check, the ownership of the `authorized_keys` file should be bender and bender.

    `bender@bender:~$`  `ll .ssh/`

0. Type `exit` to get out of the bender container.

    `bender@bender:~$`  `exit`

0. Change directory into /home/student/.ssh.

    `student@napya-000-bchd:~$` `cd ~/.ssh`
    
0. Copy your machine's public RSA key to the bender container.

    `student@napya-000-bchd:~/.ssh$` `ssh-copy-id bender@10.10.2.3`

0. You should now be able to ssh into bender without being prompted for a password!

    `student@napya-000-bchd:~/.ssh$` `ssh bender@10.10.2.3`
    
0. Type `exit` to get out of this container.

    `bender@bender:~$`  `exit`
    
0. Repeat these steps for `fry@10.10.2.4` and `zoidberg@10.10.2.5`! Let Chad know if you need any help!
