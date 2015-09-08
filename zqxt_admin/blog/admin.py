from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Person
 
 
# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
 
admin.site.register(Article,ArticleAdmin)

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_name',)

admin.site.register(Person,PersonAdmin)
