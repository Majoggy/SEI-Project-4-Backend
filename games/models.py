from django.db import models

# User ID field is a placeholder until I hook up user model/auth. Shouldn't be blank=true

class Game(models.Model):
    user_id = models.IntegerField(blank=True)
    first_place = models.ForeignKey(
        'players.Player',
        related_name="+", 
        on_delete=models.DO_NOTHING)

    second_place = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING)

    third_place = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING)

    fourth_place = models.ForeignKey(
        'players.Player', related_name="+", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    fifth_place  = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    sixth_place  = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    seventh_place  = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    eight_place  = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    ninth_place  = models.ForeignKey(
        'players.Player', 
        related_name="+", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)
        
    buy_in = models.FloatField()
    prize_for_first = models.FloatField()
    prize_for_second = models.FloatField()
    prize_for_third = models.FloatField()
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.date}'