from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.customer import Customer
from django.views import View

class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def post(self, request):
        error_message = None
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_by_email(email)

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email

                if email=="parulsharmaudh2001@gmail.com":
                    return redirect('parul')
                    
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'invalid email or password'
        else:
            error_message = 'invalid email or password'
        return render(request, 'login.html', {'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('homepage')