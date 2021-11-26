# Create your views here.
from django.shortcuts import render
from cardmaker.models import Card, Deck, StudySet, StudentDeck, Marks, Post, Replie
from cardmaker.forms import CardForm, DeckForm, CardFormSet
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


# Create your views here.

def show_my_decks(request):
    d_list = Deck.objects.all()
    context = {'list_of_decks': d_list}
    return render(request, 'show_my_decks.html', context)

# git ka comment hai

def delete_card(request, deck_id, card_id):
    card_to_delete = Card.objects.get(id=card_id)
    card_to_delete.delete()
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards': c_list, 'deck': deck}
    return render(request, 'show_deck.html', context)


def show_deck(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards' : c_list, 'deck': deck}
    return render(request, 'show_deck.html', context)


def show_all_decks(request):
    d_list = Deck.objects.all()
    context = {'list_of_decks': d_list}
    if request.method == "POST":
        query_name = request.POST.get('search1', None)
        # if we have searched for something the list will be altered accordingly
        if query_name is not None:
            d_list2 = Deck.objects.filter(title__contains=query_name)
            context = {'list_of_decks': d_list2}
            return render(request, 'show_all_decks.html', context)
    else:
        return render(request, 'show_all_decks.html', context)


def delete_deck(request, deck_id):
    deck_to_delete = Deck.objects.get(id=deck_id)
    deck_to_delete.delete()
    return redirect('my_decks')


class DeckCreate(CreateView): #using a generic view
    form_class = DeckForm
    model = Deck

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creator = self.request.user
        f.save()
        return super().form_valid(form)


def create_cards(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    if request.method == 'POST':
        formset = CardFormSet(request.POST, instance = deck)
        if formset.is_valid():
            formset.save()
            return redirect('create_cards', deck_id)

    formset = CardFormSet(instance=deck)
    return render(request, 'create_cards.html', {'formset':formset, 'deck': deck})


def rehearse_deck(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards' : c_list}
    return render(request, 'rehearse_deck.html', context)


def save_for_study(request, deck_id):
    user = request.user #logged in user
    deck = Deck.objects.get(pk=deck_id)
    studyset , created = StudySet.objects.get_or_create(student=user)
    if not StudentDeck.objects.filter(deck=deck, student=user):
        s = StudentDeck()
        s.studyset = studyset
        s.student = user
        s.deck = deck
        s.save()
    else:
        pass
    return redirect('show_my_studyset')


def show_my_studyset(request):
    try:
        studyset = StudySet.objects.get(student_id=request.user.id)
        deck_list = StudentDeck.objects.filter(studyset_id=studyset.id)
        context = {'studyset':studyset, 'deck_list': deck_list}
    except StudySet.DoesNotExist:
        context = None
    return render(request, 'my_studyset.html', context)


def remove_from_studyset(request, studentdeck_id):
    deck_to_remove = StudentDeck.objects.get(id=studentdeck_id)
    deck_to_remove.delete()
    return redirect('show_my_studyset')


def test(request, deck_id):
    deck = Deck.objects.get(pk=deck_id)
    c_list = Card.objects.filter(deck_id=deck)
    context = {'list_of_cards': c_list}
    return render(request, 'test_deck.html', context)


def show_user(request):
    user = request.user.username
    context = {'users': user}
    return render(request, 'show_settings.html', context)


def review_subject(request, deck_id):
    m_list = Marks.objects.all()
    context = {'list_of_marks': m_list}
    return render(request, 'show_my_marks.html', context)


def forum(request):
    if request.method == "POST":
        user = request.user
        content = request.POST.get('content', '')
        post = Post(user1=user, post_content=content)
        post.save()
        alert = True
        return render(request, "forum.html", {'alert': alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "forum.html", {'posts': posts})


def discussion(request, myid):
    post = Post.objects.filter(id=myid).first()
    replies = Replie.objects.filter(post=post)
    if request.method == "POST":
        user = request.user
        desc = request.POST.get('desc', '')
        post_id = request.POST.get('post_id', '')
        reply = Replie(user = user, reply_content = desc, post=post)
        reply.save()
        alert = True
        return render(request, "discussion.html", {'alert': alert})
    return render(request, "discussion.html", {'post': post, 'replies': replies})