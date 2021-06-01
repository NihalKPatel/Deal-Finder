from django.urls import reverse
from django.test import TestCase


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


class DetailsViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/deals/details')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('details'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('details'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/details.html')


class BudgetCalculatorTest(TestCase):

    # test that the BudgetCalculator view can be accessed via the following url
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/deals/budget_calculator')
        self.assertEqual(response.status_code, 200)

    # test that the BudgetCalculator view can be accessed via the following name
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('budget_calculator'))
        self.assertEqual(response.status_code, 200)

    # test that the BudgetCalculator view is using the correct template
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('budget_calculator'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/budget_calculator.html')
