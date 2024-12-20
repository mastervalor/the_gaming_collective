from django.test import TestCase
from account.models import UserManager, Users, Devices

class TestAccountModelsUserManager(TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.existing_user = Users.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            username='johndoe',
            password='hashed_password'
        )

    def test_valid_user_data(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertEqual(errors, {})
        
    def test_invalid_email(self):
        postData = {
            'email': 'invalid.email',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_short_first_name(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_passwords_do_not_match(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPaword1!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_short_password(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'Valid!',
            'password_confirm': 'Valid!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.default_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_vaild_edit_data(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertEqual(errors, {})
        
    def test_invalid_edit_email(self):
        postData = {
            'email': 'invalid.email',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_short_first_name(self):
        postData = {
            'email': 'valid.email@example.com',
            'password': 'ValidPassword1!',
            'password_confirm': 'ValidPassword1!',
            'first_name': 'J',
            'last_name': 'Doe'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_no_device(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_duplicate_username(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'johndoe'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_edit_short_username(self):
        postData = {
            'email': 'valid.email@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'devices': ['Xbox'],
            'username': 'j'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_finalize_valid_user_validator(self):
        postData = {
        'devices': ['Xbox'],
        'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertEqual(errors, {})
        
    def test_finalize_invalid_usernam(self):
        postData = {
        'devices': ['Xbox'],
        'username': 'j'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
    
    def test_finalize_no_devices(self):
        postData = {
        'username': 'janesmith'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
        
    def test_finalize_duplicate_username(self):
        postData = {
            'devices': ['Xbox'],
            'username': 'johndoe'
        }
        
        errors = self.user_manager.edit_user_validator(postData)
        self.assertIn('login', errors)
         

class DevicesModelTest(TestCase):
    def test_create_device(self):
        device = Devices.objects.create(device="Smartphone", dev_id=101)
        self.assertEqual(device.device, "Smartphone")
        self.assertEqual(device.dev_id, 101)
    
    def test_device_max_length(self):
        device = Devices.objects.create(device="a" * 45, dev_id=102)
        self.assertEqual(device.device, "a" * 45)
        
    def test_invalid_device_max_lenth(self):
        with self.assertRaises(Exception):
            Devices.objects.create(device="a" * 46, dev_id=103) 
    
    def test_invalid_device_max_length(self):
        with self.assertRaises(Exception):
            Devices.objects.create(device="Tablet")
            
class UsersModelTest(TestCase):
    def setUp(self):
        self.device1 = Devices.objects.create(device="Laptop", dev_id=123)
        self.device2 = Devices.objects.create(device="Phone", dev_id=456)
        self.user1 = Users.objects.create(
            email="user1@example.com",
            password="hashed_password1",
            first_name="John",
            last_name="Doe",
            username="johndoe"
        )
        self.user2 = Users.objects.create(
            email="user2@example.com",
            password="hashed_password2",
            first_name="Jane",
            last_name="Doe",
            username="janedoe"
        )
        
    def test_user_creation(self):
        """Test that a User instance is created with correct field values."""
        user = Users.objects.create(
            email="newuser@example.com",
            password="hashed_password",
            first_name="Alice",
            last_name="Smith",
            username="alicesmith"
        )
        self.assertEqual(user.email, "newuser@example.com")
        self.assertEqual(user.first_name, "Alice")
        self.assertEqual(user.username, "alicesmith")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        
    def test_email_field_label(self):
        """Test that the email field label is set correctly."""
        field_label = self.user1._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "User Email")
    
    def test_user_field_max_length(self):
        """Test max_length constraints on relevant fields."""
        max_length_username = self.user1._meta.get_field("username").max_length
        max_length_first_name = self.user1._meta.get_field("first_name").max_length
        max_length_last_name = self.user1._meta.get_field("last_name").max_length
        self.assertEqual(max_length_username, 45)
        self.assertEqual(max_length_first_name, 45)
        self.assertEqual(max_length_last_name, 45)
        
    def test_invalid_username_max_length(self):
        """Test that exceeding username max_length raises an error."""
        with self.assertRaises(Exception):
            Users.objects.create(
                email="longusername@example.com",
                password="hashed_password",
                first_name="John",
                last_name="Doe",
                username="a" * 46
            )
    
    def test_fav_devices_relationship(self):
        """Test the many-to-many fav_devices relationship."""
        self.user1.fav_devices.add(self.device1, self.device2)
        self.assertEqual(self.user1.fav_devices.count(), 2)
        self.assertIn(self.device1, self.user1.fav_devices.all())
        self.assertIn(self.device2, self.user1.fav_devices.all())
        
    def test_friends_relationship(self):
        """Test the many-to-many symmetrical friends relationship."""
        self.user1.friends.add(self.user2)
        self.assertIn(self.user2, self.user1.friends.all())
        self.assertIn(self.user1, self.user2.friends.all()) 
        
    def test_user_update(self):
        """Test updating an existing user."""
        self.user1.first_name = "Johnny"
        self.user1.save()
        updated_user = Users.objects.get(id=self.user1.id)
        self.assertEqual(updated_user.first_name, "Johnny")
        
    def test_user_deletion(self):
        """Test deleting a user instance."""
        user_id = self.user2.id
        self.user2.delete()
        with self.assertRaises(Users.DoesNotExist):
            Users.objects.get(id=user_id)
            