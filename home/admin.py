from django.contrib import admin

# Register your models here.
from home.models import Contact,Applicant

admin.site.register(Contact)
admin.site.register(Applicant)