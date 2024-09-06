from django.shortcuts import render


def home(request):
    """ Домашняя страница"""
    return render(request, 'home.html')


def contacts(request):
    """ Страница контактов """
    # Получить от пользователя его данные для обратной связи
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f""" Данные для обратной связи:
        Имя: {name}, 
        Телефон: {phone}, 
        Доп. информация: {message}
        """)

    return render(request, 'contacts.html')



