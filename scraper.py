import sys
import requests
from bs4 import BeautifulSoup
import shutil

def get_assignment_1(value, tag_value):
    print_title(value)
    assignment_requirements = find_requirements(value, tag_value)

    for requirement in assignment_requirements:
        if 'NOTE' in requirement.text:
                pass
        elif 'A html page looking like this:' in requirement.text:
                pass
        elif 'Becomes:' in requirement.text:
                pass
        elif 'The links to follow' in requirement.text:
                pass            
        else:
            print(requirement.text)
            requirement_text = requirement.text
            add_to_file(requirement_text)


def get_assignment_2(value, tag_value):
    print_title(value)
    assignment_requirements = find_requirements(value, tag_value)

    for requirement in assignment_requirements:
        if 'Exam' in requirement.text:
            pass
        elif "Assignment" in requirement.text:
            pass
        elif 'Assingment' in requirement.text:
            pass
        else:
            print(requirement.text)
            requirement_text = requirement.text
            add_to_file(requirement_text)
        

def get_assignment_3(value, tag_value):
    print_title(value)
    assignment_requirements = find_requirements(value, tag_value)

    for requirement in assignment_requirements:
        if 'Exam' in requirement.text:
            pass
        elif "Assignment" in requirement.text:
            pass
        elif 'Assingment' in requirement.text:
            pass
        else:
            print(requirement.text)
            requirement_text = requirement.text
            add_to_file(requirement_text)

def get_assignment_4(value, tag_value):
    print_title(value)
    assignment_requirements = find_requirements(value, tag_value)
    for requirement in assignment_requirements:
        if "NOTE" in requirement.text:
            pass
        elif "Assignment" in requirement.text:
                pass
        else:
            print(requirement.text)
            requirement_text = requirement.text
            add_to_file(requirement_text)


def find_requirements(value, tag_value):
    url = create_url(value)
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')    
    assignment_requirements = soup.find_all(tag_value)
    return assignment_requirements

def create_url(url_index):
    url_base = "https://clbokea.github.io/exam/assignment_" 
    url_ending = ".html"
    new_url = url_base+url_index+url_ending
    return new_url

def add_to_file(input_text):
    string = str(input_text)
    string_line = string + "\n"
    with open('your_assignment.md', 'a+') as file:
        file.write(string_line)

def print_title(url_index):
    url = create_url(url_index)
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    assignment_titles = soup.find_all('h1')

    for title in assignment_titles:
        print(title.text.upper())
        string = str(title.text.upper())
        string_line = string + "\n"
        add_to_file(string_line)
        add_to_file("\n")