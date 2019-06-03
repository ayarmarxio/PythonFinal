import sys
import requests
from bs4 import BeautifulSoup
import shutil
from handler import create_intro
from scraper import create_url
from scraper import get_assignment_1
from scraper import get_assignment_2
from scraper import get_assignment_3
from scraper import get_assignment_4


def start_process(value):
    print('Process has started...')
    if value == '1':
        print('Get assignment number 1')
        get_assignment_1(value, 'p')
    elif value == '2':
        print('Get assignment number 2')
        get_assignment_2(value, 'li')
    elif value == '3':
        print('Get assignment number 3')
        get_assignment_3(value, 'li')
    elif value == '4':
        print('Get assignment number 4')
        get_assignment_4(value, 'p')
    else:
        print('Something wrong has happened')
        get_assignment_4(value, 'p')
        
    
   

def check_input(value):
    input_list = ['1', '2', '3', '4']
    if value in input_list:
        print('Input has been validated')
        return True           
    else:
        print('You should write 1 or 2 or 3 or 4')
        return False


def input_handler():
    i = False
    while i == False:
        print ('Write the number of the assignment you want to see')
        print('It can be: 1 or 2 or 3 or 4')
        print('')
        val = str(input('Write here: '))        
        i = check_input(val)
    start_process(val)
    

def main():
    create_intro()
    input_handler()
      
   

if __name__ == '__main__':
    main()