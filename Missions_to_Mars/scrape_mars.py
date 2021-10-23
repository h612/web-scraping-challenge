from splinter import Browser
# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

def scrape():
    scraped_dict={}
    

    url='https://redplanetscience.com/'
    html=requests.get(url)
    soup=BeautifulSoup(html,'html.parser')    
    news_title =soup.find('div',class_='content_title').text
    print(news_title)
    news_p=soup.find('div', class_="article_teaser_body").text
    print(news_p)
    scraped_dict['news_title']=news_p
    scraped_dict['news_title']=news_title
    
    Featured_Space_Image_site_url ="https://spaceimages-mars.com/"    
    html=requests.get(Featured_Space_Image_site_url)
    soup2=BeautifulSoup(html,'html.parser')
    featured_image_url=soup2.find('img',class_="headerimage")['src']
    print(Featured_Space_Image_site_url+featured_image_url)
    scraped_dict['Featured_Space_Image_site_url']=Featured_Space_Image_site_url
    
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
    facts_html=df.to_html()
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
    for r in url_results:
        hemisphere_image_urls['title']=r.find('img',class_="thumb")['src']
        hemisphere_image_urls['img_url']=r.find('h3').text
        hemispheres_list.append(hemisphere_image_urls)
    print(hemispheres_list)
    scraped_dict['hemispheres_list']=hemispheres_list
    return scraped_dict
print(scrape())