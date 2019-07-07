import csv
from random import random, randint
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from myproject.live.models import Live


def csv_to_list(filename: str) -> list:
    '''
    Lê um csv e retorna um OrderedDict.

    Créditos para Rafael Henrique
    https://bit.ly/2FLDHsH
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        csv_data = [line for line in reader]
    return csv_data


def delete_users():
    users = User.objects.exclude(username='admin')
    users.delete()


def delete_lives():
    lives = Live.objects.all()
    lives.delete()


def save_data(data):
    '''
    Salva os dados no banco
    '''
    aux = []
    for item in data:
        number = item.get('number')
        title = item.get('title')
        guest = item.get('guest')
        like = randint(80, 2000)
        unlike = random() * like
        if guest:
            user = User.objects.create_user(
                username=slugify(guest),
                first_name=guest.split()[0],
                last_name=' '.join(guest.split()[1:]).strip()
            )
            guest_user = user
            obj = Live(
                number=number,
                title=title,
                like=like,
                unlike=unlike,
                guest=guest_user
            )
        else:
            obj = Live(number=number, title=title, like=like, unlike=unlike)
        aux.append(obj)
    Live.objects.bulk_create(aux)


class Command(BaseCommand):
    help = ''' Importa os dados. '''

    def handle(self, *args, **kwargs):
        delete_users()
        delete_lives()
        data = csv_to_list('data.csv')
        save_data(data)
