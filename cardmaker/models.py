from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Deck(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('create_cards', kwargs={'deck_id' : self.id})


class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class StudySet(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")


class StudentDeck(models.Model):
    studyset = models.ForeignKey(StudySet, on_delete=models.CASCADE, related_name="studyset")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)


class Marks(models.Model):
    score = models.FloatField(max_length=5)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)