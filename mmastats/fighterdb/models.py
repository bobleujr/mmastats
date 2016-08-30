from django.db import models

# Create your models here.

class Fighter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    nick_name = models.CharField(max_length=300, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    locality = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    height = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    weight = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    weight_class = models.CharField(max_length=80, null=True, blank=True)
    team = models.CharField(max_length=150, null=True, blank=True)
    win_counter = models.IntegerField(null=True, blank=True)
    w_kos_tkos = models.IntegerField(null=True, blank=True)
    w_submissions = models.IntegerField(null=True, blank=True)
    w_decisions = models.IntegerField(null=True, blank=True)
    loss_counter = models.IntegerField(null=True, blank=True)
    l_kos_tkos = models.IntegerField(null=True, blank=True)
    l_submissions = models.IntegerField(null=True, blank=True)
    l_decisions = models.IntegerField(null=True, blank=True)


class Fight(models.Model):
    id = models.AutoField(primary_key=True)
    fighter1 = models.IntegerField(null=True, blank=True, db_column="fighter1_id")
    fighter2 = models.IntegerField(null=True, blank=True, db_column="fighter2_id")
    fighter_winner = models.IntegerField(null=True, blank=True, db_column="fighter_winner_id")
    fight_date = models.DateField(null=True, blank=True)
    event_id = models.IntegerField(null=True, blank=True)
    fight_result_type = models.CharField(max_length=50,null=True, blank=True)
    referee = models.CharField(max_length=150, null=True, blank=True)
    round = models.IntegerField(null=True, blank=True)
    time = models.CharField(max_length=10, null=True, blank=True)

