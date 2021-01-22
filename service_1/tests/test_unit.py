from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.models import Characters

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Characters(name="test_name", item="test_item", class_type="test_class", bonus="test_bonus"))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):

    def test_service1(self):
        with requests_mock.mock() as m:
            m.get("http://service2-backend:5000/name", text='Dave')
            m.get("http://service2-backend:5000/item", text='Wand')
            m.get("http://service3-backend:5000/class", text='Wizard')
            m.post('http://service4-backend:5000/stats', json='+100 Magic, +120 Magic, +200 Magic')
            response = self.client.get(url_for('index'))
            self.assertIn(b'Dave', response.data)
            self.assertIn(b'Wand', response.data)
            self.assertIn(b'Wizard', response.data)
            self.assertIn(b'+100 Magic, +120 Magic, +200 Magic', response.data)
            
        
            