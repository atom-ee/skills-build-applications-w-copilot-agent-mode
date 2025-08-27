from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flying heroes')
        w1.suggested_for.set([tony, bruce])
        w2.suggested_for.set([steve, clark])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
