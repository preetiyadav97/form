from django.contrib import admin
from .models import Employee_detail

# Register your models here.
class Employee_detailAdmin(admin.ModelAdmin):
    model=Employee_detail
    list_display=['firstname','secondname','email','phone','state','city','skills','experience','reference','file','address']
admin.site.register(Employee_detail,Employee_detailAdmin)