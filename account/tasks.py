from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings


def save_otp_to_cache(email: str, otp: int) -> bool:
    key_code = email
    data = {"otp": otp}
    if cache.get(key_code) is None:
        data.__setitem__('count', 1)
        cache.set(key_code, data, 5 * 60)
    else:
        old_cache = cache.get(key_code)
        count = old_cache.get('count')
        if count > 5:
           print(f'ERROR: OTP count for user {email} more than 5pc!!!')
           return False
        else:
            cache.delete(email)
            data.__setitem__('count', count+1)
            cache.set(key_code, data, 5 * 60)

    return True

@shared_task
def send_otp_email(email: str, title: str, msg: str, otp: int):
    if save_otp_to_cache(email, otp):
        send_mail(title, msg, settings.EMAIL_HOST_USER, [email])
    elif not save_otp_to_cache(email, otp):
        send_mail('ERROR from django-back',
                  'Your OTP not send, cause sent before more than 5pc',
                  settings.EMAIL_HOST_USER,
                  [email])

