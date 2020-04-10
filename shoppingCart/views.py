from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from shoppingCart.models import Cart
from django.contrib.auth.models import User
from catalog.models import Book
from django.shortcuts import redirect
from .forms import CartAddForm
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404


@login_required()
def cart(request):
    form = CartAddForm()

    items = Cart.objects.filter(belong_to=request.user)
    item_count = 0
    total = 0

    for item in items:
        if item.number > item.item.stock:
            item.number = item.item.stock
            item.save()
        item_count += item.number
        total = total + item.get_cost()

    context = {
        'form': form,
        'items': items,
        'item_count': item_count,
        'total': total}

    return render(request, 'shoppingcart/cart.html', context)


def add_item_to_cart(request, item_id):
    number = 1

    if request.method == "GET":
        if request.user.is_authenticated:
            item = Book.objects.filter(id=item_id).first()
            cart = Cart.objects.filter(belong_to=request.user, item=item).first()
            if item.stock < 1:
                return redirect('catalogs:index')
            if cart:
                cart.number = cart.number + number
                cart.save()
            else:
                Cart(belong_to=request.user, item=item, number=number).save()

            return redirect('catalogs:index')
        else:
            return redirect('accounts:customer_login')

    if request.method == "POST":
        form = CartAddForm(request.POST)
        if form.is_valid():
            item = get_object_or_404(Book, id=item_id)
            cart = get_object_or_404(Cart, belong_to=request.user, item=item)

            if item.stock < form.cleaned_data['number']:
                error = "{} 庫存不足".format(item.title)
                return redirect('shoppingCars:cart')
            else:
                cart.number = form.cleaned_data['number']
                cart.save()
                return redirect('shoppingCars:cart')
        else:
            raise Http404


def remove_item_in_cart(request, item_id):
    if request.user.is_authenticated and request.method == "GET":
        cancel_target = Cart.objects.filter(belong_to=request.user, item=item_id)
        cancel_target.delete()
        return redirect('shoppingCars:cart')
    pass
