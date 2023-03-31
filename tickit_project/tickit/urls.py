from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('venues/', views.VenueList.as_view(), name='venue_list'),
    path('events/', views.EventList.as_view(), name='event_list'),
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue_detail'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail')
]