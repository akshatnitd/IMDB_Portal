# IMDB_Portal

**_A simple utility script which assists in getting movies information and ratings._**

**Features:**

1. Get movie information by title
2. Find top rated movies
3. Rename the directories which contain the movies by appending IMDB rating and year of release to it.

**Modules used:**

- Bs4
  * It can be installed using `sudo pip install bs4` or `sudo apt-get install python-bs4`

- Requests
  * It can be installed using `sudo pip install requests` or `sudo apt-get install python-requests`

- lxml 
  * It can be installed using `sudo pip install lxml` or `sudo apt-get install python-lxml`



It is implemented using the **BeautifulSoup** module of **bs4** , **requests** module, along with **os**, **sys** and **json** modules.
* The first feature is implemented using the json response generated, after making a request via the **requests** module to the [TMDB API](https://www.themoviedb.org/) after generating an API key from the website. The json response is thereafter processed and the information is extracted using the **json** module. The IMDB rating is obtained by using the IMDB ID obtained from the json response and then using the ID to scrap rating from : http://www.imdb.com/title/<IMDB_ID> .

* The second feature is implemented by scraping the Top 'n'(say 50) movies from the [IMDB](http://www.imdb.com/chart/top) website using the response generated through the **requests** module.

*  The third feature is an added sub-feature to the first one. The information gathered, is thereafter appended to the directory name. This directory accessing and renaming is done by the help of **os** module.


**How to use:** Enter the choices and title of the movie when asked for.

**Instructions before using:** If you are going to use the third feature, make sure that all the folders' name contain only the movie name, and no other extra character or whitespace should be left. Also ensure you enter the correct and complete path (e.g.: _/home/user-name/Videos/_  or _/media/user-name/New Volume/Videos_).

**To run the script:** Type `python imdb.py` from your terminal.

All the results will be displayed on the terminal, as well as saved in a file called _info.txt_ in the same directory where the script is present.
