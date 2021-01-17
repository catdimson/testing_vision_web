from django.db import models

# Create your models here.

class LandingData(models.Model):
    # блок 1
    # logo = models.ImageField()
    menu_item1 = models.CharField(max_length=30, verbose_name="Пункт меню 1", default="Научим")
    menu_item2 = models.CharField(max_length=30, verbose_name="Пункт меню 2", default="Для кого курс")
    menu_item3 = models.CharField(max_length=30, verbose_name="Пункт меню 3", default="Что входит")
    menu_item4 = models.CharField(max_length=30, verbose_name="Пункт меню 4", default="Автор")
    button_cabinet = models.CharField(max_length=30, verbose_name="Название кнопки в шапке")
    link_button_cabinet = models.CharField(verbose_name="Название кнопки в шапке", default="#", max_length=300)

    # h1_block1 = models.CharField(max_length=150, verbose_name="Заголовок h1 (блок 1)")
    text_block1 = models.TextField(verbose_name="Текст (блок 1)",
                                   default="Мы создали \"Реальную школу\", чтобы обезопасить подростков от необдуманных "
                                           "финансовых поступков и дать успешные перспективы в будущем")
    button_1 = models.CharField(verbose_name="Кнопка 1", default="Записаться на курс")
    link_button_1 = models.CharField(verbose_name="Ссылка кнопки 1", default="#", max_length=300)
    button_2 = models.CharField(verbose_name="Кнопка 2", default="Попробовать бесплатно")
    link_button_2 = models.CharField(verbose_name="Ссылка кнопки 2", default="#", max_length=300)
    # img_block1 = models.ImageField()

    # блок 2
    h2_block2 = models.CharField(max_length=150, verbose_name="Заголовок h2 (блок 2)")
    text1_block2 = models.TextField(verbose_name="Текст 1 (блок 2)",
                                    default="С первого урока ученики вовлечены в практические упражнения, которые "
                                            "воспитывают в них")
    speech_cloud1 = models.CharField(verbose_name="Текст речевого облака 1", max_length=200,
                                     default="Креативность в поиске нестандартых ходов и решений")
    speech_cloud2 = models.CharField(verbose_name="Текст речевого облака 2", max_length=200,
                                     default="Ответственное отношение к деньгам ")
    speech_cloud3 = models.CharField(verbose_name="Текст речевого облака 3", max_length=200,
                                     default="Уважение и чувство ценности к труду")
    text2_block2 = models.TextField(verbose_name="Текст 2 (блок 2)",
                                    default="Задача курса \"Простые финансы\" – не просто рассказать про деньги, "
                                            "а увлечь и дать возможность самостоятельно научится управлять деньгами и "
                                            "зарабатывать.")
    # img_block2 = models.ImageField()

    # блок 3
    h2_block3


    class Meta:
        verbose_name = "Лэндинг"
        verbose_name_plural = "Данные по лэндингу"


