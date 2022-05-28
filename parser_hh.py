import requests


def parser(stat, region_id=99, url_vacancies='https://api.hh.ru/vacancies'):
    num = 0
    start_page = 0
    while True:
        params = {
            'text': 'python Developer',
            'per_page': 50,
            'page': start_page,
            'area': region_id
        }
        response = requests.get(url_vacancies, params=params).json()

        try:
            items = response['items']
        except KeyError:
            print('ОШИБКА')
            items = []

        if len(items) == 0:
            print('Поиск завершен')
            break

        for item in items:  # список словарей   -> текущий словарь
            requirement = item['snippet']['requirement'].lower()  # словарь требований/ответственности
            num += stat.find(requirement)  # сбор статистики
        print(f'Поиск по стрнице {start_page}, обнаружено {num} совпадений')
        start_page += 1
