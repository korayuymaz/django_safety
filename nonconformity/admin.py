from django.contrib import admin
from .models import Nonconformity
from .models import Employee

admin.site.register(Employee)
admin.site.register(Nonconformity)
# Register your models here.
