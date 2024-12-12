
from django.core.management.base import BaseCommand
from main.models import Tour

class Command(BaseCommand):
    help = 'Удаляет все туры, кроме первых 10'

    def handle(self, *args, **kwargs):

        first_10_tours = Tour.objects.all()[:10]
        tours_to_delete = Tour.objects.exclude(id__in=first_10_tours.values('id'))

        deleted_count, _ = tours_to_delete.delete()
        self.stdout.write(self.style.SUCCESS(f'Удалено туров: {deleted_count}'))