# Python Virtual Environments

### Objective

The objective of this lab is to become more familiar with setting up and using a virtual environment for Python.

Using a virtual environment is beneficial for several reasons. First, it will allow you to specify which version of Python you wish to use if you have multiple versions installed. Second, it will provide a dedicated context for pip to install packages into. This is the primary reason why programmers would use virtual environments. This frees us up to specifically install a third party package at whatever necessary version we need for this project/script that, due to version skew, could potentially cause our other scripts to fail.

### Procedure

0. Install python3-venv

    `student@pyb-000-bchd:~$` `sudo apt-get install python3-venv -y`

0. Before going too far ahead, let's get rid of a package that was already downloaded for us using pip. The requests package is very useful, and we probably will want it back, but for now, lets remove it.

     `student@pyb-000-bchd:~$` `sudo pip3 uninstall requests`

0. Let's not create a directory to be used for our virtual environment.

    `student@pyb-000-bchd:~$` `mkdir ~/my_venv`

0. Change directories into my_venv.

    `student@pyb-000-bchd:~/my_venv` `cd ~/my_venv`

0. Now we are going to run the command to create a virtual environment. **Note the Period (.) at the end of the command** This directs the venv to use the current directory as the name of our virtual environment.

    `student@pyb-000-bchd:~/my_venv` `python3 -m venv .`

0. Next, let's take a look at what the venv has done for us. List out the contents of the directory.

    `student@pyb-000-bchd:~/my_venv` `ls`

        bin  include  lib  lib64  pyvenv.cfg  share

0. Let's take a closer look at the config file.

    `student@pyb-000-bchd:~/my_venv` `cat pyvenv.cfg`

        home = /usr/bin
        include-system-site-packages = false
        version = 3.6.8

0. Alright, now in order to use this virtual environment that we just created, we have to **source** it.

    `student@pyb-000-bchd:~/my_venv` `source bin/activate`

0. You should notice that your prompt has changed. This is due to us sourcing the configuration of the virtual environment.

    `(my_venv) student@pyb-000-bchd:~/my_venv`

0. Next we will do a pip install, and create a small script to use that package.

    `(my_venv) student@pyb-000-bchd:~/my_venv` `pip3 install requests`

0. Perform the following command to see what version of requests is installed.

    `(my_venv) student@pyb-000-bchd:~/my_venv` `pip3 show requests`

0. Now, let's try using requests.

    `(my_venv) student@pyb-000-bchd:~/my_venv` `vim try_it.py`

        import requests
        r = requests.get('https://swapi.co/api/people/1/')
        print(r.json())

0. Go ahead and try running the script now.

    `(my_venv) student@pyb-000-bchd:~/my_venv` `python3 try_it.py`

    You should see a bunch of information about Luke Skywalker printing out now.

        {'name': 'Luke Skywalker', 'height': '172', 'mass': '77', 'hair_color': 'blond' ...

0. Now to get ourselves out of the virtual environment we created, all we have to do is type `deactivate`:

     `(my_venv) student@pyb-000-bchd:~/my_venv` `deactivate`

0. And now we are back to our regular prompt. Go ahead and try our script again.

    `student@pyb-000-bchd:~/my_venv` `python3 try_it.py`

        /usr/lib/python3/dist-packages/requests/__init__.py:80: RequestsDependencyWarning: urllib3 (1.25.6)...

    Notice the warning above. This means that we still have requests installed, but the version is different.


0. Do another `pip show` command to see what version of requests we are working with here.

    `(my_venv) student@pyb-000-bchd:~/my_venv` `pip3 show requests`
