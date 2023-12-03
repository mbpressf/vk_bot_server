import requests
from photo_filter import main_func
from os import remove

path = r'/home/vk_bot/photo/image.jpg'

def download(url):

    response = requests.get(url)

    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content) 
        txt = main_func(img=path)
        
        remove(path)
        return r'filter_img.jpg', txt
    else:
        return "Ой извините, что-то нет так, думаю аура требует повторной проверки 🙄"
