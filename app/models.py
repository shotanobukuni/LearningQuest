from django.db import models


class QuestRewardModel(models.Model):
    """
    達成報酬モデル
    """
    class Meta:
        db_table = 'QuestReward'

    reward = models.CharField(max_length=100)
    target_time = models.IntegerField()


class StudyTimeModel(models.Model):
    """
    学習時間モデル
    """
    class Meta:
        db_table = 'StudyTime'

    study_time = models.IntegerField()