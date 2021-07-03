from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from recipes.models import Ingredient
from .models import Favorite, Purchase, Subscription


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'dimension')
        model = Ingredient


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('author', 'user')
        model = Subscription

    def validate_author(self, value):
        user = self.context['request'].user
        if user.id == value:
            raise ValidationError('Нельзя подписаться на самого себя')
        return value


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('recipe', 'user')
        model = Favorite


class PurchaseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('recipe', 'user')
        model = Purchase
