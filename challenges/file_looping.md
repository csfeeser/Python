## Spooky Loopin' Exercise

<img src="https://cdn.onebauer.media/one/empire-tmdb/films/12110/images/y7N276seR43H31xvDbWMWxEsDr.jpg?format=jpg&quality=80&width=960&height=540&ratio=16-9&resize=aspectfill" alt="drawing" width="300"/>

> HOMEWORK FOR THE WEEKEND: go watch this movie!



Run the following command to download the book *Dracula* by Bram Stoker. Yes, the whole thing!

`student@bchd:~$` `wget https://www.gutenberg.org/files/345/345-0.txt`

Write a script that does the following:

#### Part 1

- Read in the content of the *Dracula* novel as a file object.

<details>
<summary>Help!</summary>
<pre>
with open("345-0.txt","r") as foo:
</pre>
OR
<pre>
foo= open("345-0.txt","r")
foo.close()
</pre>
</details>


#### Part 2

- Loop over every line in *Dracula,* print each line out!

<details>
<summary>Help!</summary>
<pre>
for line in foo:
    print(line)
</pre>
</details>

#### Part 3

- Actually, fix that for loop... only print out the line if it has the word `vampire` in it!

<details>
<summary>Help!</summary>
<pre>
for line in foo:
    if "vampire" in line:
        print(line)
</pre>
</details>


#### Part 4

- If you didn't already, make sure it prints the line no matter what case `vampire` is!

<details>
<summary>Help!</summary>
<pre>
for line in foo:
    if "vampire" in line.lower():
        print(line)
</pre>
</details>

#### Part 5

- Count that up! How many times does the word `vampire` appear?

<details>
<summary>How many times does it appear?</summary>
<pre>
32
</pre>
</details>

<details>
<summary>Help!</summary>
<pre>
count= 0
for line in foo:
    if "vampire" in line.lower():
        count += 1
        
print(count)
</pre>
</details>

#### Part 6

- Take the lines from *Dracula* that have `vampire` in it and write them to a second file named `vampytimes.txt`.

<details>
<summary>Help!</summary>
YOU GOT THIS :)
</details>
