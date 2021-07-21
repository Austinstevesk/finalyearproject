from django.contrib import admin
from .models import Post
from Consumers.models import Consumer

# Register your models here.
admin.site.register(Post)
admin.site.register(Consumer)

