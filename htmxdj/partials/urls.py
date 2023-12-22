from django.urls import path

from htmxdj.partials.views import PartialHomeProjects

app_name = "users"
urlpatterns = [
    path("projects/", view=PartialHomeProjects.as_view(), name="partial-projects"),
    path("services/", view=PartialHomeProjects.as_view(), name="partial-services"),
    path("news/", view=PartialHomeProjects.as_view(), name="partial-news"),
]
