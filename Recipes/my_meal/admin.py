from django.contrib import admin

# Register your models here.
from .models import Blog

admin.site.register(Blog) 



from django.contrib import admin
from .models import AllergicRecipe, VegetarianRecipe, DiabeticRecipe, NormalRecipe

@admin.register(AllergicRecipe)
class AllergicRecipeAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'meal_time')
    search_fields = ('food_name',)

@admin.register(VegetarianRecipe)

class VegetarianRecipeAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'meal_time')
    search_fields = ('food_name',)

@admin.register(DiabeticRecipe)
class DiabeticRecipeAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'meal_time')
    search_fields = ('food_name',)

@admin.register(NormalRecipe)
class NormalRecipeAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'meal_time')
    search_fields = ('food_name',)




from .models import (
    AllergicDrinks, AllergicSnacks, AllergicDesserts, AllergicFruits,
    VegeterianDrinks, VegeterianSnacks, VegeterianDesserts, VegeterianFruits,
    NormalDrinks, NormalSnacks, NormalDesserts, NormalFruits,
    DiabeticDrinks, DiabeticSnacks, DiabeticDesserts, DiabeticFruits
)


admin.site.register([
    AllergicDrinks, AllergicSnacks, AllergicDesserts, AllergicFruits,
    VegeterianDrinks, VegeterianSnacks, VegeterianDesserts, VegeterianFruits,
    NormalDrinks, NormalSnacks, NormalDesserts, NormalFruits,
    DiabeticDrinks, DiabeticSnacks, DiabeticDesserts, DiabeticFruits
])