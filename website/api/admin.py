from django.contrib import admin
from .models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(Book, BookAdmin)