from .views import home,signup,login, cart, checkout, orders, parul
from django.urls import path


urlpatterns = [
    path('',home.Index.as_view(), name='homepage'),
    path('signup',signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('cart', cart.Cart.as_view(), name='cart'),
    path('checkout', checkout.Checkout.as_view(), name='checkout'),
    path('orders', orders.OrderView.as_view(), name='orders'),
    path('parul', parul.Parul.as_view(), name='parul'),
]
