from django.contrib import admin
from exam import models
from user.hashmanager import makeHash

@admin.register(models.field)
class fieldAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.section)
class sectionAdmin(admin.ModelAdmin):
    list_display = ('fname', 'name')


@admin.register(models.problem)
class problemAdmin(admin.ModelAdmin):
    list_display = ('sec', )


