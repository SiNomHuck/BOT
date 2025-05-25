from aiogram import F,Router
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile
import app.Keyboard as kb



router=Router()#переменная router которой присваивается класс Router

@router.message(CommandStart())#Дает знак отправлять сообщения по команде /start
async def cmd_start(message: Message):
    await message.answer('Добрый день!Тут вы узнаете все о нашей компании и получите инструмент для лидов',reply_markup=kb.catalog)    #Бот отвечает на отправленное сообщение




@router.message(Command('help'))        #Вывод сообщение через команду help
async def cmd_help(message: Message):
    await message.answer('Вы вызвали команду помощи')


@router.message(F.text=='Каталог')        #Вывод сообщение через определенный текст указанный в F.text
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catalog)


@router.callback_query(F.data=='t-shirt')
async def t_shirt(callback:CallbackQuery):
    await callback.message.answer('Вы выбрали категорию футболок.')