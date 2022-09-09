from django.contrib import admin

# Register your models here.
from .models import projectDatabase, assignmentDatabase, studentDatabase, submissionDatabase, evaluationDatabase

admin.site.register(projectDatabase)
admin.site.register(assignmentDatabase)
admin.site.register(studentDatabase)
admin.site.register(submissionDatabase)
admin.site.register(evaluationDatabase)
