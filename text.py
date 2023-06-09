main_menu = '''\nГлавное меню:
1. Открыть файл
2. Сохранить файл
3. Показать контакты
4. Добавить контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_success = 'Телефонная книга успешно открыта!'

save_success = 'Телефонная книга успешно сохранена!'

pb_empty = 'Телефонная книга пуста или не загружена!'

input_new_contact = "Введите данные нового контакта: "

new_contact = {'name': 'Введие имя: ',
            'phone': 'Ведите номер телефона: ',
            'comment': 'Введите комментарий: '}


def new_contact_success(name: str):
    return f'Контакт {name} успешно добавлен!'

input_search = 'Введите слово для поиска: '

def empty_search(word):
    return f'Контакты, содержащие слово "{word}" не найдены!'

input_modify = 'Какой контакт будем менять? Введите слово для поиска: '
modify_contact = 'Введите новые данные или оставьте поле пустым, чтобы ничего не менять: '
input_index_modify = 'Ведите индекс контакта для изменения: '

def modify_success(name: str):
    return f'Контакт "{name}" успешно изменен!'


input_delete = 'Какой контакт будем удалять? Введите слово для поиска: '
input_index_delete = 'Ведите индекс контакта для удаления: '

def delete_confirm(name: str):
    return f'\nВы уверены, что хотите удалить контакт "{name}" (Y/N)?: '

def delete_success(name: str):
    return f'Контакт "{name}" успешно удален!'