# web-scraping-challenge


### The web-scraping-challenge consists of:

1. Analyzing the data and developing/testing the code needed to scrape the data in a jupyter notebook.
2. Taking the code developed in step one and creating a python app to be used by a flask app to scrape the data.
3. Developing a flask app to host the site and scrape the web data into a mongo database using the app created in the previous step.
4. Developing an index.html file with bootstrap to display the front end.


scrape_mars.py file does the following:

1. Scrapes https://mars.nasa.gov/news/ for the top news article's title and paragraph text.
2. Scrapes https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars for the featured image url.
3. Scrapes https://space-facts.com/mars/ for the Mars facts data with Pandas and convert to html.
4. Scrapes https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars for the high resolution images of the hemispheres and save the title and url to a dictionary.
5. Returns all of the above scraped data as one Python dictionary.

app.py does the following:

1. Establishes a connection to the mars_app mongo db.
2. Establises a root route that returns the content of index.html.
3. Establises a /scrape route which calls the scarpe_mars.py app and updates the mars_app db with the scraped values.

index.html displays the data to best fit the example photos provided with the assignment.
mission_to_mars.ipynb was used to develop the code in scrape_mars.py.