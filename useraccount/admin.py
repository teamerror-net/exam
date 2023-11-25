from django.contrib import admin
from useraccount.models import UserAccount
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class UserAccountAdmin(UserAdmin):
    search_fields = ('studentId','phone')

    list_display = ['first_name','last_name','dept','studentId', 'phone','date_joined','is_active']
    fieldsets = UserAdmin.fieldsets + (
            ('Account Summary', {'fields': ('profile_pic','studentId','dept','phone','auth_token',)}),
    )

    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('profile_pic','username', 'first_name', 'last_name','dept','studentId','email','phone', 'password1', 'password2'),
                },
            ),
        )
    ordering = ('-date_joined',)
    
admin.site.register(UserAccount,UserAccountAdmin)
admin.site.unregister(Group)