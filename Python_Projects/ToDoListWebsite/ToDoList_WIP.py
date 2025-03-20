import os
import shutil

def initialize():
    folder_name = 'ToDoList'
    create_folder(folder_name)

    title = 'ToDoList'
    body = '''
    <h1>ToDoList</h1>
    <ul>
        <li>Task 1</li>
        <li>Task 2</li>
        <li>Task 3</li>
    </ul>
    '''
    html = create_html(title, body)
    file_name = os.path.join(folder_name, 'index.html')
    create_file(file_name, html)
    return


def create_html(title, body):
    html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        {body}
    '''
    return html

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(f'{folder_name} already exists.')
        print('Do you want to overwrite it?')
        overwrite = input('Y/N: ')
        if overwrite.lower() == 'y':
            shutil.rmtree(folder_name)
            os.mkdir(folder_name)
            print(f'{folder_name} is overwritten.')
        else:
            print(f'{folder_name} is not overwritten.')

def create_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def initial_parameters():
    if os.path.exists('ToDoList'):
        print("ToDoList already exists. Would you like to display it?")
        answer = input("Y/N: ")
        if answer.lower() == 'y':
            folder_name = 'ToDoList'
            file_name = os.path.join(folder_name, 'index.html')
            os.system(file_name)
            return
                 
    print("Would you like to create a new/overwrite ToDoList?")
    answer = input("Y/N: ")

    if answer.lower() == 'y':
        initialize()

    else:
        print("Would you like to display the existing ToDoList?")
        answer = input("Y/N: ")

        if answer.lower() == 'y':
            folder_name = 'ToDoList'
            file_name = os.path.join(folder_name, 'index.html')
            os.system(file_name)
            
        else:
            print("Goodbye!")
            return


def main():
    initial_parameters()
    return
        
if __name__ == '__main__':
    main()