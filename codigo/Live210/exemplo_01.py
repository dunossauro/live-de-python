from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
)

load_dotenv()

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
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_2'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 1'
        },
        'page_3': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='data'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_2'),
            'texto': 'Você está na página 3'
        },
        'page_2': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_3'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 2'
        }
    }
    page = pages[callback_query.data]
    await callback_query.edit_message_text(
        page['texto'],
        reply_markup=InlineKeyboardMarkup([[page['anterior'], page['proximo']]])
    )


@app.on_message(filters.command('inline'))
async def teclado(client, message):
    botoes = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Callback', callback_data='data'),
                InlineKeyboardButton(
                    'Link',
                    url='https://docs.pyrogram.org/api/methods/#messages'
                )
            ]
        ]
    )
    await message.reply(
        'Aperta aí no teclado',
        reply_markup=botoes
    )

@app.on_message(filters.command('teclado'))
async def teclado(client, message):
    teclado = ReplyKeyboardMarkup(
        [
            ['/ajuda', '/xpto'],
            ['a', 'b', 'c']
        ],
        resize_keyboard=True
    )
    await message.reply(
        'Aperta aí no teclado',
        reply_markup=teclado,
    )
    

@app.on_message(filters.command('photo'))
async def photo(client, message):
    await app.send_photo(
        message.chat.id,
        'https://images.pexels.com/photos/12641780/pexels-photo-12641780.jpeg?cs=srgb&dl=pexels-stayhereforu-12641780.jpg&fm=jpg'
    )

@app.on_message(filters.sticker)
async def sticker(client, message):
    await app.send_sticker(
        message.chat.id,
        message.sticker.file_id
    )
    

@app.on_message(filters.voice | filters.audio)
async def voice_audio(client, message):
    await message.reply(
        'Ah, já vai começar o podcast'
    )

@app.on_message(filters.photo | filters.video)
async def photo_video(client, message):
    await message.reply(
        'Espero que não seja **nudes**!'
    )

@app.on_message(filters.command('help'))
async def ajuda(client, message):
    print(message.chat.username, message.text)
    await message.reply(
        'Essa é uma mensagem de ajuda!'
    )

@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '???')


print('Rodando!!')
app.run()
