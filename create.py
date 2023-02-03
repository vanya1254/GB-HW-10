from aiogram import Bot, Dispatcher
from os import getenv
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot)
users_dict = dict()
games_list_pvp = []