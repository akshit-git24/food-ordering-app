from django.contrib import admin
from .models import RegularUserProfile,StaffProfile
# Register your models here.
admin.site.register(StaffProfile)
admin.site.register(RegularUserProfile)
