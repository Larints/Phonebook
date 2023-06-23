import text
import view
import model


def start():
    pb = model.PhoneBook()
    while True:
        select = view.menu()
        match select:
            case 1:
                if pb.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if pb.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(pb.get(), text.empty_book)
            case 4:
                new = view.add_contact()
                pb.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.view_input(text.search_word)
                result = pb.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:  # Костыль номер раз
                view.show_contacts(pb.get(), text.empty_book)
                act_id = pb.search_id(text.index_change)
                change_list = view.change(text.contact_change)
                pb.change_contact(act_id, change_list)
                view.print_message(text.change_success())
            case 7:
                word = view.view_input(text.search_word)
                result = pb.search(word)
                view.show_contacts(result, text.empty_search(word))
                index = view.view_input(text.index_remove)
                name = pb.remove(index)
                view.print_message(text.remove_contact(name))
            case 8:
                if pb.check_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer != 'n':
                        pb.save_file()
                view.print_message(text.goodbay)
                break
