from django.contrib import admin
from .models import notification, sender, recepient

admin.site.register(notification)
admin.site.register(sender)
admin.site.register(recepient)
