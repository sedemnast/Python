import model
import view
import text_fields as txt


def start():
    while True:
        choice = view.main_menu()
        if choice == 1:
            model.open_file()
            view.print_message(txt.successful_open)
        elif choice == 2:
            model.save_file()
            view.print_message(txt.successful_save)
        elif choice == 3:
            pb = model.get_phone_book()
            view.show_contacts(pb, txt.empty_list_or_not_open_file)
        elif choice == 4:
            new_contact = view.new_contact()
            model.add_contact(new_contact)
            view.print_message(txt.contact_saved(new_contact.get('name')))
        elif choice == 5:
            word = view.enter_keyword()
            result = model.find_contact(word)
            view.show_contacts(result, txt.not_found(word))
        elif choice == 6:
            pb = model.get_phone_book()
            view.show_contacts(pb, txt.empty_list_or_not_open_file)
            if pb:
                edited_contact = view.edit_contact(pb, txt.input_index)
                model.edit_contact(edited_contact)
                view.print_message(txt.successful_edited(edited_contact[1].get('name')))
        elif choice == 7:
            pb = model.get_phone_book()
            view.show_contacts(pb, txt.empty_list_or_not_open_file)
            if pb:
                index = view.input_index(pb, txt.input_delete_index)
                if view.confirm(txt.confirm_delete(pb[index - 1].get('name'))):
                    view.print_message(txt.delete_contact(model.remove_contact(index)))
        elif choice == 8:
            if model.original_book != model.phone_book:
                if view.confirm(txt.no_saved_book):
                    model.save_file()
            view.print_message(txt.goodbye)
            exit()
