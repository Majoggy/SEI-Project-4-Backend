from django.db import models
from players.models import Player

# User ID field is a placeholder until I hook up user model/auth. Shouldn't be blank=true

class Game(models.Model):
    user_id = models.IntegerField(blank=True)
    first_place = models.ForeignKey(
        Player,
        related_name="first_place", 
        on_delete=models.DO_NOTHING)

    second_place = models.ForeignKey(
        Player,
        related_name="second_place", 
        on_delete=models.DO_NOTHING)

    third_place = models.ForeignKey(
        Player, 
        related_name="third_place", 
        on_delete=models.DO_NOTHING)

    fourth_place = models.ForeignKey(
        Player, related_name="fourth_place", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    fifth_place  = models.ForeignKey(
        Player, 
        related_name="fifth_place", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    sixth_place  = models.ForeignKey(
        Player, 
        related_name="sixth_place", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    seventh_place  = models.ForeignKey(
        Player, 
        related_name="seventh_place", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    eighth_place  = models.ForeignKey(
        Player, 
        related_name="eighth_place", 
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    ninth_place  = models.ForeignKey(
        Player, 
        related_name="ninth_place",
        on_delete=models.DO_NOTHING, 
        null=True, blank=True)

    buy_in = models.FloatField()
    prize_for_first = models.FloatField()
    prize_for_second = models.FloatField()
    prize_for_third = models.FloatField()
    date = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    number_of_players = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.date}'