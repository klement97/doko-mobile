from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Email


# tests for views

class BaseViewTest(TestCase):

    @staticmethod
    def register(email="", message=""):
        if email != "":  # message can be blank
            Email.objects.create(email=email, message=message)

    def setUp(self):
        # add test data
        self.client = Client()
        manager = User.objects.create(username="admin", is_superuser=True)
        manager.set_password("admin")
        manager.save()
        self.client.login(username="admin", password="admin")

        self.register("klementomeri97@gmail.com", "Hello doko mobile!")
        self.register("klement-omeri97@hotmail.com", "Hello hello pershendetje")
        self.register("arliarli123@gmail.com", "O PUCO CA BEN ATQII")
        self.register("arlitorotoroarli@gmail.com", "Hello, im arli")


class GetAllEmailsTest(BaseViewTest):

    def test_get_all_songs(self):
        """
        This test ensures that all emails registered in setUp method exists when we
        make a GET request to the /manager end point and this endpoint is protected
        """

        response = self.client.get(reverse("manager"))

        expected = Email.objects.all()

        self.assertEqual(response.status_code, 200)

        # logging out now
        self.client.logout()

        # making request again
        response = self.client.get(reverse('manager'))

        self.assertEqual(response.status_code, 400)
