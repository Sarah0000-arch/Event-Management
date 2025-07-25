from django.contrib import admin
from django.urls import path
from events.views import dashboard,event_search,show_event, create_event, update_event, delete_event, participant_list, category_list, event_search, create_category, create_participant, update_category, update_participant, delete_category, delete_participant
urlpatterns = [
    path('', dashboard, name='home'),
    path('category/<int:category_id>/', dashboard, name='filter-by-category'),
    path('events/<int:id>/', show_event, name='event-detail'),
    path('event-search/', event_search, name='event-search'),
    path('create-event/', create_event, name='create-event'),
    path('update-event/<int:id>/', update_event, name='update-event'),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
    path('categories/', category_list, name='category-list'),
    path('participants/', participant_list, name='participant-list'),
    path('search/', event_search, name='event_search'),
    path('create-category/', create_category, name='create-category'),
    path('update-category/<int:id>/', update_category, name='update-category'),
    path('delete-category/<int:id>/', delete_category, name='delete-category'),
    path('create-participant/', create_participant, name='create-participant'),
    path('update-participant/<int:id>/', update_participant, name='update-participant'),
    path('delete-participant/<int:id>/', delete_participant, name='delete-participant'),
]