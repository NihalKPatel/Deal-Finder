from django.test import TestCase
from django.urls import reverse


class DashboardViewTest(TestCase):

    # test that the dashboard view can be acessed via the following url
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/deals/dashboard')
        self.assertEqual(response.status_code, 200)

    # test that the dashboard view can be acessed via the following name
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    # test that the dashboard view is using the correct template
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/dashboard.html')


class IndexViewTest(TestCase):

    # test that the index view can be accessed via the following url
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/deals/')
        self.assertEqual(response.status_code, 200)

    # test that the index view can be access via the following name
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    # test that the index view is using the correct template
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class AboutViewTest(TestCase):

    # test that the about view can be accessed via the following url
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/deals/about/')
        self.assertEqual(response.status_code, 200)

    # test that the about view can be access via the following name
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    # test that the about view is using the correct template
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
