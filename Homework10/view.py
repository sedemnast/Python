import text_fields as txt
from classes import Contact

def main_menu() -> int:
    print(txt.main_menu)
    while True:
        choice: str = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def show_contacts(book: list[Contact], message: str) -> None:
    print('\n' + '-' * 70)
    if book:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact}')
    else:
        print(message)
    print('-' * 70 + '\n')


def print_message(message: str) -> None:
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def edit_contact(book: list, message: str) -> tuple[int, Contact]:
    index: int = 0
    while True:
        choice: str = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            index = int(choice)
            break
    print(txt.enter_or_empty)
    contact: Contact = new_contact()
    return index, contact


def new_contact() -> Contact:
    print()
    name: str = input(txt.new_name)
    phone: str = input(txt.new_phone)
    comment: str = input(txt.new_comment)
    return Contact(name, phone, comment)


def enter_keyword() -> str:
    print()
    key_word: str = input(txt.input_keyword)
    return key_word


def input_index(book: list, message: str) -> int:
    while True:
        choice: str = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            return int(choice)


def confirm(message: str) -> bool:
    answer = input(f'{message} (y/n)')
    return answer.lower() == 'y'
