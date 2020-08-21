# Introduction to Asyncronous Programming with AsycnIO

## Procedure

0. Before we begin we must upgrade our version of Python to match AsyncIO requirements. Please use the following steps:

    `student@bchd:~$` `sudo apt update -y`
    
    `student@bchd:~$` `sudo apt install python3.7`

    `student@bchd:~$` `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1`
    
    `student@bchd:~$` `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2`

    `student@bchd:~$` `sudo update-alternatives --config python3`

0. In the output window that rises from the previous command, Press `2`.

    ```
      Selection    Path                Priority   Status
    ------------------------------------------------------------
    * 0            /usr/bin/python3.6   2         auto mode
      1            /usr/bin/python3.6   1         manual mode
      2            /usr/bin/python3.7   2         manual mode

    Press <enter> to keep the current choice[*], or type selection number:
    ```
    
0. Check your Python version to confirm that we are good to go.

    `student@bchd:~$` `python3 --version`
    
    ```
    Python 3.7.9
    ```
    
0. Async is rather new to Python, and it has been improving much in the last few years and minor versions. So let's make sure that we have the newest version of Python available to us. We are looking to get Python3.8 right now. Additionally, we want to create a virtual environment for us to play around in. In order to help facilitate this, let's create the following bash script.

    `student@bchd:~$` `vim gimme_new_python.sh`
    
    ```bash
    sudo apt update
    sudo apt install -y software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa -y
    sudo apt update

    sudo apt install -y python3.8 python3.8-venv build-essential python3.8-dev
    python3.8 -m venv venv
    source venv/bin/activate
    python3 -m pip install wheel
    ```
    
0. Now run that bash script to get Python3.8 set up for you.

    `student@bchd:~$` `bash gimme_new_python.sh`

0. Next, we want to start using the virtual environment we just created. To do so, simply run the following `source` command:

    `student@bchd:~$` `source venv/bin/activate`
    
0. The first concept that needs to be thoroughly understood with async programming is the [**event loop**](https://docs.python.org/3/library/asyncio-eventloop.html). This is the heart and soul of every asyncio app. Event loops:
    - run asynchronous tasks and callbacks
    - perform network IO operations
    - run subprocesses
    
    When an async process starts, it kicks off an event loop. Let's see it in action here:
    
    `(venv) student@bchd:~$` `vim learning_event_loops.py`
 
    ```python
    #!/usr/bin/env python3

    """
    This program exemplifies how to:

    - Connect to the event loop
    - Schedule a function to run in the event loop
    - Run the event loop
    """

    import asyncio
    from datetime import datetime as dt
    import time

    def sundial():
        """
        This function sleeps for 1 second,
        then prints out the current time.
        
        Notice that this is a task that "blocks" 
        execution of other code
        """
        
        time.sleep(1)
        print(f"Sundial: {dt.now()}")

    loop = asyncio.get_event_loop() # Connect to the event loop
    loop.call_soon(sundial) # Schedule a function to run in the event loop
    loop.call_soon(sundial) # Schedule another function to run in the event loop
    loop.run_until_complete(asyncio.sleep(1)) # Run the event loop and sleep for 1 second
    ```
    
    > `asyncio.get_event_loop()` https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop
    
    > `loop.call_soon()` https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon
    
    > `loop.run_until_complete()` https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete
    
    > `asyncio.sleep()` https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep
    
0. Run your script!

    `(venv) student@bchd:~$` `python3 learning_event_loops.py`

0. Next, let's look at the `asyncio.sleep()` functionality, and how we could use it in our code.

    `(venv) student@bchd:~$` `vim learn_async_sleep.py`
    
    ```python
    #!/usr/bin/env python3

    import asyncio
    from datetime import datetime as dt
    import time

    async def rolex():
        await asyncio.sleep(1)
        print(f"Rolex: {dt.now()}")

    async def main():
        # Fancy looking, but still slow
        print("Job 1:")
        await rolex()
        print("Job 2:")
        await rolex()
        
    if __name__ == "__main__":
        asyncio.run(main()) 
    ```

0. Run your script!

    `(venv) student@bchd:~$` `python3 learn_async_sleep.py`
    
    > **async** - Goes before `def` to indicate that it is an asynchronous function.  https://docs.python.org/3/reference/compound_stmts.html#async-def "Functions defined with async def syntax are always coroutine functions, even if they do not contain await or async keywords."
    
    > **await** - "Asynchronously Wait". This means that other code may be executed at the same time in the background. *HOWEVER*, this script shows us that if you simply *await* two async functions, one after another, they still will execute in a serial fashion.
    
    
    OUTPUT = 
    
    ```
    Job 1:
    Rolex: 2020-08-14 21:43:10.079975
    Job 2:
    Rolex: 2020-08-14 21:43:11.081427
    ```

0. Okay, that still took just as long. How do we overcome this? With Tasks!

    `(venv) student@bchd:~$` `vim learning_tasks.py`
    
    ```python
    #!/usr/bin/env python3

    import asyncio
    from datetime import datetime as dt
    import time

    async def swiss():
        await asyncio.sleep(1)
        print(f"Swiss: {dt.now()}")

    async def main():
        # Most preferred way to write async code
        task3 = asyncio.create_task(swiss())
        task4 = asyncio.create_task(swiss())
        await asyncio.gather(task3, task4)


    if __name__ == "__main__":
        asyncio.run(main())
    ```

0. Run your script!

    `(venv) student@bchd:~$` `python3 learning_tasks.py`

0. Your output should resemble the following.

    ```
    Swiss: 2020-08-21 13:30:51.636129
    Swiss: 2020-08-21 13:30:51.636901
    ```
    
    > **task** - https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "Event loops use cooperative scheduling: an event loop runs one Task at a time. While a Task awaits for the completion of a Future, the event loop runs other Tasks, callbacks, or performs IO operations."
    
    > **coroutine** - https://docs.python.org/3/glossary.html#term-coroutine "Coroutines are a more generalized form of subroutines. Subroutines are entered at one point and exited at another point. Coroutines can be entered, exited, and resumed at many different points."


0. This is for **ADVANCED USE CASES**. Specifically, when you have some type of blocking code that you have no control over (such as deep within a different module). To use your blocking, non-async code in an async manner, do something like this: 

    `(venv) student@bchd:~$` `vim advanced_event_loop.py`

    ```python
    import asyncio
    from datetime import datetime as dt
    import time

    def sundial():
        """
        This function sleeps for 1 second,
        then prints out the current time.

        Notice that this is a task that "blocks" 
        execution of other code
        """

        time.sleep(1)
        print(f"Sundial: {dt.now()}")

    # For advanced use cases when you can't turn your blocking 
    # code into async code
    async def main():
        loop = asyncio.get_event_loop()
        task1 = loop.run_in_executor(None, sundial)
        task2 = loop.run_in_executor(None, sundial)
        tasks = [await task for task in [task1, task2]]


    if __name__ == "__main__":
        asyncio.run(main())
    ```

0. Run your script!

    `(venv) student@bchd:~$` `python3 advanced_event_loop.py`
    
    > `asyncio.get_event_loop()` - https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop Gets or creates an event loop
    
    > `loop.run_in_executor()` - https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor Schedules the **sundial** function to be executed inside of a certain executor. This is typically hidden inside of a task (as we did earlier), however, this gives the programmer direct access to the loop and to declare where this function should be scheduled to run.
    
    > By using a list comprehension, we are able to have the tasks all be awaited on. Although this is not necessary, it is a handy trick.
 

    OUTPUT =
    
    ```
    Sundial: 2020-08-14 21:54:00.169623
    Sundial: 2020-08-14 21:54:00.169996
    ```
    
