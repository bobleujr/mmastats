from django.db import models

# Create your models here.

class Fighter(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(unique=True, default=0)
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
    ufc = models.BooleanField(default=False)


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











class EventMetric(models.Model):
    id = models.AutoField(primary_key=True)
    hasher = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

class FightMetric(models.Model):
    id = models.AutoField(primary_key=True)
    event_hasher = models.CharField(max_length=50, null=True, blank=True)
    fight_hasher = models.CharField(max_length=50, unique=True)
    fighter1 = models.CharField(max_length=30, null=True, blank=True, db_column="fighter1_id")
    fighter2 = models.CharField(max_length=30, null=True, blank=True, db_column="fighter2_id")
    str1 = models.IntegerField(null=True, blank=True)
    str2 = models.IntegerField(null=True, blank=True)
    td1 = models.IntegerField(null=True, blank=True)
    td2 = models.IntegerField(null=True, blank=True)
    sub1 = models.IntegerField(null=True, blank=True)
    sub2 = models.IntegerField(null=True, blank=True)
    pass1 = models.IntegerField(null=True, blank=True)
    pass2 = models.IntegerField(null=True, blank=True)
    round = models.IntegerField(null=True, blank=True)
    time = models.CharField(max_length=15, null=True, blank=True)
    method = models.CharField(max_length=100, null=True, blank=True)
    method2 = models.CharField(max_length=100, null=True, blank=True)
    weight_cate = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

class FighterMetric(models.Model):
    id = models.AutoField(primary_key=True)
    hasher = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=150, null=True, blank=True)
    nick_name = models.CharField(max_length=300, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    reach = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    weight = models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)
    height = models.CharField(max_length=20, null=True, blank=True)
    # significant strikes landed per minute
    slpm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # significant striking accuracy
    stracc = models.IntegerField(null=True, blank=True)
    # significant strike absorbed per minute
    sapm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # significant strike defence
    strdef = models.IntegerField(null=True, blank=True)
    # average takedown landed per 15 minutes
    tdavg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # takedown accuracy
    tdacc = models.IntegerField(null=True, blank=True)
    # takedown defense
    tddef = models.IntegerField(null=True, blank=True)
    # submission attempted per 15 minutes
    subavg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

