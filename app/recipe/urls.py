from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('tags', views.TagView)
router.register('ingredients', views.IngredientView)
router.register('recipes', views.RecipeView)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
