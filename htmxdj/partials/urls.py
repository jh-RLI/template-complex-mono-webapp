from django.urls import path

from htmxdj.partials.views import PartialHomeNews, PartialHomeProjects, PartialHomeServices

app_name = "users"
urlpatterns = [
    path("projects/", view=PartialHomeProjects.as_view(), name="partial-projects"),
    path("services/", view=PartialHomeServices.as_view(), name="partial-services"),
    path("news/", view=PartialHomeNews.as_view(), name="partial-news"),
]
