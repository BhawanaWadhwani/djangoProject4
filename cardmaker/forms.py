from cardmaker.models import Card, Deck
from django.forms import ModelForm, Textarea, inlineformset_factory, TextInput
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView

# Create the form class.
class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('question', 'answer', 'deck')


class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ('title', 'subject', 'description')
        widgets = {'title':
            TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Title",
            }),
            'subject':
                TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': "Subject e.g. ASD",
                }),
            'description':
                Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': "Description e.g. Agile Software Development, chapter 1-12",
                }),
        }


CardFormSet = inlineformset_factory(
    Deck, Card,
    fields=('question', 'answer'),
    can_delete=False,
    extra=1,
    widgets={
        'question': TextInput(attrs={"class": "form-control form-control-lg",
                                     "placeholder": "Question", }),
        'answer': TextInput(attrs={"class": "form-control",
                                   "placeholder": "Answer"}),

    }

)
