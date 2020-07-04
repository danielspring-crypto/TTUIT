from django.contrib import admin

# Register your models here.
from .models import *
import csv
import datetime
from django.http import HttpResponse

admin.site.site_header = 'TTU IT Department'
admin.site.index_title = 'Seminar Schedule'

def print_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;'\
        'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many\
    and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
print_csv.short_description = 'print_excel_file'

class SupervisorAdmin(admin.ModelAdmin):
	list_display = ['supervisor', 'supervisor_ph', 'supervisor_email', 'group']
	list_filter = ['group', 'supervisor']
	search_fields = ['supervisor',]
	actions = [print_csv]

class Seminar1Admin(admin.ModelAdmin):
	list_display = ['student_name', 'thesis_title', 'supervisor', 'student_roll', 'date', 'result']
	list_filter = ['supervisor', 'result', 'date']
	search_fields = ['student_name',]
	actions = [print_csv]

admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Seminar1, Seminar1Admin)












