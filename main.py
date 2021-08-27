from bs4 import BeautifulSoup
import requests
import lxml
import json

URL = 'https://webscraper.io/test-sites/e-commerce/allinone'

#fetch page content
def fetch_page_content(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')
    except Exception as e:
        raise e
    print('soup', soup)
    return soup
   


#parse page content
def parse_page_content(content):
    
    top_items = []
    products = content.select('div.thumbnail')
    for product in products:
        title = product.select('a.title')[0].text
        review = product.select('div.ratings > p.pull-right')[0].text
        price = product.select(' h4.price')[0].text
        description = product.select('div.caption > p.description')[0].text
        image = product.select('img')[0].get('src')

        top_items.append({
            'title': title.strip(),
            'review': review.strip(),
            'price':price.strip(),
            'image':image.strip(),
            'description': description.strip()
        })
    # print('p', top_items)
    return top_items

#save page content to json
def save_to_json(data):
    with open('products.json', 'w') as output_file:
        json_file = json.dumps(data)
        output_file.write(json_file)

if __name__ == '__main__':
    result = fetch_page_content(URL)
    # print(result)
    parsed_content= parse_page_content(result)
    print (parsed_content)
    save_to_json(parsed_content)