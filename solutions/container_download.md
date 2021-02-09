0. Move into the home directory.

    `student@beachhead:~$` `cd`

0. We will build a bash script that will download the images we need to build containers for our labs!

    `student@bchd:~$` `vim download.sh`

    ```
    #!/bin/bash

    wget https://static.alta3.com/projects/ansible/modules/ssh-bender.tar.gz -O ~/.config/dockerfiles/ansible/ssh-bender.tar.gz
    wget https://static.alta3.com/projects/ansible/modules/ssh-farnsworth.tar.gz -O ~/.config/dockerfiles/ansible/ssh-farnsworth.tar.gz
    wget https://static.alta3.com/projects/ansible/modules/ssh-fry.tar.gz -O ~/.config/dockerfiles/ansible/ssh-fry.tar.gz
    wget https://static.alta3.com/projects/ansible/modules/ssh-zoidberg.tar.gz -O ~/.config/dockerfiles/ansible/ssh-zoidberg.tar.gz
    ```

0. At the command line, execute your bash script.

    `student@bchd:~$` `bash download.sh`

0. Once complete, change directories.

    `student@bchd:~$` `cd ~/.config/dockerfiles/ansible`

0. We'll now need to unzip the tar files we just downloaded. Run each command once.

    `student@bchd:~/.config/dockerfiles/ansible$` `gunzip ssh-bender.tar.gz`

    `student@bchd:~/.config/dockerfiles/ansible$` `gunzip ssh-fry.tar.gz`

    `student@bchd:~/.config/dockerfiles/ansible$` `gunzip ssh-farnsworth.tar.gz`

    `student@bchd:~/.config/dockerfiles/ansible$` `gunzip ssh-zoidberg.tar.gz`
