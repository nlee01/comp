from django.contrib import admin

# Register your models here.
from .models import Content, Article, Contributor

class ContentAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, { 'fields': ['title']}),
		(None, { 'fields': ['subtitle']}),
		(None, { 'fields': ['pub_date']}),
		('Contributors', { 'fields': ['contributors'], 'classes': ['collapse']}),
	]
	list_display = ('title', 'subtitle', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['title', 'subtitle']

admin.site.register(Content, ContentAdmin)
admin.site.register(Article)
admin.site.register(Contributor)