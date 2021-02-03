
import requests
from bs4 import BeautifulSoup



def getBigStoryHeadLines(soup):
    headlines = []
    big_story_headlines = {}
    big_story_list = soup.findAll('div', attrs = {'data-tb-region' :'big-story'})
    for each_big_story in big_story_list:
        title_list = each_big_story.findAll('a', attrs={'class' :'item-title'})
        #     print(title_list)
        for each_title in title_list :
            title_text = each_title.text
            headlines.append(title_text)
    big_story_headlines['topic'] = "Big Story"
    big_story_headlines['headlines'] = headlines
    big_story_headlines['language_code'] = "en"
    if len(headlines) > 0:
        big_story_headlines['is_data_empty'] = "false"
    else:
        big_story_headlines['is_data_empty'] = "true"

    return big_story_headlines




# In[25]:


# getBigStoryHeadLines(soup)


# In[26]:


def getTopStoryHeadLines(soup):
    headlines = []
    top_story_headlines = {}
    top_story_list = soup.findAll('div', attrs = {'data-tb-region' :'top-stories'})
    for each_top_story in top_story_list:
        title_list = each_top_story.findAll('a', attrs={'class' :'item-title'})
        #     print(title_list)
        for each_title in title_list :
            title_text = each_title.text
            headlines.append(title_text)
    top_story_headlines['topic'] = "Top Stories - World"
    top_story_headlines['headlines'] = headlines
    top_story_headlines['language_code'] = "en"
    if len(headlines) > 0:
        top_story_headlines['is_data_empty'] = "false"
    else:
        top_story_headlines['is_data_empty'] = "true"
    return top_story_headlines




# In[27]:


# getTopStoryHeadLines(soup)


# In[28]:


def getTopTechStoryHeadLines(soup):
    headlines = []
    top_tech_story_headlines = {}
    top_tech_story_list = soup.findAll('div', attrs = {'data-tb-region' :'tech'})
    for each_top_tech_story in top_tech_story_list:
        title_list = each_top_tech_story.findAll('a', attrs={'class' :'item-title'})
        #     print(title_list)
        for each_title in title_list :
            title_text = each_title.text
            headlines.append(title_text)
    top_tech_story_headlines['topic'] = "Tech Stories"
    top_tech_story_headlines['headlines'] = headlines
    top_tech_story_headlines['language_code'] = "en"
    if len(headlines) > 0:
        top_tech_story_headlines['is_data_empty'] = "false"
    else:
        top_tech_story_headlines['is_data_empty'] = "true"
    return top_tech_story_headlines




# In[29]:


# getTopTechStoryHeadLines(soup)


# In[30]:


def getRootPageHeadLines():
    root_headlines = []
    URL = "https://www.ndtv.com/"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    root_headlines.append(getBigStoryHeadLines(soup))
    root_headlines.append(getTopStoryHeadLines(soup))
    root_headlines.append(getTopTechStoryHeadLines(soup))
    return root_headlines



# In[31]:


# getRootPageHeadLines()


# In[32]:


def getIndiaNewsheadLines(soup, pg_no = None):
    headlines = []
    top_india_story_headlines = {}
    top_india_story_list = soup.findAll('h2', attrs = {'class' :'newsHdng'})
    for each_top_india_story in top_india_story_list:
        title_list = each_top_india_story.findAll('a')
        #         print(title_list)
        for each_title in title_list :
            title_text = each_title.text
            headlines.append(title_text)
    top_india_story_headlines['topic'] = "India"  if pg_no is None else "India  " +str(pg_no)
    top_india_story_headlines['headlines'] = headlines
    top_india_story_headlines['language_code'] = "en"
    if len(headlines) > 0:
        top_india_story_headlines['is_data_empty'] = "false"
    else:
        top_india_story_headlines['is_data_empty'] = "true"
    return top_india_story_headlines




# In[33]:


def getIndiaPageHeadLines():
    india_headlines = []
    URL = "https://www.ndtv.com/india?pfrom=home-ndtv_mainnavgation"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    india_headlines.append(getIndiaNewsheadLines(soup, pg_no = 1))

    URL_PAGE_2 = "https://www.ndtv.com/india/page-2"
    r = requests.get(URL_PAGE_2)
    soup = BeautifulSoup(r.content, "lxml")
    india_headlines.append(getIndiaNewsheadLines(soup, pg_no = 2))

    URL_PAGE_3 = "https://www.ndtv.com/india/page-3"
    r = requests.get(URL_PAGE_3)
    soup = BeautifulSoup(r.content, "lxml")
    india_headlines.append(getIndiaNewsheadLines(soup ,pg_no = 3))

    return india_headlines



# In[34]:


# getIndiaPageHeadLines()


# In[35]:


def getBuisnessHeadLines(soup):
    headlines = []
    top_buisness_story_headlines = {}
    top_buisness_story_list = soup.findAll('div', attrs = {'class' :'widcont_topstories'})
    #     print("top_buisness_story_list => ",top_buisness_story_list)
    for each_top_buisness_story in top_buisness_story_list:
        title_list = each_top_buisness_story.findAll('a')
        #         print(title_list)
        for each_title in title_list :
            title_text = each_title.text
            #             print("title_text => ",title_text)
            if len(title_text) > 0:
                headlines.append(title_text)
    top_buisness_story_headlines['topic'] = "Global Buisness"
    top_buisness_story_headlines['headlines'] = headlines
    top_buisness_story_headlines['language_code'] = "en"
    if len(headlines) > 0:
        top_buisness_story_headlines['is_data_empty'] = "false"
    else:
        top_buisness_story_headlines['is_data_empty'] = "true"
    return top_buisness_story_headlines



# In[36]:


def getBuisnessPageHeadLines():
    buisness_headlines = []
    URL = "https://www.ndtv.com/business?pfrom=ndtv-globalnav"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    buisness_headlines.append(getBuisnessHeadLines(soup))
    return buisness_headlines



# In[37]:


# getBuisnessPageHeadLines()


# In[38]:


def getTechMediaAndTelecomHeadLines(soup, pg_no=None):
    headlines = []
    top_tech_medta_and_telecom_story_headlines = {}
    top_tech_medta_and_telecom_story_list = soup.findAll('h2', attrs = {'class' :'newsHdng'})
    for each_top_tech_medta_and_telecom_story in top_tech_medta_and_telecom_story_list:
        title_list = each_top_tech_medta_and_telecom_story.findAll('a')
        #         print(title_list)
        for each_title in title_list :
            title_text = each_title.text
            headlines.append(title_text)
    top_tech_medta_and_telecom_story_headlines['topic'] = "Tech-Media-Telecom"  if pg_no is None else "Tech-Media-Telecom  " +str(pg_no)
    top_tech_medta_and_telecom_story_headlines['headlines'] = headlines
    top_tech_medta_and_telecom_story_headlines['language_code'] = "en"
    if len(headlines) > 0:
        top_tech_medta_and_telecom_story_headlines['is_data_empty'] = "false"
    else:
        top_tech_medta_and_telecom_story_headlines['is_data_empty'] = "true"
    return top_tech_medta_and_telecom_story_headlines


# In[39]:


def getTechMediaAndTelecomPageHeadLines():
    buisness_headlines = []
    URL = "https://www.ndtv.com/business/tech-media-telecom"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "lxml")
    buisness_headlines.append(getTechMediaAndTelecomHeadLines(soup, pg_no = 1))

    #     URL = "https://www.ndtv.com/business/tech-media-telecom/page-2"
    #     r = requests.get(URL)
    #     soup = BeautifulSoup(r.content, "lxml")
    #     buisness_headlines.append(getTechMediaAndTelecomHeadLines(soup, pg_no = 2))

    #     URL = "https://www.ndtv.com/business/tech-media-telecom/page-3"
    #     r = requests.get(URL)
    #     soup = BeautifulSoup(r.content, "lxml")
    #     buisness_headlines.append(getTechMediaAndTelecomHeadLines(soup, pg_no = 3))

    #     URL = "https://www.ndtv.com/business/tech-media-telecom/page-4"
    #     r = requests.get(URL)
    #     soup = BeautifulSoup(r.content, "lxml")
    #     buisness_headlines.append(getTechMediaAndTelecomHeadLines(soup, pg_no = 4))

    return buisness_headlines



# In[40]:


# getTechMediaAndTelecomPageHeadLines()


# In[41]:


def getNDTVNewsHeadLines():
    temp_list = []
    root_page_headlines = getRootPageHeadLines()
    india_page_headlines = getIndiaPageHeadLines()
    buisness_page_headlines = getBuisnessPageHeadLines()
    tech_media_telecom_page_headlines = getTechMediaAndTelecomPageHeadLines()

    temp_list = root_page_headlines + india_page_headlines +  buisness_page_headlines + tech_media_telecom_page_headlines
    return temp_list

# getNDTVNewsHeadLines()







