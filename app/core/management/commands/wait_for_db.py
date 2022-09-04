"""
Django command to wait for an available db
"""

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

import time

from psycopg2 import OperationalError as Pyscopg2OpError


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pyscopg2OpError, OperationalError):
                self.stdout.write('Db unavailable, waiting 1 sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database Available'))
