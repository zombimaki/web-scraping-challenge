################################################################################
# Web Scraping Homework - Mission to Mars
################################################################################

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
import time

mars_scrape_dict = {}

################################################################################
# NASA Mars News
################################################################################
def scrape_mars_news():

        executable_path = {'executable_path': 'C:\ProgramData\ChromeDriver\chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

        # url for scraping
        mars_news_url = 'https://mars.nasa.gov/news/'
        browser.visit(mars_news_url)

        # HTML object
        mars_news_html = browser.html

        # Parse HTML with Beautiful Soup
        mars_news_soup = bs(mars_news_html, 'html.parser')

        # wait 5 seconds before running next block
        time.sleep(5)

        # collect the latest News Title and Paragraph Text
        mars_news_find = mars_news_soup.find("div", class_="list_text")

        news_title = mars_news_find.find('div', class_='content_title').text

        news_p = mars_news_find.find('div', class_='article_teaser_body').text 

        mars_scrape_dict['news_title'] = news_title
        mars_scrape_dict['news_p'] = news_p

        browser.quit()
        
        return mars_scrape_dict

################################################################################
# JPL Mars Space Images - Featured Image
################################################################################
def scrape_jpl():

        executable_path = {'executable_path': 'C:\ProgramData\ChromeDriver\chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

        # url for scraping
        jpl_base_url = 'https://www.jpl.nasa.gov/'
        jpl_suffix_url = 'spaceimages/?search=&category=Mars'
        jpl_img_url = jpl_base_url+jpl_suffix_url

        browser.visit(jpl_img_url)

        # HTML object
        jpl_img_html = browser.html

        # Parse HTML with Beautiful Soup
        jpl_img_soup = bs(jpl_img_html, 'html.parser')

        # wait 5 seconds before running next block
        time.sleep(5)

        # find the div class "carousel_container"
        jpl_img_find = jpl_img_soup.find("div", class_="carousel_container")

        # find the img url in the ariticle class carousel_item in the style 
        image_url = jpl_img_find.find("article", class_="carousel_item")["style"].\
                replace("'",'').\
                replace(";",'').\
                replace(")",'').\
                replace("(",'').\
                replace("background-image: url/",'')

        # concatenate the base and img urls
        featured_image_url = jpl_base_url + image_url

        mars_scrape_dict['image_url'] = featured_image_url

        browser.quit()

        return mars_scrape_dict

################################################################################
# Mars Facts
################################################################################
def scrape_facts():

        executable_path = {'executable_path': 'C:\ProgramData\ChromeDriver\chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

        # declare the url for pandas to scrape
        mars_facts_url = 'https://space-facts.com/mars/'

        mars_facts_url_df = pd.read_html(mars_facts_url)

        # take the first table of metrics
        mars_clean_fact_df = mars_facts_url_df[0]

        # rename colums
        mars_clean_fact_df.columns = ["Description", "Mars"]
        mars_clean_fact_df = mars_clean_fact_df.set_index("Description")

        # generate an html file of the df to the Resources folder
        html_table = mars_clean_fact_df.to_html()

        mars_scrape_dict['html_table'] = html_table

        browser.quit()

        return mars_scrape_dict

################################################################################
# Mars Hemispheres
################################################################################
def scrape_hemi():

        executable_path = {'executable_path': 'C:\ProgramData\ChromeDriver\chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

        # declare the urls
        mars_hemi_base_url = 'https://astrogeology.usgs.gov'
        mars_hemi_suffix_url = '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

        mars_hemi_url = mars_hemi_base_url+mars_hemi_suffix_url

        browser.visit(mars_hemi_url)

        # HTML object
        mars_hemi_html = browser.html

        # Parse HTML with Beautiful Soup
        mars_hemi_soup = bs(mars_hemi_html, 'html.parser')

        # wait 5 seconds before running next block
        time.sleep(5)

        # query the item div class
        mars_hemi_find = mars_hemi_soup.find_all("div", class_="item")

        # create a list to hold the dictionaries
        hemisphere_image_urls =[]

        for hemi in mars_hemi_find:
                # grab the title in the h3 tags
                title = hemi.find('h3').text
                # grab the href 
                hemi_img_suffix_url = hemi.find("a", class_="itemLink product-item")['href']
                hemi_img_url = mars_hemi_base_url+hemi_img_suffix_url

                browser.visit(hemi_img_url)

                # HTML object
                hemi_html = browser.html

                # Parse HTML with Beautiful Soup
                hemi_soup = bs(hemi_html, 'html.parser')

                # search the new link for the downloads div class
                hemi_find = hemi_soup.find("div", class_="downloads")
                # grab the first href a class
                img_url = hemi_find.find("a")["href"]
                # append dict to list
                hemisphere_image_urls.append({
                                                "title": title, 
                                                "img_url": img_url
                                                })

                mars_scrape_dict['hemis'] = hemisphere_image_urls
        
        browser.quit()
        return mars_scrape_dict

  
