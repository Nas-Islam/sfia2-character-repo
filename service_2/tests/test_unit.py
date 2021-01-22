from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from application import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

class TestResponse(TestBase):

    def test_get_name(self):
        for _ in range(15):
            response = self.client.get(url_for('get_name'))
            self.assertIn(response.data, [b"Linda", b"Elena", b"Rosa", b"Vy", b"Lola", b"Adrianne",b"Frederik", b"Rodriguez", b"Miguel", b"Dave", b"Harry", b"Roberto"])

    def test_get_item(self):
        for _ in range(10):
            response = self.client.get(url_for('get_item'))
            self.assertIn(response.data, [b'Sword', b'Axe', b'Bow', b'Sponge', b'Mirror', b'Wand'])
        
            
        
            