# Week Three Warmup

Let's install a goofy little application called `sl`. You'll see what it does in a moment!

1. First, uninstall/reinstall your `planetexpress` machines (bender, fry, zoidberg, and farnsworth) with the following command.

    `student@bchd:~$` `cd && wget https://labs.alta3.com/projects/napya/deploy/napyasetup.sh -qO setup.sh && bash setup.sh`
    
0. Use the following command to confirm that the `sl` application is installed on `bchd`.

    `student@bchd:~$` `test -f /usr/games/sl && echo "FILE exists" || echo "File does not exist"`
    
    ```
    File does not exist
    ```
    
0. Now install `sl`. Be sure to use `sudo` or you won't have permission to install it!

    `student@bchd:~$` `sudo apt install sl`
    
0. Use that command again to confirm that the `sl` application is installed on `bchd`.

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

Let's pretend that the `sl` application is one of several legitimate services we need to provision on a network of machines and/or VMs. Write a script (***you are seriously encouraged to steal code from Lab 66***) that does the following:

- runs against `bender`,`fry`, AND `zoidberg`
- installs the `sl` application
- confirms that `sl` has been installed.
- **BONUS:** if `sl` has already been installed on a host, SKIP installation (why install it again?). Inform the user that this host was SKIPPED.
- **BONUS 2:** make it easy to switch this program back and forth between installing and *uninstalling* `sl`.
- **ROCKET SCIENTISTS LOOKING FOR A HEADACHE:** use the *threading* module to allow installation to all three devices [concurrently](https://www.dictionary.com/browse/concurrently) instead of [consecutively](https://www.dictionary.com/browse/consecutively).
- **FINALLY:** ask yourself this question... *do you wish that this whole process was a lot easier?*
