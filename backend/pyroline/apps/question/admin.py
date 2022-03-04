from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Question, Answer, QuestionPaper, QuestionSetter

# Register your models here.
admin.site.register(Question, SimpleHistoryAdmin)
admin.site.register(Answer, SimpleHistoryAdmin)
admin.site.register(QuestionPaper, SimpleHistoryAdmin)
admin.site.register(QuestionSetter, SimpleHistoryAdmin)
