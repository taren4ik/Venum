from django.db import models

# Наша "База данных"

chats_db = {
        'Протестная Рооссия': 'https://t.me/RussianOppositionRu1',
        'Владивосток активный. Чат' : 'https://t.me/vdkzakhv',
    }

class Serch_Person(models.Model):
    name = models.CharField("Имя", max_length = 20)
    last_name = models.CharField("Фамилия", max_length = 20)
    discription = models.TextField("Описание", max_length = 300)
    id_telegram = models.IntegerField("ID_telegram")
    def __str__(self):
        return  self.name
