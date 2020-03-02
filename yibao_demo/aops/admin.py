from django.contrib import admin

# Register your models here.

from .models import EmployeeUser, Organization, GroupMember


@admin.register(EmployeeUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ['empno', 'name']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']

@admin.register(GroupMember)
class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ['employee_user', 'group']