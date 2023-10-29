from django.contrib import admin
from dapp.models import denal,c_denal,email
  
# Register your models here.
class denalAdmin(admin.ModelAdmin):
	list_display = ['p_name','p_email','p_date','p_time']
admin.site.register(denal,denalAdmin)


class denalAdmincontact(admin.ModelAdmin):
	list_display = ['c_name','c_email','c_subject','c_message']
admin.site.register(c_denal,denalAdmincontact)


class emailAdmin(admin.ModelAdmin):
	list_display = ['email']
admin.site.register(email,emailAdmin)