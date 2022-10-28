from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')

        # validation 
        data = {}
        error_message = None

        value={
                'first_name':first_name,
                'last_name': last_name,
                'phone':phone,
                'email':email
            }

        customer=Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password
                            )

        error_message = self.validate(customer)
        
        #saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data={'values':value,
                  'error':error_message}
            return render(request, 'signup.html',data)

    def validate(self, customer):
        error_message=None
        if not customer.first_name:
            error_message='First name is required !!'
        elif len(customer.first_name)<4:
            error_message='First name must be 4 char long!!'

        elif not customer.last_name:
            error_message='last name is required !!'
        elif len(customer.last_name)<4:
            error_message='Last name must be 4 char long!!'

        elif not customer.phone:
            error_message='Phone number required !!'
        elif len(customer.phone)<10:
            error_message='Phone number must be 10 char long!!'
 
        elif len(customer.password)<6:
            error_message='Password must be 6 char long!!'

        elif len(customer.email)<5:
            error_message='Email must be 5 char long!!'
        
        elif customer.is_exists():
            error_message='Email already registered'
        return error_message
