# from django.contrib import admin
#
# from .models import Account
#
# admin.site.register(Account)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django.utils.html import format_html

import decimal, csv
from django.http import HttpResponse
from django.db.models import F
# Register your models here.

def export_users(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name'])
    Account = queryset.values_list('email')
    for user in Account:
        writer.writerow(user)
    return response
export_users.short_description = 'Download Customer Details'


class AccountAdmin(UserAdmin):
    list_display = (
        'email', 'fname', 'lname', 'last_login', 'is_active', 'date_joined'
    )
    list_display_links = (
        'email', 'fname', 'lname',
    )
    readonly_fields = (
        'last_login', 'date_joined',
    )
    ordering = (
        '-date_joined',
    )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
