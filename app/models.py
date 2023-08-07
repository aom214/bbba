from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class upcoming(models.Model):
    team1=models.CharField(max_length=30)
    team2=models.CharField(max_length=30)
    match_unique_name=models.CharField(max_length=120,default="")
    match_venue=models.CharField( max_length=50,default="")
    match_date=models.DateField()
    match_time=models.TimeField()
    match_price=models.IntegerField(default=0)
    match_desc=models.TextField()
    match_image=models.ImageField(upload_to='game/images',default="")
    def __str__(self):
        return self.match_unique_name
class teams(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default="")
    team_name=models.CharField(max_length=30)
    teams_image=models.ImageField(upload_to='game/images',default="")
    team_owner=models.CharField(max_length=30,default="")
    team_coach=models.CharField(max_length=30,default="")
    team_captain=models.CharField(max_length=30,default="")
    team_home=models.CharField(max_length=30,default="")
    def __str__(self):
        return self.team_name
players_types=(
    ('one','chaser'),
    ('two','keeper'),
    ('three','beaters'),
    ('four','seeker'))


class addplayers(models.Model):
    team=models.CharField(max_length=60,default="")
    players_type=models.CharField(max_length=15,choices=players_types,default="")
    player_name=models.CharField(max_length=30)
    player_image=models.ImageField(upload_to='game/images',default="")

    def __str__(self):
        return self.player_name
class points(models.Model):
    team=models.CharField(max_length=30,default="")
    team_image=models.ImageField(upload_to='game/images',default="")
    MATCHES_PLAYED=models.IntegerField(default=0)
    MATCHES_WON=models.IntegerField(default=0)
    MATCHES_DRAW=models.IntegerField(default=0)
    TOTAL_GOALS_SCORED=models.IntegerField(default=0)
    TOTAL_GOALS_AGAINST=models.IntegerField(default=0)
    def __str__(self):
        return self.team
    def poin(self):
        return self.MATCHES_WON*3+self.MATCHES_DRAW*1
    def plusminus(self):
        return self.TOTAL_GOALS_SCORED-self.TOTAL_GOALS_AGAINST
    def loss(self):
        return self.MATCHES_PLAYED-self.MATCHES_DRAW-self.MATCHES_WON



class regteam(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    team_name=models.CharField(max_length=50)
    team_logo=models.ImageField(upload_to='game/images',default="")
    team_homevenue=models.CharField(max_length=100)
    preferred_location=models.CharField(max_length=200,default="")
    def __str__(self):
        return self.team_name
    

class register_players(models.Model):
    team=models.ForeignKey(regteam, on_delete=models.CASCADE)
    player_name=models.CharField(max_length=100)
    player_type=models.CharField(max_length=100)
    player_age=models.IntegerField(default=18)
    player_image=models.ImageField(upload_to='shopp/images',default="")



class previous(models.Model):
    team1=models.CharField(max_length=30)
    team2=models.CharField(max_length=30)
    match_won_team=models.CharField(max_length=100)
    match_venue=models.CharField( max_length=50,default="")
    match_date=models.DateField()
    match_time=models.TimeField()
    match_desc=models.TextField()
    match_image=models.ImageField(upload_to='game/images',default="")
    def __str__(self):
        return self.team1
    


class matchCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match_unique_name = models.ForeignKey(upcoming, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def priceofmatch(self):
        return self.match_unique_name.match_price*self.quantity

    def __str__(self):
        return f"{self.user.username}'s {self.match_unique_name} ({self.quantity})"


class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_age=models.IntegerField(default=0)
    user_occupation=models.CharField(max_length=100,default="")
    user_image=models.ImageField(upload_to='game/images',default="")

    def __str__(self):
        return self.first_name
