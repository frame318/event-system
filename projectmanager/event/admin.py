from django.contrib import admin
from .models import Event, ApplyEvent, EventParticipation
# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'start_date'
    ordering = ['start_date']
    # list_editable = ['credit']
    list_per_page = 10
    list_max_show_all = 100

class EventParticipationInline(admin.TabularInline):
    model = EventParticipation
    extra = 0

@admin.register(ApplyEvent)
class ApplyEventAdmin(admin.ModelAdmin):
    list_display = ['event', 'student', 'date']
    inlines = [EventParticipationInline]
    list_filter = ['date']
    search_fields = ['event', 'student']
    date_hierarchy = 'date'
    ordering = ['date']
    list_per_page = 10
    list_max_show_all = 100


@admin.register(EventParticipation)
class EventParticipationAdmin(admin.ModelAdmin):
    list_display = ['apply_event', 'date', 'checkin']
    list_filter = ['date']
    search_fields = ['apply_event']
    date_hierarchy = 'date'
    ordering = ['date']
    list_per_page = 10
    list_max_show_all = 100