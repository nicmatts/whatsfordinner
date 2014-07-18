from django.db import models


# Create your models here.
class AllMealsManager(models.Manager):
    def get_queryset(self):
        return super(AllMealsManager, self).get_queryset().all()

class AllIngredientsManager(models.Manager):
    def get_queryset(self):
        return super(AllIngredientsManager, self).get_queryset().all()

class AllLastMadesManager(models.Manager):
    def get_queryset(self):
        return super(AllLastMadesManager, self).get_queryset().all()

class LastTenMadesManager(models.Manager):
    def get_queryset(self):
        return super(LastTenMadesManager, self).get_queryset().all().order_by('-id')[:10]

class LeastTenMadesManager(models.Manager):
    def get_queryset(self):
        return super(LeastTenMadesManager, self).get_queryset().all().order_by('id')[:10]


class Ingredient(models.Model):
	ingredient_name = models.CharField(max_length=200, verbose_name="Ingredient name")
	ingredient_quantity = models.CharField(max_length=5, verbose_name="Ingredient quantity", blank="True")

	def __unicode__(self):
		return self.ingredient_name

	all_ingredients = AllIngredientsManager()


class Meal(models.Model):
	CATEGORY = (
		('breakfast', 'breakfast'),
		('cheese', 'cheese'),
		('chicken', 'chicken'),
		('hotdish', 'hotdish'),
		('pasta', 'pasta'),
		('pizza', 'pizza'),
		('soup', 'soup'),
		('other', 'other'),
	)

	meal_name = models.CharField(max_length = 200, verbose_name="Dish name")
	meal_description = models.TextField(blank=True, verbose_name="Dish description")
	meal_category = models.CharField(max_length=15, choices=CATEGORY)
	meal_ingredient = models.ManyToManyField(Ingredient)
	meal_slug = models.SlugField(max_length=100, unique=True)

	def __unicode__(self):
		return self.meal_name

	all_meals = AllMealsManager()

class LastMade(models.Model):
	last_made = models.DateField(auto_now_add=False, auto_now=True, verbose_name="Last made on")
	meal = models.ForeignKey(Meal,related_name='meal')
	last_made_meal_slug = models.SlugField(max_length=100, unique=True)

	def __unicode__(self):
		return unicode(self.last_made)

	all_last_mades = AllLastMadesManager()
	last_ten_mades = LastTenMadesManager()
	least_ten_mades = LeastTenMadesManager()

