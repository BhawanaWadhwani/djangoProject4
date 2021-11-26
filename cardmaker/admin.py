from django.contrib import admin

# Register your models here.
from .models import Deck, Card, StudySet, StudentDeck, Post, Replie


class DeckAdmin(admin.ModelAdmin):
    fields = ['title', 'subject', 'creator', 'description']


class CardAdmin(admin.ModelAdmin):
    fields = ['question', 'answer', 'deck']


class StudySetAdmin(admin.ModelAdmin):
    fields = ['student']


class StudentDeckAdmin(admin.ModelAdmin):
    fields = ['studyset', 'student', 'deck']


admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(StudySet, StudySetAdmin)
admin.site.register(StudentDeck, StudentDeckAdmin)
admin.site.register(Post)
admin.site.register(Replie)
