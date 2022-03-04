from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import Program, Subject, Chapter, ChapterSet, Topic, Description

admin.site.register(Program, SimpleHistoryAdmin)
admin.site.register(Subject, SimpleHistoryAdmin)
admin.site.register(Chapter, SimpleHistoryAdmin)
admin.site.register(ChapterSet, SimpleHistoryAdmin)
admin.site.register(Topic, SimpleHistoryAdmin)
admin.site.register(Description, SimpleHistoryAdmin)
