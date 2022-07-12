# ls bot.py | entr -r python bot.py
from os import getenv
from dotenv import load_dotenv
from uvloop import install
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
)

load_dotenv()
install()


app = Client(
    'dunossauro_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

@app.on_callback_query()
async def callback(client, callback_query):
    pages = {
        'data': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_1'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_2'),
            'texto': 'Você está de volta ao inicio'
        },
        'page_1': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_2'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 1'
        },
        'page_2': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='data'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_1'),
            'texto': 'Você está na página 2'
        }
    }

    page = pages[callback_query.data]
    inline_markup = InlineKeyboardMarkup(
        [[page['anterior'], page['proximo']]]
    )
    await callback_query.edit_message_text(page['texto'], reply_markup=inline_markup)


@app.on_message(filters.command('callback'))
async def callbacks(client, message):
    inline_markup = InlineKeyboardMarkup(
        [
            [
          	InlineKeyboardButton('Callback', callback_data='data'),
                InlineKeyboardButton('URL', url='https://docs.pyrogram.org')
            ]
        ]
    )
    await message.reply('Escolha algo!', reply_markup=inline_markup)

@app.on_message(filters.command('keyboard'))
async def start_command(client, message):
    await message.reply(
        'Escolha algo!',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['a', 'b'],
                ['c', 'd', 'e', 'f', 'g']
            ],
            resize_keyboard=True
        ),
    )


@app.on_message(filters.command('help') |filters.command('start'))
async def help_command(client, message):
    await message.reply(
        'Esse é o menu para pedir ajuda!\n'
        'Use **/start** para iniciar o bot!\n'
        'Use **/menu** para esse menu em teclado!\n'
        'Use **/help** para pedir ajuda!\n'
        'Use **/photo** para ver uma foto TOP!\n'
        'Use **/keyboard** para ver um teclado de comandos\n'
        'Use **/callback** para ver alguns botões\n'
        '**Me envie stickers** xD\n'
        '`Não me envie audio`, **eu odeio**\n'
        '--Também questiono veracidade de imagems.--'
    )

@app.on_message(filters.command('menu'))
async def help_command(client, message):
    await message.reply(
        'Escolha algo!',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['/start', '/help'],
                ['/photo', '/keyboard'],
                ['/callback']
            ],
            resize_keyboard=True
        ),
    )

@app.on_message(filters.command('photo'))
async def photo_command(client, message):
    await app.send_photo(
        message.chat.id,
        'https://images.pexels.com/photos/12489081/pexels-photo-12489081.jpeg?cs=srgb&dl=pexels-josh-hild-12489081.jpg&fm=jpg'
    )


@app.on_message(filters.sticker)
async def stickers(client, message: Message):
    await app.send_sticker(
        message.chat.id,
        message.sticker.file_id
    )


@app.on_message(filters.voice)
async def audio(client, message: Message):
    await message.reply('Ah não, já vai começar o podcast!')


@app.on_message((filters.photo | filters.video) & filters.private)
async def photo_or_video_private(client, message: Message):
    await message.reply('Espero que não seja Nudes!')


@app.on_message((filters.photo | filters.video) & filters.group)
async def photo_or_video_group(client, message: Message):
    await message.reply('Quem não encherga não pode fotos, mande texto!')


@app.on_message()
async def hello(client, message: Message):
    print(message.chat.username,  message.text)
    await message.reply(message.text)


print('running!!!')
app.run()
