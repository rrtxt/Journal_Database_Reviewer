from django.urls import path, include
from . import views
# ... your other URL patterns ...


urlpatterns = [
    path("", view=views.index)
]