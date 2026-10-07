from django.test import TestCase
from django.contrib.auth.models import User, Group
from main.models import Project
class T(TestCase):
    def setUp(self):
        self.p=Project.objects.create(title="P",description="d")
        for n,g in (("regular",None),("editor","Editor"),("owner","Owner")):
            u=User.objects.create_user(n,password="aaaaa")
            if g: u.groups.add(Group.objects.get(name=g))
    def login(self,n): self.client.login(username=n,password="aaaaa")
    def test_all(self):
        assert self.client.get("/projects/create/").status_code==302
        self.login("regular")
        assert self.client.get("/projects/create/").status_code==403
        assert self.client.get(f"/projects/{self.p.id}/edit/").status_code==403
        assert self.client.post(f"/projects/{self.p.id}/delete/").status_code==403
        assert self.client.post(f"/projects/{self.p.id}/star/").status_code==302
        assert self.p.starred_by.count()==1
        self.client.post(f"/projects/{self.p.id}/star/"); assert self.p.starred_by.count()==0
        assert self.client.get(f"/projects/{self.p.id}/star/").status_code==405
        h=self.client.get("/").content.decode()
        assert "create-control" not in h and "edit-control" not in h and "delete-control" not in h
        self.client.logout(); self.login("editor")
        assert self.client.get("/projects/create/").status_code==403
        assert self.client.get(f"/projects/{self.p.id}/edit/").status_code==200
        r=self.client.post(f"/projects/{self.p.id}/edit/",{"title":"New","description":"x"}); assert r.status_code==302
        self.p.refresh_from_db(); assert self.p.title=="New"
        assert self.client.get("/projects/999/edit/").status_code==404
        h=self.client.get("/").content.decode()
        assert "edit-control" in h and "delete-control" not in h and "create-control" not in h
        assert self.client.post(f"/projects/{self.p.id}/delete/").status_code==403
        self.client.logout(); self.login("owner")
        r=self.client.post("/projects/create/",{"title":"Z","description":"y"}); assert r.status_code==302 and Project.objects.count()==2
        h=self.client.get("/").content.decode()
        assert "create-control" in h and "edit-control" in h and "delete-control" in h
        assert self.client.post(f"/projects/{self.p.id}/delete/").status_code==302 and Project.objects.count()==1
