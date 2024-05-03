import random
import json
import requests
from voice import voice


def thanks(text):
    options = [
        'Было несложно!',
        'Вам спасибо',
        'Обращайтесь'
    ]
    voice.text_to_speech(random.choice(options))


def fact(text):
    global data
    try:
        response = requests.get('http://numbersapi.com/random/math')
        data = response.json()
        print(data)
    except Exception:
        print('Что-то не так')
    voice.text_to_speech('Сгенерирован новый факт')


def next_fact(text):
    fact(text)


def read(text):
    voice.text_to_speech(data)


def write(text):
    with open('facts.txt', 'w') as file:
        file.write(data)
    voice.text_to_speech('Факт записан!')


def delete(text):
    with open('facts.txt', 'w') as file:
        lines = file.readlines()
        lines = lines[:-1]
    voice.text_to_speech('Последний факт удалён')
