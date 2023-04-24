class Contact:
    def __init__(self, name: str, phone: str, comment: str = ''):
        self.name = name
        self.phone = phone
        self.comment = comment

    def edit(self, name: str = None, phone: str = None, comment: str = None):
        self.name = name if name else self.name
        self.phone = phone if phone else self.phone
        self.comment = comment if comment else self.comment

    def to_str(self) -> str:
        return f'{self.name};{self.phone};{self.comment}'

    def __str__(self) -> str:
        return f'{self.name:<20}{self.phone:<20}{self.comment:<20}'


class PhoneBook:
    def __init__(self, path: str):
        self.path = path
        self.phone_book: list[Contact] = []
        self.is_changed = False

    def open(self):
        self.phone_book.clear()
        with open(self.path, 'r', encoding='UTF-8') as file:
            for line in file:
                contact = line.strip().split(';')
                self.phone_book.append(Contact(contact[0], contact[1], contact[2]))

    def save(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            for contact in self.phone_book:
                file.write(contact.to_str() + '\n')
        self.is_changed = False

    def get(self) -> list[Contact]:
        return self.phone_book

    def add(self, new_contact: Contact) -> None:
        self.phone_book.append(new_contact)
        self.is_changed = True

    def find(self, word: str) -> list[Contact]:
        result = []
        for contact in self.phone_book:
            if word in contact.to_str():
                result.append(contact)
        return result

    def edit_contact(self, index: int, new_contact: Contact) -> None:
        self.phone_book[index - 1].edit(new_contact.name, new_contact.phone, new_contact.comment)
        self.is_changed = True

    def remove(self, index: int) -> str:
        deleted_element = self.phone_book.pop(index - 1)
        self.is_changed = True
        return deleted_element.name

    def save_on_exit(self) -> bool:
        return self.is_changed
