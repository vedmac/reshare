from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(
        'Ingredient name',
        max_length=256,
        db_index=True
    )
    dimension = models.CharField('Dimension', max_length=64)

    class Meta:
        ordering = ('title', )
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'

    def __str__(self):
        return f'{self.title}, {self.dimension}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Recipe author'
    )
    title = models.CharField('Recipe name', max_length=200)
    image = models.ImageField('Image', upload_to='recipes/')
    text = models.TextField('Recipe text')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ingredient'
    )
    cooking_time = models.PositiveSmallIntegerField('Cooking time')
    slug = AutoSlugField(populate_from='title', allow_unicode=True)
    tags = models.ManyToManyField(
        'Tag',
        related_name='recipes',
        verbose_name='Tags'
    )
    pub_date = models.DateTimeField(
        'Date of publication',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts'
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('ingredient', 'recipe')


class Tag(models.Model):
    title = models.CharField('Tag name', max_length=50, db_index=True)
    display_name = models.CharField('Tag name for template', max_length=50)
    color = models.CharField('Tag color', max_length=50)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.title
