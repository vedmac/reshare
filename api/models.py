from django.contrib.auth import get_user_model
from django.db import models

from recipes.models import Recipe

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='User',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favored_by',
        verbose_name='Add to favorite',
    )

    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Favorite recipes'
        verbose_name_plural = 'Favorite recipes'


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Follow',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Follower',
    )

    class Meta:
        unique_together = ('user', 'author')
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


class Purchase(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='purchases',
        verbose_name='User',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Recipe in shopping list',
    )

    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'
