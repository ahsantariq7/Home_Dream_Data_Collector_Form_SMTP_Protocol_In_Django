from django.contrib import admin
from .models import Gender,Married_opt,Education_level,Property,Province,Job_Type,Home_Dream
# Register your models here.
admin.site.register(Gender)
admin.site.register(Married_opt)
admin.site.register(Education_level)
admin.site.register(Property)
admin.site.register(Province)
admin.site.register(Job_Type)
admin.site.register(Home_Dream)