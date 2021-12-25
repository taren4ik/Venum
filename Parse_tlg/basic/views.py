from asgiref.sync import sync_to_async
from django.shortcuts import render
from .models import chats_db
from .services import find_song


def index(request):
    chats = ''
    selected_chats = ''
    id_output = ''
    song = ''

    # for i in range(len(chats_db)):
    #     chats +=(f'<input type="radio" name="chats"'
    #                 f' required value="{chats_db[i]["name"]}">{chats_db[i]["name"]}<br>')

    for chat in chats_db:
        # Около каждого имени вставляется radio button,
        # и теперь в форме кликом по кнопочке можно будет выбрать одного из друзей.
        chats += (f'<input type="radio" name="name"'
                  f' required value="{chat}"> {chat}<br>')

    if request.method == 'POST':
        # Извлекли из запроса название чата
        selected_chats = request.POST['name']
        # Извлечение ссылки
        hypertext = chats_db[selected_chats]
        #id_output = x2(hypertext)

        #id_output = x2(hypertext)
        # Вместо слова "мороженое" выведите название сорта из запроса.
        # friend_output = f'{selected_friend}, тебе прислали {selected_icecream}!'
        # city_weather = f'В городе {city} погода: {weather}'
        # weather = what_weather('perm')
        song = find_song()
    context = {
        'chats': chats,
        # 'weather': weather,
        'song': song,
        #'id_output': id_output,
    }
    return render(request, 'basic/index.html', context)


def about(request):
    return render(request, 'basic/about.html')


def contact(request):
    return render(request, 'basic/contact.html')


def calendar(request):
    return render(request, 'basic/calendar.html')
