from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from application import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

class TestResponse(TestBase):

# Tests if all the classes can be reached
    def test_get_class(self):
        for _ in range(15):
            response = self.client.get(url_for('get_class'))
            self.assertIn(response.data, [b'Warrior', b'Wizard', b'Witch', b'Knight', b'Royal Knight', b'Warlock', b'Maid', b'Doctor'])
        
            
        
            