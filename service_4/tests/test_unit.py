from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase


from application import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

class TestResponse(TestBase):

    # Testing all the 'Wand' item bonuses with every class
    def test_get_wand_wizard_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Wizard"})
        self.assertEqual(b'+100 Magic, +120 Magic, +200 Magic', response.data)
    
    def test_get_wand_warrior_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Warrior"})
        self.assertEqual(b'+100 Attack, +120 Magic, +5 Magic', response.data)

    def test_get_wand_witch_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Witch"})
        self.assertEqual(b'+100 Alchemy, +120 Magic, +150 Magic', response.data)

    def test_get_wand_knight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Knight"})
        self.assertEqual(b'+150 Attack, +120 Magic, +1 Magic', response.data)   

    def test_get_wand_royalknight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Royal Knight"})
        self.assertEqual(b'+250 Attack, +120 Magic, -30 Magic', response.data)

    def test_get_wand_warlock_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Warlock"})
        self.assertEqual(b'+300 Magic, +120 Magic, +200 Magic', response.data)
    
    def test_get_wand_maid_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Maid"})
        self.assertEqual(b'+100 Cleaning, +120 Magic, +30 Magic', response.data)
    
    def test_get_wand_doctor_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Wand", "class_response":"Doctor"})
        self.assertEqual(b'+150 Healing, +120 Magic, +30 Magic', response.data) 
    
    # Testing all the 'Sword' item bonuses with every class
    def test_get_sword_warrior_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Warrior"})
        self.assertEqual(b'+100 Attack, +120 Attack, +100 Attack', response.data)
    
    def test_get_sword_wizard_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Wizard"})
        self.assertEqual(b'+100 Magic, +120 Attack, +5 Attack', response.data)
    
    def test_get_sword_witch_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Witch"})
        self.assertEqual(b'+100 Alchemy, +120 Attack, +5 Attack', response.data)
    
    def test_get_sword_knight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Knight"})
        self.assertEqual(b'+150 Attack, +120 Attack, +150 Attack', response.data)
    
    def test_get_sword_royalknight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Royal Knight"})
        self.assertEqual(b'+250 Attack, +120 Attack, +200 Attack', response.data)

    def test_get_sword_warlock_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Warlock"})
        self.assertEqual(b'+300 Magic, +120 Attack, +10 Attack', response.data)
    
    def test_get_sword_maid_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Maid"})
        self.assertEqual(b'+100 Cleaning, +120 Attack, +80 Attack', response.data)
    
    def test_get_sword_doctor_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sword", "class_response":"Doctor"})
        self.assertEqual(b'+150 Healing, +120 Attack, +30 Attack', response.data)

    # Testing all the 'Axe' item bonuses with every class
    def test_get_axe_warrior_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Warrior"})
        self.assertEqual(b'+100 Attack, +120 Woodcutting, +40 Attack', response.data)
    
    def test_get_axe_wizard_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Wizard"})
        self.assertEqual(b'+100 Magic, +120 Woodcutting, +10 Attack', response.data)
    
    def test_get_axe_witch_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Witch"})
        self.assertEqual(b'+100 Alchemy, +120 Woodcutting, +10 Attack', response.data)
    
    def test_get_axe_knight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Knight"})
        self.assertEqual(b'+150 Attack, +120 Woodcutting, +50 Attack', response.data)
    
    def test_get_axe_royalknight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Royal Knight"})
        self.assertEqual(b'+250 Attack, +120 Woodcutting, +60 Attack', response.data)

    def test_get_axe_warlock_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Warlock"})
        self.assertEqual(b'+300 Magic, +120 Woodcutting, +10 Magic', response.data)
    
    def test_get_axe_maid_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Maid"})
        self.assertEqual(b'+100 Cleaning, +120 Woodcutting, +100 Attack', response.data)
    
    def test_get_axe_doctor_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Axe", "class_response":"Doctor"})
        self.assertEqual(b'+150 Healing, +120 Woodcutting, +30 Attack', response.data)

    # Testing all the 'Bow' item bonuses with every class
    def test_get_bow_warrior_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Warrior"})
        self.assertEqual(b'+100 Attack, +120 Range, +30 Ranged', response.data)
    
    def test_get_bow_wizard_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Wizard"})
        self.assertEqual(b'+100 Magic, +120 Range, +10 Ranged', response.data)
    
    def test_get_bow_witch_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Witch"})
        self.assertEqual(b'+100 Alchemy, +120 Range, +10 Ranged', response.data)
    
    def test_get_bow_knight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Knight"})
        self.assertEqual(b'+150 Attack, +120 Range, +50 Ranged', response.data)
    
    def test_get_bow_royalknight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Royal Knight"})
        self.assertEqual(b'+250 Attack, +120 Range, +60 Ranged', response.data)

    def test_get_bow_warlock_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Warlock"})
        self.assertEqual(b'+300 Magic, +120 Range, +10 Ranged', response.data)
    
    def test_get_bow_maid_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Maid"})
        self.assertEqual(b'+100 Cleaning, +120 Range, +100 Ranged', response.data)
    
    def test_get_bow_doctor_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Bow", "class_response":"Doctor"})
        self.assertEqual(b'+150 Healing, +120 Range, +30 Ranged', response.data)

    # Testing all the 'Sponge' item bonuses with every class
    def test_get_sponge_warrior_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Warrior"})
        self.assertEqual(b'+100 Attack, +120 Cleanliness, Shiny Armour', response.data)
    
    def test_get_sponge_wizard_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Wizard"})
        self.assertEqual(b'+100 Magic, +120 Cleanliness, Shiny Wizard Hat', response.data)
    
    def test_get_sponge_witch_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Witch"})
        self.assertEqual(b'+100 Alchemy, +120 Cleanliness, Shiny Cauldron', response.data)
    
    def test_get_sponge_knight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Knight"})
        self.assertEqual(b'+150 Attack, +120 Cleanliness, Shiny Armour', response.data)
    
    def test_get_sponge_royalknight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Royal Knight"})
        self.assertEqual(b'+250 Attack, +120 Cleanliness, Extremely Shiny Armour', response.data)

    def test_get_sponge_warlock_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Warlock"})
        self.assertEqual(b'+300 Magic, +120 Cleanliness, Cleaning Spell', response.data)
    
    def test_get_sponge_maid_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Maid"})
        self.assertEqual(b'+100 Cleaning, +120 Cleanliness, Invincibility', response.data)
    
    def test_get_sponge_doctor_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Sponge", "class_response":"Doctor"})
        self.assertEqual(b'+150 Healing, +120 Cleanliness, Disinfectant', response.data)

    #Testing all "No_Bonuses" with every class
    def test_get_no_bonus_warrior_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Warrior"})
        self.assertEqual(b'+100 Attack, Reflective Armour, No Extra Bonuses', response.data)
    
    def test_get_no_bonus_wizard_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Wizard"})
        self.assertEqual(b'+100 Magic, Reflective Armour, No Extra Bonuses', response.data)
    
    def test_get_no_bonus_witch_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Witch"})
        self.assertEqual(b'+100 Alchemy, Reflective Armour, No Extra Bonuses', response.data)
    
    def test_get_no_bonus_knight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Knight"})
        self.assertEqual(b'+150 Attack, Reflective Armour, No Extra Bonuses', response.data)
    
    def test_get_no_bonus_royalknight_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Royal Knight"})
        self.assertEqual(b'+250 Attack, Reflective Armour, No Extra Bonuses', response.data)

    def test_get_no_bonus_warlock_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Warlock"})
        self.assertEqual(b'+300 Magic, Reflective Armour, No Extra Bonuses', response.data)
    
    def test_get_no_bonus_maid_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Maid"})
        self.assertEqual(b'+100 Cleaning, Reflective Armour, No Extra Bonuses', response.data)
    
    def test_get_no_bonus_doctor_bonus(self):
        response = self.client.post(url_for('get_bonus'), json={"item_response":"Mirror", "class_response":"Doctor"})
        self.assertEqual(b'+150 Healing, Reflective Armour, No Extra Bonuses', response.data)