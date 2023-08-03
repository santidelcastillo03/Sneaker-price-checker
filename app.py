from bs4 import BeautifulSoup
import requests
from sneaker import Sneaker
from file_helper import *


def load_data(sneaker_list):
     if not is_file_empty('sneakers.json'):
        f = open('sneakers.json', 'r')
        listS = json.loads(f.read())
        for sneaker in listS:
            sneaker_list.append(Sneaker(sneaker['name'], sneaker['url'], sneaker['price']))
        f.close()


def save_data(sneaker_list):
    f = open('sneakers.json', 'w')
    json.dump(sneaker_list, f, cls=CustomEncoder)
    f.close()

def add_sneaker(sneaker_list):
    url = input('Sneaker\'s URL: ')
    result = requests.get(url)
    soap = BeautifulSoup(result.text, 'html.parser')
    for tag in soap.find_all(class_='chakra-heading css-t7k2e1'):
        name = tag.text
        break
    for tag in soap.find_all(class_='chakra-text css-13uklb6'):
        price = tag.text
        break
    sneaker_list.append(Sneaker(name, url, price))
    print('Sneaker added')
    save_data(sneaker_list)

def remove_sneaker(sneaker_list):
    show_sneaker(sneaker_list)
    option = int(input('Select a sneaker to remove: '))
    sneaker_list.pop(option-1)
    print('Sneaker removed')
    save_data(sneaker_list)
    
def show_sneaker(sneaker_list):
    for index, sneaker in enumerate(sneaker_list):
        print(f'------{index+1}------\n{sneaker.name}')
        
def sneaker_info(sneaker_list):
    for s in sneaker_list:
        print(f'Name: {s.name}\nLast Sale: {s.price}')
        print('-----------------')
    
    
    




