from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        Workout.objects.create(name='Super Strength', description='Strength training')
        Leaderboard.objects.create(team=marvel, points=100)
        Activity.objects.create(user=tony, type='Running', duration=30, date='2025-08-27')

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)
