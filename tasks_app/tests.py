from django.test import TestCase
import requests

class SimpleTest(TestCase):
    
    def test_basic(self):
        """This should definitely work"""
        print("🎯 TEST IS RUNNING!")
        self.assertEqual(1 + 1, 2)
        print("✅ Basic test passed!")
    
    def test_jwt_flow(self):
        """Test JWT authentication"""
        print("\n🔐 Testing JWT Authentication...")
        
        try:
            # Get JWT token
            response = requests.post(
                'http://localhost:8000/api/token/',
                json={'username': 'seif', 'password': '1234'},
                timeout=10
            )
            print(f"Token Response: {response.status_code}")
            
            if response.status_code == 200:
                token = response.json()['access']
                print("✅ Token obtained successfully!")
                print(f"Token: {token}")
                
                
                # Test protected endpoint
                headers = {'Authorization': f'Bearer {token}'}
                api_response = requests.get(
                    'http://localhost:8000/api/employees/',
                    headers=headers
                )
                print(f"API Response: {api_response.status_code}")
                
                if api_response.status_code == 200:
                    data = api_response.json()
                    print(f"✅ Success! Found {data.get('count', 0)} employees")
                else:
                    print(f"❌ API call failed: {api_response.text}")
            else:
                print(f"❌ Token request failed: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Cannot connect to server! Run: python manage.py runserver")
        except Exception as e:
            print(f"❌ Error: {e}")