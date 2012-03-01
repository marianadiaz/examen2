from django.contrib import admin
from main.models import Zombie, Tweet


class ZombieAdmin(admin.ModelAdmin):
	list_display = ('name', 'graveyard',)
	search_fields = ('name',)

class TweetAdmin(admin.ModelAdmin):
	list_display = ('status', 'created_at',)

admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Tweet, TweetAdmin)
