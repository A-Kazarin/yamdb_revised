from django.contrib import admin
from .models import User, Reviews, Titles, Comments, Genres, Categories

# Register your models here.
admin.site.register(User)
admin.site.register(Reviews)
admin.site.register(Titles)
admin.site.register(Comments)
admin.site.register(Genres)
admin.site.register(Categories)