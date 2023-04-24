import text_fields as txt


def main_menu() -> int:
    print(txt.main_menu)
    while True:
        choice = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def show_contacts(book: list[dict], message: str) -> None:
    print('\n' + '–' * 70)
    if book:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
    else:
        print(message)
    print('–' * 70 + '\n')


def print_message(message: str) -> None:
    print(f'\n{"-" * len(message)}\n{message}\n{"-" * len(message)}\n')


def edit_contact(book: list[dict], message: str) -> tuple[int, dict[str, str]]:
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            index = int(choice)
            break
    print(txt.enter_or_empty)
    return index, new_contact()


def new_contact() -> dict[str, str]:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    return {'name': name, 'phone': phone, 'comment': comment}


def enter_keyword() -> str:
    print()
    return input(txt.input_keyword)


def input_index(book: list[dict], message: str) -> int:
    while True:
        choice = input(message)
        if choice.isdigit() and 0 < int(choice) < len(book) + 1:
            return int(choice)


def confirm(message: str) -> bool:
    answer = input(f'{message} (y/n)')
    return answer.lower() == 'y'
