from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(cartItem)
admin.site.register(Item)