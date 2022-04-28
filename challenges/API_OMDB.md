## Movie API Slicing!

<img src="https://www.codeitbro.com/wp-content/uploads/2020/07/python-meme-2-first-python-program.jpg" alt="drawing" width="300"/>

Let's take a look at the Open Movie Database API! This massive data source pretty much every movie title you could name... but also every TV show and video game!

What is different about this API is that the information we return from it must be passed in via a **query parameter.** What's that?

<img src="https://nullbeans.com/wp-content/uploads/2020/05/urldescription-1.png" alt="drawing" width="500"/>

Query parameters allow us to control what info we get back from the API. For instance, adding this to the end of our API URL:

```
?s=matrix
```

Means that the only movies that include the string (`s`) "matrix" will be returned! Open this link in your browser to see what is returned by that! 

http://www.omdbapi.com/?apikey=875c4c78&s=matrix

Below is some starter code. Copy it into your environment and give it a test run.

```python
#!/usr/bin/env python3

URL= "http://www.omdbapi.com/?apikey=875c4c78&s="

def main():
    choice= input("Enter a movie title:\n>")
    
    full_url= URL + choice
    
    movies= requests.get(full_url).json
  
    print(movies)
    print(full_url)
    
if __name__ == "__main__":
    main()
```

### OBJECTIVE 1:
- Use a **for loop** to print out the title of the movie.

**EXAMPLE**
```
The Matrix
The Matrix Reloaded
The Matrix Revolutions
The Matrix Resurrections
```

### OBJECTIVE 2:
- Add to your **for loop**: have it also print out the year the movie was released.

**EXAMPLE**
```
The Matrix was released in 1999
The Matrix Reloaded was released in 2003
The Matrix Revolutions was released in 2003
The Matrix Resurrections was released in 2021
```

### OBJECTIVE 3:
- Add a condition to your **for loop**: ONLY print out movies, not TV shows or games.

### Chad, I'm feeling extra sassy this morning.
- Excellent! Download the movie poster from only the FIRST result you get back :)
