import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router #обращаемся к router в файле handlers


async def main():
    bot = Bot(token='7836795086:AAENVFcrjQ3oBmIUeXSesI6XjkgCIV7gGmQ')  # тут ставится токен бота
    dp = Dispatcher()  # Диспетчер,обработчик запросов
    dp.include_router(router)   #говорим Dispatcher подключить router
    await dp.start_polling(bot)#обращение к серверу телеграмм с запросов обновлений от бота


if __name__ == '__main__':
    asyncio.run(main())     #запускает функцию main