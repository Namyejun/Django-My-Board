from django.contrib import admin

# Register your models here.
from .models import Board
class BoardAdmin(admin.ModelAdmin):
    list_display= ("title", "writer", "created_at")

admin.site.register(Board, BoardAdmin)