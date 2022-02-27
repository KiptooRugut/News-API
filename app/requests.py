from app import app
import urllib.request,json
from .models import Source

# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_source(thesource):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(thesource,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_sources = None

        if get_source_response['sources']:
            news_source_list = get_source_response['sources']
            news_sources = process_sources(news_source_list)


    return news_sources

def process_sources(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        sources_list: A list that contain various article sources
    Returns :
        news_sources: A list of source objects
    '''
    news_sources = []
    for source_item in source_list:
      
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        

        if name:
            news_object_sources =Source(id,name,description,url)
            news_sources.append(news_object_sources)

    return news_sources