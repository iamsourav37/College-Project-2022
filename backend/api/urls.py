from django.urls import path, include
from rest_framework.authtoken import views as auth_view

from . import views


from django.urls import path, include
from rest_framework.authtoken import views
from .views import api_index

urlpatterns = [
    path('', api_index, name='api.home'),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    # path('payment/', include('api.payment.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),

]
