from django.contrib import admin
from polls.models import Poll, Choice
from django.contrib.admin.options import ModelAdmin

class PollAdmin(admin.ModelAdmin):
    list_display = ['pk','question','pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk','poll','choice_text','votes']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)