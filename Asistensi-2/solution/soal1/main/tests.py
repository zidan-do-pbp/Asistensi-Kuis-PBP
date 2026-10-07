from django.test import TestCase
from django.contrib.auth.models import User
class T(TestCase):
    def test_all(self):
        r=self.client.get("/register/"); assert r.status_code==200
        r=self.client.post("/register/",{"username":"a","password1":"xK9#mQ2$vL","password2":"bad"}); assert r.status_code==200 and User.objects.count()==0
        r=self.client.post("/register/",{"username":"a","password1":"xK9#mQ2$vL","password2":"xK9#mQ2$vL"}); assert r.status_code==302 and r.url=="/login/"
        r=self.client.post("/login/",{"username":"a","password":"no"}); assert r.status_code==200
        r=self.client.post("/login/",{"username":"a","password":"xK9#mQ2$vL"}); assert r.status_code==302 and r.url=="/"
        c=r.cookies["last_login"]; assert c["httponly"] and c["samesite"]=="Lax" and c["max-age"]==3600, c
        import re; assert re.match(r"\d{4}-\d\d-\d\d \d\d:\d\d:\d\d$",c.value)
        assert self.client.get("/logout/").status_code==405
        r=self.client.post("/logout/"); assert r.status_code==302 and r.cookies["last_login"]["max-age"]==0
        assert b"Belum login" in self.client.get("/").content
