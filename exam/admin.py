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


@admin.register(models.exam)
class examAdmin(admin.ModelAdmin):
    list_display = ('startdate', 'enddate', 'name', )
    search_fields = ('startdate', 'enddate', 'name', )
    list_per_page = 15
    list_max_show_all = 30
    
@admin.register(models.examproblems)
class examproblemsAdmin(admin.ModelAdmin):
    list_display = ('examid', 'problemid', )
    search_fields = ('examid', 'problemid', )
    list_per_page = 15
    list_max_show_all = 30
    

@admin.register(models.useranswers)
class useranswers(models.Model):
    list_display = ('examid', 'problemid', 'userid', 'answer', )
    search_fields = ('examid', 'problemid', 'userid', )
    list_per_page = 15
    list_max_show_all = 30
    
