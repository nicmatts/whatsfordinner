from django.db import models

# Create your models here.
class AllMealsManager(models.Manager):
    def get_queryset(self):
        return super(AllMealsManager, self).get_queryset().all()

class AllIngredientsManager(models.Manager):
    def get_queryset(self):
        return super(AllIngredientsManager, self).get_queryset().all()

class Ingredient(models.Model):
	CATEGORY = (
		('breakfast', 'breakfast'),
		('chicken', 'chicken'),
		('hotdish', 'hotdish'),
		('pasta', 'pasta'),
		('soup', 'soup'),
		('other', 'other'),
	)

	ingredient_name = models.CharField(max_length = 200, verbose_name = "Ingredient name")
	ingredient_category = models.CharField(max_length=15, choices=CATEGORY)

	def __unicode__(self):
		return self.ingredient_name

	all_ingredients = AllIngredientsManager()


class Meal(models.Model):
	meal_name = models.CharField(max_length = 200, verbose_name="Dish name")
	meal_description = models.TextField(blank=True, verbose_name="Dish description")
	meal_ingredient = models.ManyToManyField(Ingredient)
	
	def __unicode__(self):
		return self.meal_name

	all_meals = AllMealsManager()

class LastMade(models.Model):
	last_made = models.DateField(auto_now_add=False, auto_now=True, verbose_name="Last made on")
	meal = models.ForeignKey(Meal)

	def __unicode__(self):
		return self.last_made

