# Core Django imports.
from django.db.models.signals import post_save
from django.dispatch import receiver

# Magazine and Accounts application imports.
from accounts.models import Account
from magazine.models import Author
from members.models import UserProfile as UserProfile2

# Creates author profile immediately an account is created for her/him.
@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
        profile = UserProfile2.objects.create(user=instance)
        profile.save()


 
