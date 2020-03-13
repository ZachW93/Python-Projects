from imgurpython import ImgurClient
import random
import os
from dotenv import load_dotenv


def random_image():

    load_dotenv()
    client_id = os.getenv('IMGUR_TOKEN');
    client_secret = os.getenv('IMGUR_SECRET');
    
    client = ImgurClient(client_id, client_secret)
    
    items = client.gallery()
    item = random.choice(items)
    return item.link

def BikiniBottomTwitter():
    
    load_dotenv()
    client_id = os.getenv('IMGUR_TOKEN');
    client_secret = os.getenv('IMGUR_SECRET');
    
    client = ImgurClient(client_id, client_secret)
    items = client.gallery(section='r', sort='BikiniBottomTwitter', show_viral=False)
    item = random.choice(items)
    return item.link