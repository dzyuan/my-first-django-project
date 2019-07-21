from django.contrib import admin
from .models import Todolist,project,branch

# Register your models here.



class projectAdmin(admin.ModelAdmin):
    list_display = ('id','projectid', 'projectname', 'applicant_branch','leader','totalbudget','start_date','complete_date',)


admin.site.register(Todolist)
admin.site.register(project,projectAdmin)
admin.site.register(branch)