import time
import json
from config import config
import os

class MetroApiOnFireException(Exception):
    pass

class MetaApiOnFirException(Exception):
    pass

class MetaApi:
    def __init__(self):
        pass
    
    def fetch_like_count(self, wifi) -> [dict]:
        retry_attempt = 0
        while (retry_attempt < config['meta_api_retries']):
            try:
                # print('Fetching...')
                start = time.time()

            
                api_url = config['meta_api_url'].replace("[pageId]", os.getenv("META_PAGE_ID")).replace("[accessToken]", os.getenv('META_API_KEY'))
                # print(api_url)
                response = wifi.get(api_url, timeout=config.get("request_timeout", 15)).json()

                # print("Response returned by api: " + json.dumps(response))
                # print('Time to Update: ' + str(time.time() - start))
                return response

            except Exception as e:
                print(e)
                print('Failed to connect to API. Reattempting...')
                retry_attempt+=1
                    
               
        raise MetaApiOnFirException()
