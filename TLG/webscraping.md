# Web Scraping Data with Beautiful Soup

### Lab Objective

Imagine that one day, out of the blue, you find yourself thinking “Gee, I wonder who the five most popular mathematicians are?”

You do a bit of searching, and find the following website... but one problem. The data is being presented as HTML code. Each mathematician appears described by a `<li>`. However, there are ultimately a list of 100 names, which is where Python and web scraping come in. Web scraping is about downloading structured data from the web, selecting some of that data, and passing along what you selected to another process.

### Procedure

0. To begin make sure Beautiful Soup is installed

   `student@bchd:~$` `python3 -m pip install BeautifulSoup4`

0. Install requests

   `student@bchd:~$` `python3 -m pip install requests`

0. Create a new directory to work in

   `student@bchd:~$` `mkdir ~/mycode/scraping/`

0. Move into the new directory

   `student@bchd:~$` `cd ~/mycode/scraping/`

0. Create a new script

   `student@bchd:~/mycode/scraping/$` `vim webscrape01.py`

0. Create the following script.

    ```python
    #!/usr/bin/python3
    """ RZFeeser | Alta3 Research
    Learning to scrape webdata with BeautifulSoup
    """

    from requests import get
    from requests.exceptions import RequestException
    from contextlib import closing
    from bs4 import BeautifulSoup

    def simple_get(url):
        """
        Attempts to get the content at `url` by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
        """
        try:
            with closing(get(url, stream=True)) as resp:
                # stream=True means Requests cannot release the connection until closed
                # closing() will close "resp" at the end of this block
                if is_good_response(resp):
                    return resp.content
                    # .content() reads the HTML of the Requests object
                else:
                    return None

        except RequestException as e:
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None


    def is_good_response(resp):
        """
        Returns True if the response seems to be HTML, False otherwise.
        """
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)


    def log_error(e):
        """
        It is always a good idea to log errors.
        This function just prints them, but you can
        make it do anything.
        """
        print(e)

    def main():
        raw_html = simple_get('https://alta3.com')

        print(len(raw_html))

    if __name__ == "__main__":
        main()
    ```

0. Save and exit with `:wq`

0. Run your script:

    `student@bchd:~/mycode/scraping$` `python3 webscrape01.py`

0. Your output should be a number- looks like that's the total amount of lines in alta3.com!

0. The simple_get() function accepts a single url argument. It then makes a GET request to that URL. If nothing goes wrong, you end up with the raw HTML content for the page you requested. If there were any problems with your request (like the URL is bad, or the remote server is down), then your function returns None.

0. You may have noticed the use of the closing() function in your definition of simple_get(). The closing() function ensures that any network resources are freed when they go out of scope in that with block. Using closing() like that is good practice and helps to prevent fatal errors and network timeouts.

0. Next, let's try making some test HTML data we can work with.

0. Create the following HTML document, `montypython.html`.

    `student@bchd:~/mycode/scraping$` `vim montypython.html`

0. Your html file should look like this:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
      <title>Silly Example</title>
    </head>
    <body>
    <p id="camelot"> camelot is a silly place </p>
    <p id="knights"> bring us a shrubbery </p>
    <p id="brian"> always look on the bright side of life </p>
    </body>
    </html>
    ```

0. Save and exit with `:wq`

0. Create a script `nosoupforyou.py` that we can use to test Beautiful Soup.

0. Create the following script to read in our HTML data, `nosoupforyou.py`

    `student@bchd:~/mycode/scraping$` `vim nosoupforyou.py`

0. Your code should look like this:

    ```python
    #!/usr/bin/python3
    """
    Using BeautifulSoup to make data selections from montypython.html
    """

    from bs4 import BeautifulSoup

    # retrieve the raw HTML using the open function then read in the data
    raw_html = open('montypython.html').read()
    # use the backend parser 'html.parser' to parse out the raw_html
    html = BeautifulSoup(raw_html, 'html.parser')

    # the select method on the html object allows the selection of
    # CSS selectors to locate elements in the document
    # return a list of paragraph elements (dict like)
    for p in html.select('p'):
        if p['id'] == 'camelot' or p['id'] == 'knights':
            print(p.text)
    ```

0. Save and exit with `:wq`

0. Run the script, it should display something like the following:

    `student@bchd:~/mycode/scraping$` `python3 nosoupforyou.py`

    ```
    camelot is a silly place
    bring us a shrubbery
    ```

0. Breaking down the example, you first parse the raw HTML by passing it to the BeautifulSoup constructor. BeautifulSoup accepts multiple back-end parsers, but the standard back-end is 'html.parser', which you supply here as the second argument. (If you neglect to supply that 'html.parser', then the code will still work, but you will see a warning print to your screen.) The select() method on your html object lets you use CSS selectors to locate elements in the document. In the above case, html.select('p') returns a list of paragraph elements. Each p has HTML attributes that you can access like a dict.

0. Let's try to put what we are learning into practice. Visit the following link, and notice that it displays a list of 100 great mathematicians: http://www.fabpedigree.com/james/mathmen.htm

0. Using the `select()` method we learned about earlier, we can easily select the names of mathematicians. The secret is knowing what to pass to `select()`. In this case, all of the names are described via `<li>` (list item) tags. By passing `li` to `select('li')`, we can create a set of data suitable for looping across. Create a new script.

0. Create a new script.

   `student@bchd:~/mycode/scraping/$` `vim webscrape02.py`

0. Here is the content of your new script:

    ```python
    #!/usr/bin/python3

    from requests import get
    from requests.exceptions import RequestException
    from contextlib import closing
    from bs4 import BeautifulSoup

    def is_good_response(resp):
       """
       Returns True if the response seems to be HTML, False otherwise.
       """
       content_type = resp.headers['Content-Type'].lower()
       return (resp.status_code == 200
               and content_type is not None
               and content_type.find('html') > -1)

    def simple_get(url):
       """
       Attempts to get the content at `url` by making an HTTP GET request.
       If the content-type of response is some kind of HTML/XML, return the
       text content, otherwise return None.
       """
       try:
           with closing(get(url, stream=True)) as resp:
               if is_good_response(resp):
                   return resp.content
               else:
                   return None

       except RequestException as e:
           log_error('Error during requests to {0} : {1}'.format(url, str(e)))
           return None


    def get_names():
       """
       Downloads the page where the list of mathematicians is found
       and returns a list of strings, one per mathematician
       """
       url = 'http://www.fabpedigree.com/james/mathmen.htm'
       response = simple_get(url)

       if response is not None:
           html = BeautifulSoup(response, 'html.parser')
           names = set()
           for li in html.select('li'):
                for name in li.text.split('\n'):
                    # check if there's at least 1 character in name, otherwise it's an empty string
                    # check if any integers in string- most likely not a name
                    # then not including any strings that are likely sentences and not names
                    # because they're longer than 4 words
                   if len(name) > 1 and any(char.isdigit() for char in name) == False and len(name.split(' ')) < 6:
                       names.add(name.strip())
           return list(names)

       # Raise an exception if we failed to get any data from the url
       raise Exception('Error retrieving contents at {}'.format(url))

    def main():
       print(get_names())

    if __name__ == "__main__":
       main()
    ```

0. Save and exit

0. Run your script. A list of mathematicians should be returned.

   `student@bchd:~/mycode/scraping/$` `python3 webscrape02.py`

0. Great job! That's it for this lab. If you are tracking your code, be sure to push to GitHub!
    - `cd ~/mycode`
    - `git add *`
    - `git commit -m "webscraping with beautiful soup"`
    - `git push origin main`
