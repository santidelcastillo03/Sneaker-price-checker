class Sneaker:
    def __init__(self,name,url,price):
        self.name = name
        self.url = url
        self.price = price
        
def show_attr(self):
    print(f'Name: {self.name}')
    print(f'URL: {self.url}')
    print(f'Price: {self.price}')