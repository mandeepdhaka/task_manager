from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class RateLimitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)  

    def test_rate_limit(self):
        # Set Authorization header with JWT token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # First request should succeed
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Make 5 requests
        for _ in range(4):
            self.client.get('/api/tasks/')

        # 6th request should be rate-limited
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
