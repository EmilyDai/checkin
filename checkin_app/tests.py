from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from checkin_app.models import User

class TagTests(APITestCase):
    def test(self):
        data = {'name': 'test_tag'}
        response = self.client.post('/checkin/tags/', data, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/checkin/tags/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'test_tag')

        response = self.client.get('/checkin/tags/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test_tag')

        data = {'name': 'test_nwe_tag'}
        response = self.client.put('/checkin/tags/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test_nwe_tag')

        response = self.client.delete('/checkin/tags/1/')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/checkin/tags/1/')
        self.assertEqual(response.status_code, 404)

class RuleTests(APITestCase):
    def test(self):
        data = {'duration': 20}
        response = self.client.post('/checkin/rules/', data, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/checkin/rules/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['duration'], 20)

        response = self.client.get('/checkin/rules/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['duration'], 20)

        data = {'duration': 30}
        response = self.client.put('/checkin/rules/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['duration'], 30)

        response = self.client.delete('/checkin/rules/1/')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/checkin/rules/1/')
        self.assertEqual(response.status_code, 404)

class ProjectTests(APITestCase):
    def test(self):
        data = {"tag_id": 1, "rule_id": 1, "notice": "haha"}
        response = self.client.post('/checkin/projects/', data, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/checkin/projects/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['notice'], "haha")

        response = self.client.get('/checkin/projects/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['notice'], "haha")

        data = {"name": "test_project"}
        response = self.client.put('/checkin/projects/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], "test_project")

        response = self.client.delete('/checkin/projects/1/')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/checkin/projects/1/')
        self.assertEqual(response.status_code, 404)
