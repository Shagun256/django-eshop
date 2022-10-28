from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)


    def register(self):
        self.save()

    def is_exists(self):
        return Customer.objects.filter(email=self.email)

    @staticmethod
    def get_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def __str__(self):
        return self.email