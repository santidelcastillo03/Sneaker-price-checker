from app import *

def main():
    sneaker_list = []
    load_data(sneaker_list)
    
    while True:
        print('1. Add sneaker\n2. Remove sneaker\n3. Show sneaker info\n4. Exit')
        
        
        option = input('Select an option: ')
        
        if option == '1':
            add_sneaker(sneaker_list)
        elif option == '2':
            remove_sneaker(sneaker_list)
        elif option == '3':
            sneaker_info(sneaker_list)
        elif option == '4':
            print('Bye')
            save_data(sneaker_list)
            break
        else:
            print('Invalid option')
main()
