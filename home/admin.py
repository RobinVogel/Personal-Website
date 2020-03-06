from django.contrib import admin
from .models import News, Publications, Talks, Articles

# Register your models here.
admin.site.register(News)
admin.site.register(Publications)
admin.site.register(Talks)
admin.site.register(Articles)
