from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from deals.models import Profile, List, Budget


# A user profile to be created for each new user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
        first_list = List.objects.create(name='My First List', type='S', profile=profile)
        first_list.save()
        first_budget = Budget.objects.create(name='My Weekly Budget',
                                             max_spend=500,
                                             profile=profile,
                                             list=first_list,
                                             weekly=True)
        first_budget.save()

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


