###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

from . import views

###
# Routers
###
router = routers.SimpleRouter()
router.register(r'recipes', views.RecipeViewSet, base_name='recipes')


###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]
