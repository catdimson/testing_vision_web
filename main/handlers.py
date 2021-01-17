from django.core.mail import send_mail

from testing_vision_web.settings import EMAIL_HOST_USER, EMAIL_TO


def custom_send_mail(first_last_name, email, phone):
    send_mail(
        'Вам письмо!',
        f'Пришла заявка на бесплатные уроки с сайта. \n'
        f'Имя, фамилия: {first_last_name},\n'
        f'E-mail: {email},\n'
        f'Телефон: {phone}',
        EMAIL_HOST_USER,
        [EMAIL_TO],
    )
