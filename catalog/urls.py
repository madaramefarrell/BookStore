from django.urls import path
from . import views

app_name = "catalogs"

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>',
         views.book_detail,
         name='book_detail'),
    path('market/<str:market>',
         views.market_list,
         name='market'),
    path('contact',
         views.contact,
         name='contact'),
]
