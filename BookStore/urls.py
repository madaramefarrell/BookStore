from django.contrib import admin
from django.urls import path, include
# from . import settings
from django.conf import settings

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('account/', include('account.urls')),
                  path('social-auth/',
                       include('social_django.urls', namespace='social')),
                  path('', include('catalog.urls')),
                  path('cart/', include('shoppingCart.urls')),
                  path('paypal/', include('paypal.standard.ipn.urls')),
                  path('orders/', include('orders.urls', namespace='orders')),
                  path('payment/', include('payment.urls', namespace='payment')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
