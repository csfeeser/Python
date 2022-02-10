# Adding Modules via Collections

<img src="https://www.ansible.com/hs-fs/hubfs/Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png?width=1310&name=Screen%20Shot%202020-12-16%20at%204.04.32%20PM.png" alt="drawing" width="500"/>


Go visit https://github.com/rzfeeser/ansible-custom-modules-nasa-api/tree/master/library, a GitHub repository written by one of our instructors at Alta3. There you will find several Python files that can be used as Ansible modules!

1. Be sure you have the following directory and move into it:

    `student@bchd:~$` `mkdir -p ~/mycode/collections/ && cd ~/mycode/collections`

0. Yesterday we learned how to create a collection using the `ansible-galaxy` command. Create a new collection; replace `NAMESPACE` and `COLLECTION_NAME` with whatever you prefer!

    `student@bchd/mycode/collections:~$` `ansible-galaxy collection init NAMESPACE.COLLECTION_NAME`
    
    > if it were me, I'd use `csfeeser.nasaapis` or something similar

0. Next, `cd` into the name of the directory you just created.

    `student@bchd/mycode/collections:~$` `cd NAMESPACE/COLLECTION_NAME`

0. You'll need to create a `modules` directory inside of your `plugins` directory. Do that now and `cd` into that directory.

    `student@bchd/mycode/collections/NAMESPACE/COLLECTION_NAME:~$` `mkdir plugins/modules && cd plugins/modules`

OK! The rest of this challenge is now up to you. Attempt the following:

- Fill the `modules` directory with as many python files from the GitHub page we opened at the start of this lab as you like.
- Use the steps we learned in **Lab 28. Ansible Collections** to build and install this collection.
- Create a playbook that uses at least one of the modules you downloaded. Remember, the documentation on how to use a module is always included INSIDE the **.py** file itself!

If you get stuck or lost, let Chad know!
