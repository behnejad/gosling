from django.contrib import admin
from user import models
from user.hashmanager import HashManager
from django.contrib.messages import constants


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'datecreate', 'request', 'isactivate', 'type')
    ording = ('first_name', 'last_name', 'datecreate', 'email', 'isactive', 'type')
    search_fields = ('first_name', 'last_name', 'datecreate', 'email', 'type', 'request', 'username')
    list_per_page = 15
    list_max_show_all = 30
    list_filter = (('isactivate', admin.BooleanFieldListFilter), 'type', 'request', 'college')
    list_editable = ('isactivate', 'type', 'request')
    list_display_links = ('username', )
    readonly_fields = ('key', )
    fieldsets = (
        ('Main Information', {
            'classes': ('wide', ),
            'fields': (('first_name', 'last_name'), 'username', 'college', 'type'),
        }
         ),
        ('Advanced options', {
            'classes': ('wide', 'extrapretty'),  # 'collapse',
            'fields': ('email', 'key', 'password', 'datecreate', 'isactivate', 'request')}
         ),
    )
    actions = ('delete_selected', 'activateUser', 'deActivateUser')
    
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.request = False
            hm = HashManager('md5')
            obj.password = hm.makeHash(obj.password, obj.username)
        obj.save()

    def activateUser(self, request, queryset):
        queryset.update(isactivate=True)
        self.message_user(request, "%s Account(s) successfully activated." % queryset.count(), constants.SUCCESS)

    activateUser.short_description = "Active selected account(s)"

    def deActivateUser(self, request, queryset):
        queryset.update(isactivate=False)
        self.message_user(request, "%s Account(s) successfully deactivated." % queryset.count(), constants.WARNING)

    deActivateUser.short_description = "Deactivate selected account(s)"

