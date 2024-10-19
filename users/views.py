import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView, TemplateView

from users.forms import UserRegisterForms, UserProfileForm
from users.models import User
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    """Контроллер формы пользователя"""
    model = User
    form_class = UserRegisterForms
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
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
            recipient_list=[user.email],
        )

        return super().form_valid(form)


class UserProfileView(UpdateView):
    """Контроллер профиля пользователя"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """Передача объекта в UpdateView"""
        return self.request.user


class UserPasswordResetView(PasswordResetView):
    """Контроллер сброса пароля"""
    template_name = 'password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()
        if user is None:
            return redirect(reverse("users:invalid_email"))

        new_password = User.objects.make_random_password(length=8)
        user.password = make_password(new_password)
        user.is_active = True
        user.save()
        try:
            #отправляем новый пароль на почту пользователю
            send_mail(
                subject='Сброс пароля',
                message=f'Привет! Ваш новый пароль {new_password}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently = False,
            )

        except Exception as err:
            print(f'error: {err}')

        return redirect(reverse("users:login"))


class UserInValidEmail(TemplateView):
    """Контроллер отработки исключения, когда нет пользователя с таким email"""
    template_name = "invalid_email.html"


def email_verification(request, token):
    """Верификация пользователя"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    return redirect(reverse('users:login'))