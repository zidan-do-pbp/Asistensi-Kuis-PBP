from django.test import TestCase
from django.contrib.auth.models import User
class T(TestCase):
    def test_all(self):
        r=self.client.get("/"); assert r.status_code==302 and "/login/" in r.url
        User.objects.create_user("regular",password="aaaaa"); self.client.login(username="regular",password="aaaaa")
        r=self.client.get("/"); h=r.content.decode()
        assert "Halo, regular!" in h and "1 kali" in h and "announcement" in h and "theme-light" in h
        assert "2 kali" in self.client.get("/").content.decode()
        assert self.client.post("/preferences/theme/",{"theme":"red"}).status_code==400
        assert self.client.post("/preferences/theme/",{"theme":"dark"}).status_code==302
        assert "theme-dark" in self.client.get("/").content.decode()
        assert self.client.get("/preferences/theme/").status_code==405
        r=self.client.post("/announcement/dismiss/"); c=r.cookies["announcement_dismissed"]
        assert c.value=="1" and c["max-age"]==604800 and c["httponly"] and c["samesite"]=="Lax"
        assert 'id="announcement"' not in self.client.get("/").content.decode()
        r=self.client.post("/preferences/reset/"); assert r.cookies["announcement_dismissed"]["max-age"]==0
        h=self.client.get("/").content.decode()
        assert "1 kali" in h and "theme-light" in h
