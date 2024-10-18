import secrets

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForms
from users.models import User
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    """Контроллер формы пользователя"""
    model = User
    form_class = UserRegisterForms
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        print(user)
        user.is_active = False

        #генерация токена юзера
        token = secrets.token_hex(16)
        user.token = token
        user.save()

        #ссылка для перехода
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'

        #отправка сообщения
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Для подтверждения почты перейти по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_valid(form)


class UserLoginView():
    model = User


def email_verification(request, token):
    """Верификация пользователя"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    return redirect(reverse('users:login'))