from django.contrib import admin
from .models import User, Qualification, Department, Year, Room, Group, ProfileStudent
from event.models import Event, ApplyEvent, EventParticipation
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['year']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['qualification', 'department', 'year', 'room']

# inline
class ApplyEventInline(admin.TabularInline):
    model = ApplyEvent
    extra = 0

@admin.register(ProfileStudent)
class ProfileStudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name','last_name','student_id', 'group',]
    # inlines = [ApplyEventInline]