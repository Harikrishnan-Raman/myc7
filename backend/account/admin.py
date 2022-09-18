from django.contrib import admin
from .models import User, assignmentDatabase, evaluationDatabase, marksSplitDatabase, marksDatabase

# Register your models here.
admin.site.register(User)

admin.site.register(marksSplitDatabase)
admin.site.register(marksDatabase)

admin.site.register(assignmentDatabase)
admin.site.register(evaluationDatabase)
