from django.test import TestCase
from django.urls import reverse

class faq(TestCase):

    # test that the dashboard view can be acessed via the following url
    def test_view_url_exists_at_desired_location_faq(self):
        response = self.client.get('/deals/FAQ')
        self.assertEqual(response.status_code, 200)

    # test that the dashboard view can be acessed via the following name
    def test_view_url_accessible_by_name_faq(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)

    # test that the dashboard view is using the correct template
    def test_view_uses_correct_template_faq(self):
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/faq.html')
