# Queues And Pipes

### Objective

In this lab we are going to be working with two separate process. We want them to be friends and work together to accomplish the task that we have set out for them. This means that they need to be able to communicate somehow.

To start with, we will be using a **Queue**. This allows for multiple processes to be what they call _producers_ as well as _consumers_ at the same time.

Then we will move on to using a **Pipe**. A pipe works as a connection between two specific processes.

### Procedure

0. Let's now try working with a **Queue**. In this script we will create two separate functions that we want to work together. First, we will define a function that simply multiplies a number from a given list by 3. Next, we will define a function that prints a message with the elements in the queue before the other function starts, and after the queue is empty. First, let's import multiprocessing and define our tripler function.

    `student@pyb-000-bchd:~/mycode` `vim que_ball.py`

        from multiprocessing import Process, Queue

        def tripler(mylist, q):
            """
            function to triple items in a given list
            """
            # append triples of mylist to queue
            for num in mylist:
               q.put(num * 3)

0. Now, lets create our function to print out the queue elements.

        def print_queue(q):
            """
            function to print queue elements
            """
            print("Queue elements:")
            while not q.empty():
                print(q.get())
            print("Queue is now empty!")

0. Now, let's add in our main section, where we will be calling on the multiprocessing module to start these processes.

        if __name__ == "__main__":
            # input list
            mylist = [1,2,3,4]

            # creating multiprocessing Queue
            q = Queue()

            # creating new processes
            p1 = Process(target=tripler, args=(mylist, q))
            p2 = Process(target=print_queue, args=(q,))

            # running process p1 to square list
            p1.start()
            p1.join()

            # running process p2 to get queue elements
            p2.start()
            p2.join()

0. Now, let's try running our code, and see what happens.

    `student@pyb-000-bchd:~/mycode` `python3 que_ball.py`

        Queue elements:
        3
        6
        9
        12
        Queue is now empty!

    Notice how the print_queue function was able to print out what was placed into the **q** element with **q.put()**? Neat!

0. Okay, now it is time to move on to **Pipes**. Let's create a new script.

    `student@pyb-000-bchd:~/mycode` `vim pipe_dream.py`

    Add the following to the script.

        from multiprocessing import Process, Pipe

        def tripler(mylist, conn):
            for ind, item in enumerate(mylist):
                mylist[ind] = item * 3
            # sends or returns data through the pipe -as child_conn
            conn.send(mylist)
            # closes connection to pipe - so others may use it next
            conn.close()

        if __name__ == '__main__':
            # sets pipe ends
            parent_conn, child_conn = Pipe()
            nums = [3, 4, 5, 6]
            p = Process(target=tripler, args=(nums, child_conn,))
            p.start()
            # print what parent process received
            print(parent_conn.recv())   
            p.join()


0. Okay, now let's run it!

    `student@pyb-000-bchd:~/mycode` `python3 pipe_dream.py`    

        [9, 12, 15, 18]

    Awesome job!
