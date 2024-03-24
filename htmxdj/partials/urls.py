from django.urls import path

from htmxdj.partials.views import PartialDetailClub, PartialHomeNews, PartialHomeProjects, PartialHomeServices

urlpatterns = [
    path("projects/", view=PartialHomeProjects.as_view(), name="partial-projects"),
    path("services/", view=PartialHomeServices.as_view(), name="partial-services"),
    path("news/", view=PartialHomeNews.as_view(), name="partial-news"),
    path("club/", view=PartialDetailClub.as_view(), name="partial-club"),
]
