﻿"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Главная', 1, 200)

    def test_blog(self):
        """Tests the blog page."""
        response = self.client.get('/blog')
        self.assertContains(response, 'Блог', 3, 200)

    def test_sections(self):
        """Tests the section page."""
        response = self.client.get('/sections')
        self.assertContains(response, 'Разделы биологии', 3, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Контакты', 3, 200)



  


