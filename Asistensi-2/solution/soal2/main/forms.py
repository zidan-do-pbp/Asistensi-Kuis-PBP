from django.forms import ModelForm

from main.models import Project


# DOKUMENTASI (jangan diubah). ModelForm otomatis membuat form dari model Project, hanya field title dan description.
# Dipakai create_project: ProjectForm(request.POST) dan edit_project: ProjectForm(request.POST, instance=project). Di template: {{ form.as_p }}
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description"]
