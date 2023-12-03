from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, Text, PhotoMessageUploader
from download_photo import download



token = "TOKEN"
bot = Bot(token)

photo_uploader = PhotoMessageUploader(bot.api)

waiting_for_photo = {}
photo_path = r'/home/vk_bot/photo'

@bot.on.private_message(text=['Да', 'да', "дА",'ДА',"хорошо", "Хорошо", "Хочу", "хочу", '/start', "Начать", 'start'])
async def handler(message: Message):
    user_id = message.from_id
    response_message = "Привет, давай проверим твою ауру. ✨"
 
    waiting_for_photo[user_id] = False

    keyboard = (
        Keyboard()
        .add(Text("Проверить ауру 🔮"))
        .get_json()
    )

    await message.answer(message=response_message, keyboard=keyboard)

@bot.on.private_message(text="Проверить ауру 🔮")
async def check_aura(message: Message):
    user_id = message.from_id
    response_message = "Пришлите фото на котором находитесь вы, для того что бы проверить ауру 🌑 "
    
    waiting_for_photo[user_id] = True

    await message.answer(message=response_message, keyboard=Keyboard(one_time=True).get_json())


@bot.on.private_message()
async def handle_message(message: Message):
    try:
        res_d = download(message.attachments[0].photo.sizes[-5].url) 

        photo, text = res_d
        await message.answer(message="Уже смотрим Вашу ауру... 🤔" )
        try:
            photo = await photo_uploader.upload(file_source=res_d[0])
            await message.answer(attachment=photo)
            await message.answer(message=text)
        except:
            await message.answer(message=res_d)


    except:
        keyboard = (
            Keyboard()
            .add(Text("Проверить ауру 🔮"))
            .get_json()
            )
        
        response_message = "Давай проверим твою ауру ✨"

        await message.answer(message=response_message, keyboard=keyboard)




if __name__ == '__main__':
    bot.run_forever()

