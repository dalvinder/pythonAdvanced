from django.contrib import admin
from polls.models import Poll, Choice
from django.contrib.admin.options import ModelAdmin

class ChoiceInline(admin.StackedInline):
    model = Choice
    extras=0
    
class PollAdmin(admin.ModelAdmin):
    list_display = ['pk','question','pub_date','last_updated','audience']
    fieldsets = [
            (None,{'fields':['question']}),
            ('Display Controls',{
                        'fields':['audience','frequency'],
                        'classes':['collapse']      
                    })
        ]
    inlines = [ChoiceInline]
    list_filter=['audience']
    search_fields=['question','audience']
    date_hierarchy='pub_date'
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk','poll','choice_text','votes']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)