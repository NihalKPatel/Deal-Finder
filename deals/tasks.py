from background_task import background

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dealfinder.settings")
#
# import django
# django.setup()

@background(schedule=5)
def notify_user():
    # lookup user by id and send them a message
    print('GOT HERE')
