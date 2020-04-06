from django.shortcuts import render, redirect

from .forms import OrderCreateForm
from .models import OrderItem
from .task import order_created
from shoppingCart.models import Cart


def order_create(request):
    cart = Cart.objects.filter(belong_to=request.user)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item.item,
                                         price=item.item.price,
                                         quantity=item.number)
            # clear the cart
            cart.delete()
            order_created(order.id)
            request.session['order_id'] = order.id
            # redirect to the payment
            return redirect('payment:process')

    else:
        initial = {
        }
        form = OrderCreateForm()

    total = 0
    item_count = 0
    for item in cart:
        item_count += item.number
        total += item.get_cost()

    content = {
        'cart': cart,
        'form': form,
        'item_count': item_count,
        'total': total
    }

    return render(request, 'orders/create.html', content)
