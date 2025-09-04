from django.contrib import admin

# Register your models here.
from home.models import Feedback,Applicant

admin.site.register(Feedback)
admin.site.register(Applicant)