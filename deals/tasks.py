from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Profile, Budget
from datetime import datetime


@shared_task
def add(x, y):
    return x + y


@shared_task
def create_weekly_budgets():
    print('==============================')
    print('GENERATING WEEKLY BUDGETS')
    print('==============================')

    profiles = Profile.objects.all()

    for profile in profiles:
        # find budget template
        weekly_budget_template = Budget.objects.get(profile__user_id=profile.user.id, weekly=True)
        weekly_budget = weekly_budget_template
        weekly_budget.pk = None
        weekly_budget.name = f'{weekly_budget_template.name} {datetime.now()}'
        weekly_budget.weekly = False
        weekly_budget.save()

