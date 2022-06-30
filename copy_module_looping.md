#### Complete Labs 36 and 37

In these labs the `shutil.move()`, `shutil.copy()`, and `shutil.copytree` functions were used to automate the transferring and/or renaming of files and directories.

Choose one of the scripts from either lab and **upgrade it**. Instead of copying/moving a SINGLE file or directory, let it do MULTIPLE!

`student@bchd:~$` `mkdir ~/mycode/copyloops && cd ~/mycode/copyloops`

`student@bchd:~/mycode/copyloops$` `touch file1 file2 file3 file4 file5 && mkdir ~/mycode/copyloops/dontmoveme`

Your script should:
 - take input from a user for the files' SOURCE and for the files' DESTINATION
 - loop over all the files in the specified directory, but DON'T move the directories
 - copy the files to another location of your choosing.

### RECOMMENDED TOOLS:

[os.listdir](https://www.geeksforgeeks.org/python-os-listdir-method/)- returns a list of files/directories inside a directory.
[os.path.isdir](https://www.geeksforgeeks.org/python-os-path-isdir-method/)- returns **True/False** whether a specified path is a directory or not.

