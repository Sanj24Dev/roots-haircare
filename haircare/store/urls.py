from django.contrib import admin
from django.urls import path
from .views.home import Index , store, about
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.quiz import quiz
from .views.result import IndexR, result


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('haircare', about, name='about'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),

    path('quiz', quiz, name='quiz'),
    path('res', IndexR.as_view(), name='res'),
    path('result', result, name='result'),

    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
