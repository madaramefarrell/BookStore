from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import MyUserCreationForm, CustomerUserForm, VendorUserForm, forgetPasswordForm
from shoppingCart.models import Cart
from catalog.models import Book
from django.contrib.auth.models import User
from .task import forgetPassword


def customer_register(request):
    books = get_list_or_404(Book)

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

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        customerform = CustomerUserForm(request.POST)

        if form.is_valid() and customerform.is_valid():
            user = form.save()

            customer = customerform.save(commit=False)
            customer.user = user
            customer.save()

            account = form.cleaned_data.get('account')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=account, password=password)
            login(request, user)

            return redirect('accounts:index')
    else:
        form = MyUserCreationForm()
        customerform = CustomerUserForm()

    context = {'form': form,
               'CustomerUserForm': customerform,
               'url': request.path,
               'username': request.user.username,
               'books': books,
               'items': items,
               'item_count': item_count,
               'total': total
               }

    return render(request, 'account/register.html', context)


def vendor_register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        customerform = VendorUserForm(request.POST)

        if form.is_valid() and customerform.is_valid():
            user = form.save()

            vendor = customerform.save(commit=False)
            vendor.user = user
            vendor.save()

            account = form.cleaned_data.get('account')
            password = form.cleaned_data.get('password')
            user = authenticate(username=account, password=password)
            login(request, user)

            return redirect('accounts:index')
    else:
        form = MyUserCreationForm()
        customerform = VendorUserForm()

    context = {'form': form, 'CustomerUserForm': customerform}
    return render(request, 'account/register_vendor.html', context)


@login_required()
def ChangePersonalInfo(request):
    if request.method == 'POST':
        form = ChangePersonalInfo(request.POST)
        customerform = CustomerUserForm(request.POST)

        if form.is_valid() and customerform.is_valid():
            # user = form.save(commit=False)

            # customer = customerform.save(commit=False)
            # customer.user = user
            user = form.save()
            customer = customerform.save()
            customer.save()

            return redirect('accounts:index')
    else:
        form = MyUserCreationForm()
        customerform = CustomerUserForm()

    context = {
        'form': form,
        'CustomerUserForm': customerform
    }
    return render(request, 'account/change_personal_info.html', context)


def forget_password(request):
    error = None
    res = None
    if request.method == "POST":
        form = forgetPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data.get('email')).first()
            print(form.cleaned_data.get('email'))
            print(user)
            if user:
                res = forgetPassword(email=user.email, name=user.username)
            else:
                error = 'This Email doesn\'t register'
    else:
        form = forgetPasswordForm()

    context = {'form': form, 'error': error, 'res': res}

    return render(request, 'account/forget_password.html', context)
