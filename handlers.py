from create import dp, users_dict, games_list_pvp
from aiogram import types
from random import randint
from keyboards import kb_start, kb_inline_start


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'\n\n{message.from_user.first_name}, добро пожаловать в игру с конфетами!', reply_markup=kb_start)
    await message.answer(f'Правила игры:\n\n \
    На столе лежит заданное количество конфет.\n \
    Играют два игрока делая ход друг после друга.\n \
    Первый ход за пользователем.\n \
    За один ход можно забрать не более чем 28 конфет.\n \
    Все конфеты достаются сделавшему последний ход', reply_markup=kb_inline_start)


@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Команды для игры:\n\n \
    /start - покажет правила игры\n \
    /set 100 - установит количество конфет равное 100')


@dp.message_handler(commands=['rules'])
async def mes_rules(message: types.Message):
    await message.answer('Как играть:\n\n \
    1) Для начала напишите команду /set 100 или /set "любое число"\n \
    2) Дальше можно просто писать число сообщением, чтобы указать сколько конфет хотите взять\n \
    3) Если захотите сыграть сначала, повторите все с первого пункта\n\n \
    Приятной игры!')


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    if users_dict.get(message.from_user.id, -1) != -1:
        del users_dict[message.from_user.id]
    
    total = int(message.text.split()[1])
    users_dict.setdefault(message.from_user.id, {'total': total})
    
    if total >= 100:
        await message.answer(f'Количество конфет = {total}')
    else:
        await message.answer('Можно задать число конфет только от 100')


@dp.message_handler()
async def mes_pve(message: types.Message):
    if message.text.isdigit():
        user_step = int(message.text.strip())
        
        if 0 < user_step <= 28 and users_dict[message.from_user.id]['total'] >= user_step:
            users_dict[message.from_user.id]['total'] -= user_step
            
            if users_dict[message.from_user.id]['total'] == 0:
                await message.answer(f'Поздравляем, {message.from_user.first_name}, ты забираешь все конфеты!')
                del users_dict[message.from_user.id]
            else:
                await message.answer(f'Осталось конфет {users_dict[message.from_user.id]["total"]}')
                bot_step = int(users_dict[message.from_user.id]['total'] % 29)
                
                if bot_step == 0:
                    bot_step += randint(1, 28)
            
                await message.answer(bot_step)
                users_dict[message.from_user.id]['total'] -= bot_step    

                await message.answer(f'Осталось конфет {users_dict[message.from_user.id]["total"]}')
                if users_dict[message.from_user.id]['total'] == 0:
                    await message.answer('Сожалеем, но бот вас переиграл!')
                    del users_dict[message.from_user.id]
                    
        else:
            await message.answer(f'Можно брать от 1 до 28 конфет за раз и не больше {users_dict[message.from_user.id]["total"]}')


# @dp.message_handler(commands=['pvp'])
# async def mes_pvp(message: types.Message):
#     if len(games_list_pvp) != 0:
#         if len(games_list_pvp[-1]) < 4:
#             games_list_pvp[-1].append(message.from_user.id)
#             games_list_pvp[-1].append(message.from_user.first_name)
#             games_list_pvp[-1].append(randint(100, 1000))
#             await message.answer(f'Ваш соперник - {games_list_pvp[-1][-2]}')
#         else:
#             games_list_pvp.append([message.from_user.id, message.from_user.first_name])
#             await message.answer('Ожидайте соперника🔎')
#     else:
#         games_list_pvp.append([message.from_user.id, message.from_user.first_name])
#         await message.answer('Ожидайте соперника🔎')


