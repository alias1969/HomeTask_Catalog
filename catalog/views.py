from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category


def home(request):
    """Контроллер главной страницы"""
    products = Product.objects.all()
    return render(request, "products_list.html", context={"products": products})
    # return render(request, "home.html", context={'products':products})

def product_detail(request, pk):
    """Контроллер вывода карточки продукции"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", context={"product": product})


def product_input(request):
    """Контроллер ввода нового продукта"""
    # Получить от пользователя поля нового продукта и поместить их в словарь
    if request.method == "POST":
        product = {}
        product["name"] = request.POST.get("name")
        product["description"] = request.POST.get("description")
        product["price"] = request.POST.get("price")

        category_pk = request.POST.get("category")
        if category_pk is not None:
            product["category"] = Category.objects.get(pk=int(category_pk))

        # скачаем на сервер изображение и сохраним в media
        image = request.FILES.get("image")
        if image is not None:
           product['image'] = image

        # записывем данные в Product
        Product.objects.create(**product)

    categories = Category.objects.all()
    return render(request, "product_input.html", context={"categories": categories})


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
