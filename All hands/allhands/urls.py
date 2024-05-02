from django.urls import path
from .views import HomePageView,AllProductsView,AboutView,ContactView



urlpatterns=[
    path('', HomePageView.as_view(), name="home"),
    path('allproducts/',AllProductsView.as_view(),name='allproducts'),
    path('handcrafted_candles/',AboutView.as_view(),name='handcrafted_candles'),
    path('contactus/',ContactView.as_view(),name='contact')
]