import json

from django.test import Client, TestCase

from main.models import Report


class ItemFinderEndpointTest(TestCase):
    def test_list_and_create(self):
        Report.objects.create(title="Dompet", location="Kantin", status="hilang")
        data = self.client.get("/reports/data/").json()
        self.assertEqual(len(data["reports"]), 1)

        body = json.dumps({"title": "Kunci", "location": "Lab", "status": "ditemukan"})
        r = self.client.post("/reports/add/", body, content_type="application/json")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(Report.objects.count(), 2)

        bad = json.dumps({"title": "", "location": "Lab", "status": "x"})
        r = self.client.post("/reports/add/", bad, content_type="application/json")
        self.assertEqual(r.status_code, 400)
        self.assertIn("errors", r.json())

    def test_csrf_enforced(self):
        strict = Client(enforce_csrf_checks=True)
        r = strict.post("/reports/add/", "{}", content_type="application/json")
        self.assertEqual(r.status_code, 403)

    def test_page_renders_with_token(self):
        r = self.client.get("/")
        self.assertContains(r, "csrfmiddlewaretoken")
        self.assertContains(r, "initial-reports")
