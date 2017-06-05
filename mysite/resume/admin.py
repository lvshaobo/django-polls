from django.contrib import admin

# Register your models here.

from .models import BasicInformation, Award, Transcript

class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('basic_information', 'subject', 'score')


admin.site.register(BasicInformation)

admin.site.register(Award)

admin.site.register(Transcript, TranscriptAdmin)
