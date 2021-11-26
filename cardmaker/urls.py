from django.urls import path
from . import views
from .views import DeckCreate

# app_name = 'cardmaker'

urlpatterns = [
    path('', views.show_all_decks, name='all_decks'),
    path('deck/my', views.show_my_decks, name='my_decks'),
    path('card/delete/<int:deck_id>/<int:card_id>/', views.delete_card, name="delete_card"), #slug in django
    path('deck/all', views.show_all_decks, name='all_decks'),
    path('deck/delete/<int:deck_id>/', views.delete_deck, name="delete_deck"),
    path('deck/create/', views.DeckCreate.as_view(), name='create_deck'),
    path('deck/<deck_id>/', views.create_cards, name='create_cards'),
    path('deck/show/<int:deck_id>/', views.show_deck, name="show_deck"),
    path('deck/save/<int:deck_id>/', views.save_for_study, name="save_for_study"),
    path('studyset/', views.show_my_studyset, name='show_my_studyset'),
    path('studyset/remove/<int:studentdeck_id>/', views.remove_from_studyset, name= 'remove_from_studyset'),
    path('deck/test/<int:deck_id>', views.test, name='test'),
    path('deck/rehearse/<int:deck_id>', views.rehearse_deck, name="rehearse"),
    path('settings/', views.show_user, name="setting"),
    path('forum/', views.forum, name="forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    # path('forum/', views.forum, name="forum"),
    #path('deck/rehearse/<int:deck_id>/', views.rehearse_deck, name="rehearse_deck"),
]
