from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, TemplateView


def home(request):
    """Домашняя страница"""
    return render(request, "home.html")


def contacts(request):
    """Страница контактов"""
    # Получить от пользователя его данные для обратной связи
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(
            f""" Данные для обратной связи:
        Имя: {name}, 
        Телефон: {phone}, 
        Доп. информация: {message}
        """
        )

    return render(request, "contacts.html")


class ProductListView(ListView):
    """ Класс контроллер для вывода продуктов на главной странице"""
    model = Product
    template_name = 'product/products.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['products'] = Product.objects.all()[:5]
        return context


class ContactsTemplateView(TemplateView):
    """Класс-контроллер для вывода страницы с контактами"""
    template_name = 'contacts.html'
