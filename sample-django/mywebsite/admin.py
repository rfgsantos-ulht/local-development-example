from django.contrib import admin

# Register your models here.
from mywebsite.models import Post

admin.site.site_url = "/djangoapp"
admin.site.register(Post)
