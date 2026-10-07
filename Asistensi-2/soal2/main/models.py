from django.db import models
from django.contrib.auth.models import User


# DOKUMENTASI (jangan diubah saat kuis). Satu Project punya banyak user yang menandai bintang (ManyToMany).
# starred_by dipakai di views (toggle_star: .add / .remove / .filter(pk=...).exists()) dan template ({{ project.starred_by.count }}).
# related_name="starred_projects" = dari sisi user: user.starred_projects.all()
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    starred_by = models.ManyToManyField(User, blank=True, related_name="starred_projects")

    def __str__(self):
        return self.title
