# Argument Parsing

### Lab Objective

The objective of this lab is to learn additional ways to work accept input from users. Oftentimes passing arguments at the command line is far faster than prompting users for input when the program runs.

Back in the day, Python scripting would of accepted arguments with the `sys` module (system module). That changed with the introduction of `argparse` in Python v3.2. This new module was created specifically for accepting command line arguments. In addition to accepting arguments, it makes it easy to document and provide help to end users. The `argparse` module is documented here:

    - https://docs.python.org/3/library/argparse.html

### Procedure

0. Let's stay in the habit of organizing our work. Make `/home/student/mycode/cmdargs/` directory.

    `student@beachhead:~$` `mkdir ~/mycode/cmdargs/`

0. Move to the `/home/student/mycode/cmdargs/` directory.

    `student@beachhead:~$` `cd ~/mycode/cmdargs/`

0. Create a new script.

    `student@beachhead:~/mycode/cmdargs$` `vim pirate-args.py`

        #!/usr/bin/env python3
        import sys
        
        args = sys.argv
        print("Username: " + args[1])
        print("Password: " + args[2])
        print("IP Address: " + args[3])
        print("Gateway: " + args[4])
        print("Oh by the way, your script is named:", args[0])

0. Save and exit.

0. Save as `/home/student/mycode/cmdargs/pirate-args.py`.

0. Change permissions on your script to make it executable.

    `student@beachhead:~/mycode/cmdargs$` `chmod u+x pirate-args.py`

0. Run your script using the following command:

    `student@beachhead:~/mycode/cmdargs$` `python3 pirate-args.py blackbeard dabl00nz 10.2.3.55 10.2.3.1`

0. When the script runs it should print the arguments to the screen.

0. Run your script using the following command:

    `student@beachhead:~/mycode/cmdargs$` `python3 pirate-args.py redbeard peezez0f8ight`
    
    > Note: **THIS IS SUPPOSED TO FAIL** This command does not use the required number of positional arguments that this script expects. Using `sys.argv` is limited to _required positional arguments._ Move on to the next step to learn a better way to deal with command line arguments.

0. The second way is to use `argparse`. Where `sys.argv` is simply used to interact with a list of the command line arguments, `argparse` is a full featured command line parser which gives you back the data in a much easier to use fashion. If you're doing anything more complicated than a script that accepts a few required positional arguments you'll want to use a parser. Depending on your Python version, there are three available in the Python standard library (`getopt`, `optparse`, and `argparse`). In Alta3's opinion, argparse is by far the best.

0. Open vim, we'll write a new script.

0. Copy the following code block into vim:

        #!/usr/bin/env python3
        import argparse, socket
        from datetime import datetime
        
        def server(port):
            x = "Your choice was server and it will run on port " + str(port)
            return x
        
        def client(port):
            x = "Your choice was client and it will run on port " + str(port)
            return x
        
        if __name__ == '__main__':
            choices = {'client': client, 'server': server}
            parser = argparse.ArgumentParser(description='Send and receive UDP locally')
            parser.add_argument('role', choices=choices, help='which role to play')
            parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                                help='UDP port (default 1060)')
        args = parser.parse_args()
        function = choices[args.role]
        print(function(args.p))

0. Save as `/home/student/mycode/cmdargs/clisvr-args.py`

0. Change permissions on your script to make it executable.

    `student@beachhead:~/mycode/cmdargs$` `chmod u+x clisvr-args.py`

0. Run your script using the following command:

    `student@beachhead:~/mycode/cmdargs$` `python3 clisvr-args.py server`

0. Make sure your program works. If it doesn't, debug!

0. **CODE CUSTOMIZATION 01** - Add another argument `-t` where the default value is `UDP`. Don't pass this argument to your functions, but display to the user the protocol that will be used.

0. If you're tracking your code in GitHub, issue the following commands:
    - `cd ~/mycode`
    - `git add *`
    - `git commit -m "your commit message"`
    - `git push origin master`
