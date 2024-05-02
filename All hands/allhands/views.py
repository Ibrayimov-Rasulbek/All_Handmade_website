from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views import View
from .models import Mahsulot


class HomePageView(View):
    def get(self,request):
        pic=Mahsulot.objects.all()[:4]
        products=Mahsulot.objects.all()[:8]
        return render(request,'index.html',{'pic':pic,'products':products})
    
class AllProductsView(View):
    def get(self,request):
        products=Mahsulot.objects.all()
        return render(request,'all_products.html',{'products':products})

class AboutView(View):
    def get(self,request):
        return render(request,'AboutUs.html')
class ContactView(View):
    def get(self,request):
        return render(request,'Contact_Us.html')