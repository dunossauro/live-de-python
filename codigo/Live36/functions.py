from json import dump
from re import sub
from bs4 import BeautifulSoup as bs
from requests import get


def pretty_format(bs_list):
    return ''.join(map(lambda x: sub(r'</?(br|p)/?>', ' ', str(x)),
                       bs_list.find_all('p'))).replace('  ', ' ').strip()


def get_lirycs(base_url, musics_links, music):
    return bs(get('{}{}'.format(base_url, musics_links[music])).text,
              'lxml').find('article')


def dict_to_json(path, _dict):
    with open('{}.json'.format(path), 'w') as fp:
        dump(dict, fp, indent=2, ensure_ascii=False)
