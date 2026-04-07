
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Eliminar datos existentes
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')

        # Asignar equipos (si el modelo User tiene campo team, si no, omitir)
        # ironman.team = marvel
        # spiderman.team = marvel
        # batman.team = dc
        # superman.team = dc
        # ironman.save()
        # spiderman.save()
        # batman.save()
        # superman.save()

        # Crear actividades
        Activity.objects.create(user=ironman, type='run', duration=30, calories=300)
        Activity.objects.create(user=spiderman, type='cycle', duration=45, calories=400)
        Activity.objects.create(user=batman, type='swim', duration=60, calories=500)
        Activity.objects.create(user=superman, type='run', duration=50, calories=450)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, score=1000)
        Leaderboard.objects.create(user=spiderman, score=900)
        Leaderboard.objects.create(user=batman, score=1100)
        Leaderboard.objects.create(user=superman, score=1200)

        # Crear workouts
        Workout.objects.create(user=ironman, name='Chest Day', description='Bench press, push-ups')
        Workout.objects.create(user=spiderman, name='Cardio', description='Running, cycling')
        Workout.objects.create(user=batman, name='Strength', description='Deadlift, squats')
        Workout.objects.create(user=superman, name='Power', description='Power cleans, sprints')

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
