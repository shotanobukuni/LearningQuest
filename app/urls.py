from django.urls import path
from .views import IndexView, RewardListView
urlpatterns = [
    path('list/', RewardListView.as_view(), name='list'),
    path('', IndexView.as_view(), name='index'),
]