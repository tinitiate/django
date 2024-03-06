from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings # correct way

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("Current Time is %s" % time)
