# здесь должен быть код для работы с API ALIEXPRESS, но...........
from dotenv import load_dotenv
from os import getenv
from lxml import etree
import requests

load_dotenv(".env")

TOKEN = getenv("API_TOKEN")

def get_xml_file_from_url (url: str) -> str:
    return requests.get(url, stream=True).text

def request_to_url (url, head):
    return requests.get(url, headers=head).text

def post_req (url, data, head):
    response = requests.post(url, headers=head, data=data)
    return response.text

head = {"x-auth-token": TOKEN}

# запрос не работает!!!
print(request_to_url("https://openapi.aliexpress.ru/api/v1/method-group/method", head))
