from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import QuestRewardModel, StudyTimeModel


class IndexView(TemplateView):
    template_name = 'app/index.html'


class RewardListView(ListView):
    template_name = 'app/manageRewardView.html'
    model = QuestRewardModel
