from find_area_id import get_id_region
from statistics import Statistics
from parser_hh import parser
from pprint import pprint
import json

if __name__ == '__main__':
    stat = Statistics()
    DOMAIN = 'https://api.hh.ru/'
    url_area = f'{DOMAIN}areas/113'
    region_id = get_id_region(url_area, 'Уфа')
    url_vacancies = f'{DOMAIN}vacancies'
    parser(stat, region_id=region_id, url_vacancies=url_vacancies)
    pprint(stat.get_stat())
    with open('statistic.json', 'w') as f:
        json.dump(stat.get_stat(), f)
