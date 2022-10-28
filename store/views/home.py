from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View

class Index(View):
    def get(self, request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart=dict()
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            product = Product.get_all_products_by_categoryid(category_id)
        else:
            product = Product.get_all_products()
        data = {}
        data['products']=product
        data['categories']=categories
        print('you are: ',request.session.get('email'))
        return render(request, 'index.html',data)

    def post(self, request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                # print('this is qunatity: ', quantity)
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                    # print('this is cart in remove: ',cart)
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1 
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print('cart: ',request.session['cart'])
        return redirect('homepage')
 