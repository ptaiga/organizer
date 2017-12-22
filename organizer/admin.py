from django.contrib import admin

from .models import Project, Task

class TaskInline(admin.TabularInline):
    model = Task
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_name']}),
        ('Date information', {'fields': ['pub_date'],
                                    'classes': ['collapse']}),
    ]
    inlines = [TaskInline]
    list_display = ['project_name', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['project_name']

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['task_name']}),
        ('Date information', {'fields': ['pub_date'],
                                    'classes': ['collapse']}),
    ]
    list_display = ['task_name', 'pub_date', 'project', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['task_name']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)