# UI - user interface
from sesiunea9.marketplace.marketplace_repository import CSVMarketplaceRepository, JSONMarketplaceRepository
from pprint import pprint


def choose_db():
    db_menu = """
        DB MENU
    1. CSV
    2. JSON
    """
    print(db_menu)
    cmd = int(input("Enter DB type: "))
    file_type = 'csv' if cmd == 1 else 'json'
    file_name = f'Users.{file_type}'
    return (
               CSVMarketplaceRepository(file_name) if file_type == 'csv'
               else JSONMarketplaceRepository(file_name)
           ), file_type


def print_menu():
    menu = """
        MENU
    1. ADD User
    2. DELETE User
    3. SHOW Users
    4. EXIT MENU
    """
    print(menu)


def add_user(repository, repo_type):
    name = input('Enter your name: ')
    age = int(input('Enter you age: '))
    user_id = abs(hash(name) + hash(age))
    if repo_type == 'csv':
        repository.add([user_id, name, age])
    else:
        repository.add({'ID': user_id, 'name': name, 'age': age})


def delete_user(repository):
    user_id = input('Enter the user ID to be deleted: ')
    repository.delete(user_id)


def show_users(repository):
    pprint(repository.read())


def run():
    repo, repo_type = choose_db()
    while True:
        print("*" * 50)
        print_menu()
        user_input = int(input(f"Please enter your choose: "))
        if user_input == 1:
            add_user(repo, repo_type)
        elif user_input == 2:
            delete_user(repo)
        elif user_input == 3:
            show_users(repo)
        elif user_input == 4:
            exit(0)
        else:
            print('Comanda invalida!')


run()
