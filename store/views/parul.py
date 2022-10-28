from django.shortcuts import render
from store.models.product import Product
from django.views import View

class Parul(View):
    def get(self, request):
        return render(request, 'parul.html')
 