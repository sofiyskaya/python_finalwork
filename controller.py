import view
import model
import text

my_pb = model.PhoneBook()

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                my_pb.open()
                view.print_message(text.load_success)

            case 2:
                my_pb.save()
                view.print_message(text.save_success)

            case 3:
                pb = my_pb.load()
                view.print_contacts(pb, text.pb_empty)

            case 4:
                contact = view.input_contact(text.input_new_contact)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_success(name))

            case 5:
                key_word = view.input_search(text.input_search)
                result = my_pb.search(key_word)
                view.print_contacts(result, text.empty_search(key_word))

            case 6:
                key_word = view.input_search(text.input_modify)
                result = my_pb.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index_modify)
                    else:
                        current_id = result[0].get('id')

                    contact = view.input_contact(text.modify_contact)
                    name = my_pb.modify(contact, current_id)
                    view.print_message(text.modify_success(name))
                else:
                    view.print_message(text.empty_search(key_word))

            case 7:
                key_word = view.input_search(text.input_delete)
                result = my_pb.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        del_id = view.input_search(text.input_index_delete)
                    else:
                        del_id = result[0].get('id')

                    name = my_pb.delete(del_id)
                    view.print_message(text.delete_success(name))
                else:
                    view.print_message(text.empty_search(key_word))

            case 8:
                break
             