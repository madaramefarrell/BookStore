from django.shortcuts import render
from .models import Book
from account.models import Market
from shoppingCart.models import Cart
from django.shortcuts import get_object_or_404, get_list_or_404
from shoppingCart.forms import CartAddForm
from django.contrib.auth import authenticate


def index(request):
    books = get_list_or_404(Book)

    item_count = 0
    total = 0
    items = None

    if request.user.is_authenticated:
        items = Cart.objects.filter(belong_to=request.user)

        for item in items:
            if item.number > item.item.stock:
                item.number = item.item.stock
                item.save()
            item_count = item_count + item.number
            total = total + item.get_cost()

    form = CartAddForm()
    context = {
        'url': request.path_info,
        'form': form,
        'username': request.user.username,
        'books': books,
        'items': items,
        'item_count': item_count,
        'total': total
    }

    return render(request, 'catalog/index.html', context)


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    form = CartAddForm()

    total = 0
    item_count = 0
    items = None

    if request.user.is_authenticated:
        items = Cart.objects.filter(belong_to=request.user)

        for item in items:
            if item.number > item.item.stock:
                item.number = item.item.stock
                item.save()
            item_count = item_count + item.number
            total = total + item.get_cost()

    context = {
        'username': request.user.username,
        'form': form,
        'book': book,
        'item': items,
        'item_count': item_count,
        'total': total,
    }

    return render(request, 'catalog/item_detail.html', context)


def market_list(request, market):
    total = 0
    item_count = 0

    if request.user.is_authenticated:
        items = Cart.objects.filter(belong_to=request.user)

    for item in items:
        if item.number > item.item.stock:
            item.number = item.item.stock
            item.save()
        item_count = item_count + item.number
        total = total + item.get_cost()

    market = Market.objects.filter(market_name=market).first()
    books = Book.objects.filter(market=market).all()

    context = {
        'item': items,
        'item_count': item_count,
        'total': total,
        'books': books,
        'market': market
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    total = 0
    item_count = 0
    items = None

    if request.user.is_authenticated:
        items = Cart.objects.filter(belong_to=request.user)

        for item in items:
            if item.number > item.item.stock:
                item.number = item.item.stock
                item.save()
            item_count = item_count + item.number
            total = total + item.get_cost()

    context = {
        'username': request.user.username,
        'item': items,
        'item_count': item_count,
        'total': total,
    }
    return render(request, 'catalog/contact.html', context)
