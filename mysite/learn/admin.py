from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Person)
admin.site.register(Article)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)