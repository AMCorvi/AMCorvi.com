from django.views import generic

from .models import Project


# Create your views here.


class IndexView(generic.ListView):
    context_object_name = "projects_list"

    def get_queryset(self):
        return Project.objects.order_by("-date_published")

class ProjectView(generic.DetailView):
    model = Project

