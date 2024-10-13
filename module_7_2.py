def custom_write(file_name, strings) -> dict:
    with open(file_name, 'a', encoding='utf-8') as f:
        string_positions = {}
        for index, string in enumerate(strings):
            byte = f.tell()
            try:
                f.write(f'{string}\n')
            except Exception as e:
                print(f'При попытке записи в файл произошла ошибка: {e}')
                exit()
            string_positions[(index, byte)] = string
        return string_positions


if __name__ == '__main__':

    info = [
        'Text for tell',
        'Используйте кодировку utf-8',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)

    for elem in result.items():
        print(elem)