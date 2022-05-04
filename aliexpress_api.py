# здесь должен быть код для работы с API ALIEXPRESS, но...........
from dotenv import load_dotenv
from os import getenv
from lxml import etree
import json
import requests

load_dotenv(".env")

TOKEN = getenv("API_TOKEN")

def get_xml_file_from_url (url: str) -> str:
    return requests.get(url, stream=True).text

def request_to_url (url, head):
    return requests.get(url, headers=head).text

def post_req (url, data, head):
    response = requests.post(url, headers=head, json=data)
    return response.text

head = {"x-auth-token": TOKEN}
# товар
product = {
  "products": [
    {
      "aliexpress_category_id": 201218701,
      "attribute_list": [
        {
          "attribute_name": "Название бренда",
          "attribute_name_id": 2,
          "attribute_value": "lolola collection",
          "attribute_value_id": 203673065
        },
        {
          "attribute_name": "Происхождение",
          "attribute_name_id": 219,
          "attribute_value": "SI (производитель)",
          "attribute_value_id": 9442281483
        },
        {
          "attribute_name": "Номер модели",
          "attribute_name_id": 3,
          "attribute_value": "GUzcgwMZTU"
        },
        {
          "attribute_name": "Материал",
          "attribute_name_id": 10,
          "attribute_value": "Дерево",
          "attribute_value_id": 351793
        },
        {
          "attribute_name": "Количество штук",
          "attribute_name_id": 100006020,
          "attribute_value": "Одна единица",
          "attribute_value_id": 11927795513
        },
        {
          "attribute_name": "Размер",
          "attribute_name_id": 491,
          "attribute_value": "gQQeHKfaKK"
        }
      ],
      "brand_name": "lolola collection",
      "freight_template_id": 1001,
      "gtin": "4606203099542",
      "inventory_deduction_strategy": "place_order_withhold",
      "language": "ru",
      "lot_num": 39315,
      "main_image_urls_list": [
        "https://st.aliexpress.ru/scqa-storage/open-async-pictures/TEST%20PIC%209.jpeg",
        "https://st.aliexpress.ru/scqa-storage/open-async-pictures/TEST%20PIC%201.jpeg",
        "https://st.aliexpress.ru/scqa-storage/open-async-pictures/TEST%20PIC%2010.jpeg",
        "https://st.aliexpress.ru/scqa-storage/open-async-pictures/TEST%20PIC%203.jpeg",
        "https://st.aliexpress.ru/scqa-storage/open-async-pictures/TEST%20PIC%207.jpeg"
      ],
      "multi_language_description_list": [
        {
          "language": "ru",
          "mobile_detail": {
            "module_list": [
              {
                "html": {
                  "content": "ТЕСТОВЫЙ ПРОДУКТ! НЕ ПОКУПАТЬ! mobile_detail ru"
                },
                "type": "html"
              }
            ],
            "version": "2.0.0"
          },
          "web_detail": {
            "module_list": [
              {
                "html": {
                  "content": "ТЕСТОВЫЙ ПРОДУКТ! НЕ ПОКУПАТЬ! web_detail ru"
                },
                "type": "html"
              }
            ],
            "version": "2.0.0"
          }
        },
        {
          "language": "en",
          "mobile_detail": {
            "module_list": [
              {
                "html": {
                  "content": "TEST PRODUCT! DO NOT BUY! mobile_detail en"
                },
                "type": "html"
              }
            ],
            "version": "2.0.0"
          },
          "web_detail": {
            "module_list": [
              {
                "html": {
                  "content": "TEST PRODUCT! DO NOT BUY! web_detail en"
                },
                "type": "html"
              }
            ],
            "version": "2.0.0"
          }
        }
      ],
      "multi_language_subject_list": [
        {
          "language": "ru",
          "subject": "1634134071 ТЕСТОВЫЙ ПРОДУКТ АСИНХРОННЫЙ ru"
        },
        {
          "language": "en",
          "subject": "1634134071 TEST PRODUCT ASYNC en"
        }
      ],
      "okpd2_codes": [
        "20.42.18.110",
        "20.42.18.112",
        "20.42.18.130"
      ],
      "package_height": 30,
      "package_length": 45,
      "package_width": 31,
      "product_unit": 100078558,
      "service_policy_id": 0,
      "shipping_lead_time": 17,
      "size_chart_id": 0,
      "sku_info_list": [
        {
          "bar_code": "I1lbMDQ6",
          "discount_price": "873039.0",
          "gtin": "",
          "inventory": 326003,
          "okpd2_codes": [],
          "price": "931686.0",
          "sku_attributes_list": [
            {
              "sku_attribute_name": "Доставка из",
              "sku_attribute_name_id": "200007763",
              "sku_attribute_value": "Бразилия",
              "sku_attribute_value_id": "203054829"
            },
            {
              "sku_attribute_name": "Цвет",
              "sku_attribute_name_id": "14",
              "sku_attribute_value": "Белый",
              "sku_attribute_value_id": "29"
            }
          ],
          "sku_code": "1634134071O7gXx6rY57",
          "tnved_codes": []
        }
      ],
      "tnved_codes": [
        "3306 10 000 0",
        "3306 20 000 0",
        "3306 90 000 0"
      ],
      "weight": "396.99"
    }
  ]
}

# post-запрос к магазину
res = json.loads(post_req("https://openapi.aliexpress.ru/api/v1/product/create", prod, head))
group_id = res["group_id"]
# статус запроса на создание товара
print(request_to_url(f"https://openapi.aliexpress.ru/public/api/v1/tasks?group_id={group_id}", head))
