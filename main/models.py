from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class LandingData(models.Model):
    # шапка
    logo = models.FileField(verbose_name="Логотип", upload_to="static/img/uploads/header")
    menu_item1 = models.CharField(max_length=30, verbose_name="Пункт меню 1", default="Научим")
    menu_item2 = models.CharField(max_length=30, verbose_name="Пункт меню 2", default="Для кого курс")
    menu_item3 = models.CharField(max_length=30, verbose_name="Пункт меню 3", default="Что входит")
    menu_item4 = models.CharField(max_length=30, verbose_name="Пункт меню 4", default="Автор")
    button_cabinet = models.CharField(max_length=30, verbose_name="Название кнопки в шапке", default="Личный кабинет")
    link_button_cabinet = models.CharField(verbose_name="Ссылка кнопки в шапке", default="#", max_length=300)

    # блок 1
    h1_block1 = models.CharField(max_length=150, verbose_name="Заголовок h1", default="Доверьте ребёнку управлять "
                                                                                      "собственными деньгами")
    text_block1 = models.TextField(verbose_name="Текст",
                                   default="Мы создали \"Реальную школу\", чтобы обезопасить подростков от необдуманных "
                                           "финансовых поступков и дать успешные перспективы в будущем")
    button_1 = models.CharField(verbose_name="Кнопка 1", default="Записаться на курс", max_length=30)
    link_button_1 = models.CharField(verbose_name="Ссылка кнопки 1", default="#", max_length=300)
    button_2 = models.CharField(verbose_name="Кнопка 2", default="Попробовать бесплатно", max_length=30)
    link_button_2 = models.CharField(verbose_name="Ссылка кнопки 2", default="#", max_length=300)
    img_block1 = models.FileField(verbose_name="Картинка", upload_to="static/img/uploads/block1")

    # блок 2
    h2_block2 = models.CharField(max_length=150, verbose_name="Заголовок h2",
                                 default="Интерактивный курс по финансовой грамотности для детей и подростков")
    text1_block2 = models.TextField(verbose_name="Текст 1",
                                    default="С первого урока ученики вовлечены в практические упражнения, которые "
                                            "воспитывают в них")
    speech_cloud1 = models.CharField(verbose_name="Текст речевого облака 1", max_length=200,
                                     default="Креативность в поиске нестандартых ходов и решений")
    speech_cloud2 = models.CharField(verbose_name="Текст речевого облака 2", max_length=200,
                                     default="Ответственное отношение к деньгам ")
    speech_cloud3 = models.CharField(verbose_name="Текст речевого облака 3", max_length=200,
                                     default="Уважение и чувство ценности к труду")
    text2_block2 = models.TextField(verbose_name="Текст 2",
                                    default="Задача курса \"Простые финансы\" – не просто рассказать про деньги, "
                                            "а увлечь и дать возможность самостоятельно научится управлять деньгами и "
                                            "зарабатывать.")
    img_block2 = models.FileField(verbose_name="Картинка", upload_to="static/img/uploads/block2")

    # блок 3
    h2_block3 = models.CharField(max_length=150, verbose_name="Заголовок h2", default="Для кого этот курс?")
    h4_block3 = models.CharField(max_length=200, verbose_name="Подзаголовок (h4)",
                                 default="Этот курс идеально подходит для подростков 10 - 14 лет независимо "
                                         "от их финансовых навыков.")
    img_col1 = models.FileField(verbose_name="Картинка (колонка 1)", upload_to="static/img/uploads/block3")
    text_col1 = models.TextField(verbose_name="Текст колонки 1",
                                 default="Если они вообще не вникают в денежные дела семьи и не хотят брать на себя "
                                         "ответственность за личные накопления.")
    img_col2 = models.FileField(verbose_name="Картинка (колонка 2)", upload_to="static/img/uploads/block3")
    text_col2 = models.TextField(verbose_name="Текст колонки 2",
                                 default="Если они учатся сберегать средства, но ни вы, ни они не знают: а что можно "
                                         "сделать ещё, кроме как завести копилку?")
    img_col3 = models.FileField(verbose_name="Картинка (колонка 3)", upload_to="static/img/uploads/block3")
    text_col3 = models.TextField(verbose_name="Текст колонки 3",
                                 default="Если они хотят самостоятельно накопить на крупную покупку – или же это важно "
                                         "вам, чтобы они научились ценить дорогие вещи.")
    img_col4 = models.FileField(verbose_name="Картинка (колонка 4)", upload_to="static/img/uploads/block3")
    text_col4 = models.TextField(verbose_name="Текст колонки 4",
                                 default="И ещё если они активно интересуются – как и где уже сейчас могут заработать "
                                         "деньги, во что вложить и как грамотно распоряжаться финансами.")

    # блок 4
    text_block4 = models.TextField(max_length=150, verbose_name="Текст на голубом фоне",
                                   default="Чтобы мотивировать детей продолжать обучение, мы выстроили курс с учётом"
                                           "психологии подростков. А чего они хотят больше всего?")
    img_block4 = models.FileField(verbose_name="Картинка", upload_to="static/img/uploads/block4")

    # блок 5
    h3_block5 = models.CharField(max_length=250, verbose_name="Заголовок h3",
                                 default="Но при этом готовы прислушиваться к мнению авторитетных товарищей: "
                                         "кураторов и сокурскников в \"Чате миллионеров\".")
    button_block5 = models.CharField(verbose_name="Кнопка", default="Занять место на конкурсе", max_length=30)
    link_button_block5 = models.CharField(verbose_name="Ссылка кнопки", default="#", max_length=300)

    # блок 6
    h2_block6 = models.CharField(max_length=150, verbose_name="Заголовок h2", default="Курс \"Простые финансы\" – это")
    digit_col1 = models.IntegerField(verbose_name="Число 1", default=6)
    desc_col1 = models.TextField(verbose_name="Текст под числом колонки 1", max_length=120,
                                 default="недель интенсивных занятий")
    digit_col2 = models.IntegerField(verbose_name="Число 2", default=11)
    desc_col2 = models.TextField(verbose_name="Текст под числом колонки 2", max_length=120,
                                 default="уроков с заданиями в форме видеолекций и квестов")
    digit_col3 = models.IntegerField(verbose_name="Число 3", default=20)
    desc_col3 = models.TextField(verbose_name="Текст под числом колонки 3", max_length=120,
                                 default="минут среднее время прохождения урока")
    digit_col4 = models.IntegerField(verbose_name="Число 4", default=2)
    desc_col4 = models.TextField(verbose_name="Текст под числом колонки 4", max_length=120,
                                 default="онлайн-квеста в Zoom с кураторами и однокурсниками")

    # блок 7
    h2_block7 = models.CharField(max_length=150, verbose_name="Заголовок h2 в форме",
                                 default="Пройдите бесплатный урок")
    text_block7 = models.TextField(max_length=150, verbose_name="Текст в форме")

    class Meta:
        verbose_name = "Лэндинг"
        verbose_name_plural = "Данные по лэндингу"

    def __str__(self):
        return f"Контент лэндинга (вариант {self.id})"


class Subscribers(models.Model):
    first_last_name = models.CharField(max_length=50, verbose_name="Имя, фамилия")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.TextField(max_length=12, verbose_name="Телефон")

    def __str__(self):
        return self.first_last_name

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username