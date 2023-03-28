from aiogram import Bot, Dispatcher

TOKEN = "6041837935:AAEK1PEme5VxQRwBsEQg8hlAohzaHcJnvoQ"
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

def listen(array):

    for item in array:

        strings = item[0]

        function = item[1]

        commands = []

        words = []

        content_types=[]
        for string in strings:

            if string[0] == '/':
                commands.append(string[1:])

            elif string[0] == '-':
                content_types.append(string[1:])

            else:
                words.append(string)

        if commands != []:
            dp.register_message_handler(function, commands=commands)

        if words != []:
            dp.register_message_handler(function, text=words)

        if content_types != []:
            dp.register_message_handler(function, content_types=content_types)