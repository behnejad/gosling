from django.contrib import admin
from user import models
from user.hashmanager import makeHash
from django.contrib.messages import constants


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_create', 'request', 'is_activate', 'type')
    ording = ('first_name', 'last_name', 'date_create', 'email', 'isactive', 'type')
    search_fields = ('first_name', 'last_name', 'date_create', 'email', 'type', 'request')
    list_per_page = 15
    list_max_show_all = 30
    list_filter = (('is_activate', admin.BooleanFieldListFilter), 'type', 'request')
    list_editable = ('is_activate', 'type', 'request')
    list_display_links = ('email', )
    readonly_fields = ('key', )
    fieldsets = (
        ('Main Information', {
            'classes': ('wide', ),
            'fields': (('first_name', 'last_name'), 'type'),
        }
         ),
        ('Advanced options', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('email', 'key', 'password', 'date_create', 'is_activate', 'request')}
         ),
    )
    actions = ('delete_selected', 'activateUser', 'deActivateUser')
    
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.request = False
            obj.password = makeHash('md5', obj.password.encode("utf8"), obj.email.encode("utf8"))
        obj.save()

    def activateUser(self, request, queryset):
        queryset.update(is_activate=True)
        self.message_user(request, "%s Account(s) successfully activated." % queryset.count(), constants.SUCCESS)

    activateUser.short_description = "Active selected account(s)"

    def deActivateUser(self, request, queryset):
        queryset.update(is_activate=False)
        self.message_user(request, "%s Account(s) successfully deactivated." % queryset.count(), constants.WARNING)

    deActivateUser.short_description = "Deactivate selected account(s)"



@admin.register(models.group)
class GroupAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_max_show_all = 30
    search_fields = ('name', 'admin__last_name', 'admin__first_name')


@admin.register(models.prereg)
class registerAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_max_show_all = 30
    search_fields = ('mail', )
    list_display = ('mail', 'smash')


@admin.register(models.Reset)
class ResetAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_request', 'hash_code')
    list_per_page = 15
    list_max_show_all = 30

@admin.register(models.mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('email', 'hashId')
    list_per_page = 15
    list_max_show_all = 30
    
