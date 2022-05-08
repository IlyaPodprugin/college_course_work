from django.contrib import admin
from .models import *

admin.site.register(Quiz)
admin.site.register(QuizMeta)
admin.site.register(QuizAnswer)
admin.site.register(QuizLevel)
admin.site.register(QuizType)
admin.site.register(QuizQuestion)
admin.site.register(Take)
admin.site.register(TakeAnswer)
