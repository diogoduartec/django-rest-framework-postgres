from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        """this function run before every test"""
        
        self.client = Client()
        
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='password123'
        ) 
        
        print('session', self.client.session.session_key)
        self.client.force_login(self.admin_user)

        self.assertTrue(self.admin_user.is_authenticated)

        self.user = get_user_model().objects.create_user(
            email='user@test.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Tests that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        print('session', self.client.session.session_key)
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
