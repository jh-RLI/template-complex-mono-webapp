from django.shortcuts import HttpResponse, render
from django.views.generic.detail import DetailView
from django.views import View


class PartialHomeProjects(View):
    def get(self, request):
        partial = render(
            request,
            "partials/projects.html",
        ).content.decode("utf-8")

        return HttpResponse(partial)


class PartialHomeServices(View):
    def get(self, request):
        partial = render(
            request,
            "partials/services.html",
        ).content.decode("utf-8")

        return HttpResponse(partial)


class PartialHomeNews(View):
    def get(self, request):
        partial = render(
            request,
            "partials/news.html",
        ).content.decode("utf-8")

        return HttpResponse(partial)


class PartialDetailClub(DetailView):
    def get(self, request):

        return render(request, "partials/club.html")
