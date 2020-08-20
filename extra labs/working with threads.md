# Working with Threads

### Lab Objective

Threading in Python is used to run multiple threads (tasks, function calls) at the same time. Note that this does not mean that they are executed on different CPUs. Python threads will NOT make your program faster if it already uses 100 % CPU time. In that case, you probably want to look into parallel programming.

Python threads are used in cases where the execution of a task involves some waiting. One example would be interaction with a service hosted on another computer, such as a webserver. Threading allows Python to execute other code while waiting; this is easily simulated with the sleep function.

### Procedure

0. Clean up your terminal space.

0. Create a new space in which to work.

    `student@beachhead:~$` `mkdir -p ~/pyapi/sewing/`

0. Move into the directory.

    `student@beachhead:~$` `cd ~/pyapi/sewing/`
    
0. Create a new script.

    `student@beachhead:~/pyapi/sewing$` `vim silksuit.py`

0. Copy and paste the following into your script:

        #!/usr/bin/python3
        """A basic threading example | rzfeeser@alta3.com"""
        
        # Make a thread that simulates a NASA count down
        # waits a 1 seconds at the bottom of each loop

        ## Python standard library
        import threading
        
        ## py standard library
        import time

        def groundcontrol():
            for i in range(10, -1, -1):
                print(i)
                time.sleep(1)

        print("Orion you are primed for launch. Count down begins...")
        
        ## Create a thread object (target is the function to call)
        mythread = threading.Thread(target=groundcontrol)
        
        ## begin the thread
        mythread.start()

0. Save and exit.

0. Great! Run your script.

    `student@beachhead:~/pyapi/sewing$` `python3 silksuit.py`

0. It should work, but it is okay if the purpose of threading is still not clear. Let's write a new script. The purpose is about to become much more clear!

    `student@beachhead:~/pyapi/sewing$` `vim blacktie.py`

0. At the very bottom of your code, add a few print statements. They can be anything. If you're not feeling creative, copy the example below.

        #!/usr/bin/python3
        """A basic threading example | rzfeeser@alta3.com"""
        
        # Make a thread that simulates a NASA count down
        # Waits 1 second at the bottom of each loop

        ## Python standard library
        import threading
        
        ## py standard library
        import time

        def groundcontrol():
            for i in range(10, -1, -1):
                print(i)
                time.sleep(1)


        print("Orion, you are primed for launch. Count down begins...")
        
        ## Create a thread object (target is the function to call)
        mythread = threading.Thread(target=groundcontrol)
        
        ## begin the thread
        mythread.start()
        
        ## code AFTER we call the thread
        print("Uh oh. I forgot my wallet. Can we stop?")

0. Save and exit.

0. Great! Run your script.

    `student@beachhead:~/pyapi/sewing$` `python3 blacktie.py`
    
0. Consider what just happened. Your thread was called **before** your print statement. But your print statement ran **before** your thread finished. How very neat! If you need an analogy, think this way... until now, if you told Python to *"go do my laundry, and then wash the floor,"* Python would start the washing machine, stand there until the washing machine finished, move the clothes to the dryer, stand there until the dryer was finished, and THEN wash the floor. At first we may think, "how very wasteful!" But you might need to tweak that thinking too- instead, think how wonderfully simple that was! It is nice to teach Python to **multitask** but it introduces a new problem that telephony nerds have long understood- that problem is called **racing**. Racing is when a series of steps ends up out of order and it's really bad. For example, consider if we had told Python to multitask between doing your laundry and ironing your laundry. Ironing depends on having clean clothes come out of the dryer first... so best case scenario is Python throws an error, and worst case scenario is Python burns down your house. Let's see if we can mimic this kind of unpredictability.

    `student@beachhead:~/pyapi/sewing$` `vim cleanshirt.py`        

0. Copy and paste the following into your new script. Be sure to read through the comments.

        #/usr/bin/python3
        """A basic threading example | rzfeeser@alta3.com"""
        
        # Make a thread that simulates a NASA count down
        # Waits 1 second at the bottom of each loop

        ## Python standard library
        import threading
        
        ## py standard library
        import time

        def groundcontrol():
            for i in range(10, -1, -1):
                print(i)
                time.sleep(1)

        print("Orion, you are primed for launch. Count down begins...")
        
        ## Create a thread object (target is the function to call)
        mythread = threading.Thread(target=groundcontrol)
        
        ## begin the thread
        mythread.start()
        
        ## Ask the user to press any key to exit.
        input("Press Enter to exit.")
        exit()

0. Save and exit.

0. Run your code. Be sure to press `Enter` before you NASA countdown finishes. You'll learn a few things. The first is that your script fails to exit until all threads have finished executing. This is also a basic racing condition as we certainly did not intend to tell the user they can press `Enter` to exit before they can actually exit!

    `student@beachhead:~/pyapi/sewing$` `python3 cleanshirt.py`        

0. We can fix our racing conditions by placing the `.join()` method on our thread. This method tells Python to 'wait' until the thread finishes before moving on. Create a new script.

    `student@beachhead:~/pyapi/sewing$` `vim newshoes.py`        

0. Copy and paste the code below into your new script.

        #!/usr/bin/python3
        """A basic threading example | rzfeeser@alta3.com"""
        
        # Make a thread that simulates a NASA count down
        # Wait 1 second at the bottom of each loop

        ## Python standard library
        import threading
        
        ## py standard library
        import time

        def groundcontrol():
            for i in range(10, -1, -1):
                print(i)
                time.sleep(1)

        print("Orion, you are primed for launch. Count down begins...")
        
        ## Create a thread object (target is the function to call)
        mythread = threading.Thread(target=groundcontrol)
        
        ## begin the thread
        mythread.start()
        
        print("Oh no, I forgot socks!")
        
        # Wait until the threads finish before moving on.
        mythread.join()
        
        ## Ask the user to press any key to exit.
        input("Press Enter to exit.")
        exit()

0. Save and exit.

0. Run your code. This time, you won't be prompted to press `Enter` until our NASA countdown finishes. That's because the `.join` method prevents our code from moving any further until the script finishes.

    `student@beachhead:~/pyapi/sewing$` `python3 newshoes.py`

0. We can also have multiple threads at once and let them execute simultaneously. Let's give that a try too. Create another script.

    `student@beachhead:~/pyapi/sewing$` `vim topcoat.py`

0. To understand the next script, let's deep dive into `import threading`. We use the `thread` library to create an object of Thread class. The Thread class requires the following arguments:
    - `target` - The function to be executed by thread
    - `args` - The arguments to be passed to the target function

0. Copy and paste the following code into your script. Notice that we tweaked the first function to require an argument and added a second function. Now that we have function that requires an argument we'll need to define the `args` parameter. 

        #!/usr/bin/python3
        """A basic threading example | rzfeeser@alta3.com"""
        
        # Make a thread that simulates a NASA count down
        # Wait 1 second at the bottom of each loop

        ## Python standard library
        import threading
        
        ## py standard library
        import time

        def groundcontrol(x):
            for i in range(x, -1, -1):
                print(i)
                time.sleep(1)

        def orion():
            print("I forgot my socks.")
            time.sleep(1)
            print("Can we stop this ride?")
            time.sleep(2)
            print("No? Alright. Ugh. I forgot to close the garage too.")
            time.sleep(1)
            print("To infinity, and beyond!")
            
        print("Orion, you are primed for launch. Count down begins...")
        
        countdown = 10
        
        ## Create a thread object (target is the function to call)
        mythread = threading.Thread(target=groundcontrol, args=(countdown, ))
        
        astrothread = threading.Thread(target=orion)
        
        ## begin the threads
        mythread.start()
        astrothread.start()
                
        # Wait until the threads finish before moving on.
        mythread.join()
        astrothread.join()
        
        ## Ask the user to press any key to exit.
        input("Press Enter to exit.")
        exit()

0. Save and exit.

0. Run the script. In this simple example we see a kind of 'dueling banjos' back-and-forth between `mythread` and `astrothread`. In a more practical sense, we might use threading to perform multiple database queries before we crunch some numbers. 

    `student@beachhead:~/pyapi/sewing$` `python3 topcoat.py`

0. In another script we can shed a bit more light on how threads work.


    `student@beachhead:~/pyapi/sewing$` `vim tophat.py`

0. When we create a thread object we can apply a name to that thread object with the `name` parameter. By using that technique, we can print the thread name and corresponding process for each task:

        #!/usr/bin/python3
        """ Naming threads and pids || rzfeeser@alta3.com
        Helpful notes:
          - os.getpid() function will return ID of current process
          - threading.main_thread() returns the main thread object.
            Typically the main thread is the thread from which Python was
            started.
          - threading.current_thread() returns the current thread object.
        """        
        
        
        import threading 
        import os 
          
        def task1():
            print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
            print("ID of process running task 1: {}".format(os.getpid())) 
        
        
        def task2(): 
            print("Task 2 assigned to thread: {}".format(threading.current_thread().name))            
            print("ID of process running task 2: {}".format(os.getpid())) 
        
        def main():
            # print ID of current process 
            print("ID of process running main program: {}".format(os.getpid())) 
          
            # print name of main thread 
            print("Main thread name: {}".format(threading.main_thread().name)) 
          
            # creating threads 
            t1 = threading.Thread(target=task1, name='t1') 
            t2 = threading.Thread(target=task2, name='t2')   
          
            # starting threads 
            t1.start() 
            t2.start() 
          
            # wait until all threads finish 
            t1.join() 
            t2.join() 
        
        if __name__ == "__main__": 
            main()

0. Save and exit.

0. Run your script.

    `student@beachhead:~/pyapi/sewing$` `python3 tophat.py`

0. The output should be something like the following:

            ID of process running main program: 11758
            Main thread name: MainThread
            Task 1 assigned to thread: t1
            ID of process running task 1: 11758
            Task 2 assigned to thread: t2
            ID of process running task 2: 11758
            
0. The output is proof that a single PID identifies our main process as well as our threads. Interesting!
            
0. That concludes an overview to multithreading in Python. Even if you don't need to use multithreading, it may help unravel the 'magic' behind an API framework, such as Flask.

0. If you're tracking your code, run the following commands:
    - `cd ~/pyapi`
    - `git add *`
    - `git commit -m "Intro to threading"`
    - `git push origin master`
