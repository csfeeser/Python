# The Multiprocessing Module

### Objective

Multiprocessing allows us to spawn more than one process at the same time. This means that we can have multiple processes working for us that do not have to go one, then the next, then the next. With multiprocessing, we can spread the work out to separate processes to be more efficient.

### Procedure


0. First of all, let's start by creating a basic function that will allow us to square any number that gets passed to it.

    `student@pyb-000-bchd:~/mycode` `vim multi-square.py`

        def squarer(number):
            """
            A squaring function that can be used by a process
            """
            result = number ** 2
            print('{} squared to {}'.format(number, result))

0. Under that, let's go ahead and call on this function, and let's have it go through a list of numbers.

        if __name__ == '__main__':
            numbers = [2, 3, 4, 5, 6]
            for number in numbers:
                squarer(number)

0. Alright, now let's try it out to make sure we have that working as expected.

    `student@pyb-000-bchd:~/mycode` `python3 multi-square.py`

        2 squared to 4
        3 squared to 9
        4 squared to 16
        5 squared to 25
        6 squared to 36

0. Excellent! Now, let's hop back in there and add in our multiprocessing. Add the following **TO THE TOP OF YOUR SCRIPT**.

    `student@pyb-000-bchd:~/mycode` `vim multi-square.py`

        from multiprocessing import Process, current_process

0. Next let's alter our **squarer** function to include the **current_process** name and print that out along with the squared result.

        def squarer(number):
            """
            A squaring function that can be used by a process
            """
            result = number ** 2
            proc_name = current_process().name
            print('{0} squared to {1} by: {2}'.format(
                number, result, proc_name))

0. Now under the main code section, we need to do a good bit of work to have this script use multiprocessing. First, let's add in a blank list of processes.

        if __name__ == '__main__':
            numbers = [2, 3, 4, 5, 6]
            procs = []

0. Now, under our **for** loop, instead of just calling on the squarer() function, let's spawn a **Process** that targets the squarer() function. Also, let's append that Process to our **procs** list, and start that process with a **proc.start()**.

            for number in numbers:
                proc = Process(target=squarer, args=(number,))
                procs.append(proc)
                proc.start()

0. And finally, we will need to **.join()** each of these processes with another for loop. This will keep the whole process running until each of these are done.

            for proc in procs:
                proc.join()

0. This is what your final code should look like.


        from multiprocessing import Process, current_process


        def squarer(number):
            """
            A squaring function that can be used by a process
            """
            result = number ** 2
            proc_name = current_process().name
            print('{0} squared to {1} by: {2}'.format(
                number, result, proc_name))


        if __name__ == '__main__':
            numbers = [2, 3, 4, 5, 6]
            procs = []

            for number in numbers:
                proc = Process(target=squarer, args=(number,))
                procs.append(proc)
                proc.start()

            for proc in procs:
                proc.join()


0. Now, let's run our **squarer** code.

    `student@pyb-000-bchd:~/mycode` `python3 multi-square.py`

        3 squared to 9 by: Process-2
        2 squared to 4 by: Process-1
        4 squared to 16 by: Process-3
        5 squared to 25 by: Process-4
        6 squared to 36 by: Process-5
