from splinter import Browser
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    scraped_dict={}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url='https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')    
    news_title =soup.find('div',class_='content_title').text
    print(news_title)
    news_p=soup.find('div', class_="article_teaser_body").text
    print(news_p)
    scraped_dict['news_p']=news_p
    scraped_dict['news_title']=news_title
    
    Featured_Space_Image_site_url ="https://spaceimages-mars.com/"    
    browser.visit(Featured_Space_Image_site_url)
    time.sleep(1)
    html=browser.html
    soup2=BeautifulSoup(html,'html.parser')
    featured_image_url=soup2.find('img',class_="headerimage")['src']
    Featured_Space_Image=Featured_Space_Image_site_url+featured_image_url
    scraped_dict['Featured_Space_Image']=Featured_Space_Image
    
    #-------------------------------------FACTS
    import pandas as pd
    facts_url="https://galaxyfacts-mars.com/"
    table=pd.read_html(facts_url)
    df=table[0]
    df.head()
    df.columns=df.iloc[0]
    df = df[1:]
    df.head()
    df=df.set_index(['Mars - Earth Comparison'])
    df
    facts_html=df.to_html(classes='data')
    print(facts_html)
    scraped_dict['facts_html']=facts_html
    
    #---------------------Mars Hemispheres
    mars_highResol_url="https://marshemispheres.com/"
    hemisphere_image_urls ={}
    browser.visit(mars_highResol_url)
    html=browser.html
    soup4=BeautifulSoup(html,'html.parser')
    url_results=soup4.find_all('div',class_="item")
    hemispheres_list=[]
    l=[]
    hemisphere_image_urls={}
    for r in url_results:
        hemisphere_image_urls['img_url']=mars_highResol_url+r.find('img',class_="thumb")['src']
        hemisphere_image_urls['title']=r.find('h3').text
        hemispheres_list.append(hemisphere_image_urls.copy())
    scraped_dict['hemispheres_list']=hemispheres_list
    return scraped_dict