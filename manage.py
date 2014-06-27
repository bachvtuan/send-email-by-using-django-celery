#!/usr/bin/env python
# Input smtp information in settings.py
# Run celery:celery -A app worker -l info
# Run django : python manage.py runserver

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
