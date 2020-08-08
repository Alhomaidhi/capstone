
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import os

from models import setup_db,Movie, Actor
from app import create_app


class CastingTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path_test = os.getenv('database_path_test')
        setup_db(self.app, self.database_path_test)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    '''
    Commented out 404 tests require an empty database
    '''
    
    def test_get_movies(self):
        """Test movies returning """
        res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NTNkYzY4MjYwMGEwYjY5MGQ1IiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI3OTMsImV4cCI6MTU5NjkwOTE5MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.F6mOEvgSjHbBXa2NBykDzCJeAPNH2cnex2h7DBNJ300W2JAdiNoqqobyprFETF-R0xaAzVnvXrLZloL9aOcmvAZ-SEL-YG53lpoUFRukx9I3IkCYcbB3uLCFBm1DS3N3PHjyNJkmczmhwtGdM5HPuueR4jtor4Vatx3HttbCNI854_Otdr0G328wisRATWyDOWE620eD7bvvz5WK7fLKhDnm-kkAjTfXvk7NqVOp-j52ihSmpRjoP7pL62SyeUHFgHboa-i_RAxfbpiLzxzXxOGeLhTy_vWaae8RPUQ7yE0x6-p_pJT0nv1Ftf4pFB582on-G-mpVBETYRc6WYXaCA'})

        self.assertEqual(res.status_code, 200)

    # def test_404_get_movies(self):
    #     """Test 404 in movies"""
    #     res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})

    #     self.assertEqual(res.status_code, 404)

    def test_movies_delete(self):
        """Test movies deleting """
        id = 57 #enter valid id here before running the test
        res = self.client().delete('/movies/'+str(id), headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], id)

    def test_404_movies_delete(self):
        """Test 404 in deleting movies"""
        res = self.client().delete('/movies/100', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        
        self.assertEqual(res.status_code, 404)

    def test_movies_post(self):
        """Test in adding movies"""
        res = self.client().post('/movies', json={"title": "Scary Movie","release_date": "2002"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        data = json.loads(res.data)
        self.question_id = data['created']
        
        self.assertEqual(res.status_code, 200)

    def test_422_movies_post(self):
        """Test in adding movies wrong object"""
        res = self.client().post('/movies', json={"title": "Scary Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})

        self.assertEqual(res.status_code, 422)

    def test_movies_patch(self):
        """Test in adding movies"""
        id = 56   # enter valid id here before running the test
        res = self.client().patch('/movies/'+str(id), json={"title": "Scary Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)

    def test_404_movies_patch(self):
        """Test in adding movies wrong object"""
        res = self.client().patch('/movies/900', json={"title": "Scary Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NzZkYzY4MjYwMGEwYjY5MGRhIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI1OTYsImV4cCI6MTU5NjkwODk5NiwiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.gJWMG59mnYOFXm-phNQxTKoWceH6Q4OlyB4K3fj5_CzsCTLjqpLsKAHrNiAPDXe7ZO2E_wpa9XaSUEQNyMcmgs8MOgOxp7LdrlkDLQOO5Hr0zx8Yj-csqvTJoChgQ3qnzq7atoSi8azXEgQb-mpGWJsx7XuEo3RBR5Al3ROoDDpAdbF-mqukKHstT7l2IZV9uz0nba_vSyRONUlKpeGQISjB44z1embRVUdMQ3hfrKFe_RZ6egxjsvF39y58xGY5fCNkpU8JAzO_OaiRCJv3IY7pZfOvsTedW3uY2B7cnidVts31WvP-vxT0C9m39SimPoz3rmI0L4B41ETcwSjAUw'})

        self.assertEqual(res.status_code, 404)

    def test_get_actors(self):
        """Test actors returning """
        res = self.client().get('/actors', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NTNkYzY4MjYwMGEwYjY5MGQ1IiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI3OTMsImV4cCI6MTU5NjkwOTE5MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.F6mOEvgSjHbBXa2NBykDzCJeAPNH2cnex2h7DBNJ300W2JAdiNoqqobyprFETF-R0xaAzVnvXrLZloL9aOcmvAZ-SEL-YG53lpoUFRukx9I3IkCYcbB3uLCFBm1DS3N3PHjyNJkmczmhwtGdM5HPuueR4jtor4Vatx3HttbCNI854_Otdr0G328wisRATWyDOWE620eD7bvvz5WK7fLKhDnm-kkAjTfXvk7NqVOp-j52ihSmpRjoP7pL62SyeUHFgHboa-i_RAxfbpiLzxzXxOGeLhTy_vWaae8RPUQ7yE0x6-p_pJT0nv1Ftf4pFB582on-G-mpVBETYRc6WYXaCA'})

        self.assertEqual(res.status_code, 200)

    # def test_404_get_actors(self):
    #     """Test 404 in actors"""
    #     res = self.client().get('/actors', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})

    #     self.assertEqual(res.status_code, 404)

    def test_actors_delete(self):
        """Test actors deleting """
        id = 3   # enter valid id here before running the test
        res = self.client().delete('/actors/'+str(id), headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], id)

    def test_404_actors_delete(self):
        """Test 404 in deleting actors"""
        res = self.client().delete('/actors/100', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        
        self.assertEqual(res.status_code, 404)

    def test_actors_post(self):
        """Test in adding actors"""
        res = self.client().post('/actors', json={"name": "Abdullah","age": "23", "gender": "male"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)

    def test_422_actors_post(self):
        """Test in adding actors wrong object"""
        res = self.client().post('/actors', json={"name": "Abdullah"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})

        self.assertEqual(res.status_code, 422)

    def test_actors_patch(self):
        """Test in adding actors"""
        id = 2 #enter valid id here before running the test
        res = self.client().patch('/actors/'+str(id), json={"name": "Abdullah"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NzZkYzY4MjYwMGEwYjY5MGRhIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI1OTYsImV4cCI6MTU5NjkwODk5NiwiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.gJWMG59mnYOFXm-phNQxTKoWceH6Q4OlyB4K3fj5_CzsCTLjqpLsKAHrNiAPDXe7ZO2E_wpa9XaSUEQNyMcmgs8MOgOxp7LdrlkDLQOO5Hr0zx8Yj-csqvTJoChgQ3qnzq7atoSi8azXEgQb-mpGWJsx7XuEo3RBR5Al3ROoDDpAdbF-mqukKHstT7l2IZV9uz0nba_vSyRONUlKpeGQISjB44z1embRVUdMQ3hfrKFe_RZ6egxjsvF39y58xGY5fCNkpU8JAzO_OaiRCJv3IY7pZfOvsTedW3uY2B7cnidVts31WvP-vxT0C9m39SimPoz3rmI0L4B41ETcwSjAUw'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)

    def test_404_actors_patch(self):
        """Test in adding actors wrong object"""
        res = self.client().patch('/actors/900', json={"name": "Abdullah"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4OWNjMTNiMTMwMjI4Zjg3YzBiIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MTQ0ODMsImV4cCI6MTU5NjkwMDg4MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.YMiWHnLit67mPlssndY4NOh3-1WtUfTVm_LfoS0F3mymmwt7zrDPEe5_JLRpqDCddcxFKNHlHZAkCVR04tkxoB2JIIuHG2XHXTj8lW4g3cg-9GQOBE5uniJRnqZFSUvuKLMMlrdyn_D_Ru6A0xOViLF-I3NLnBgPzislW0v916evKhy3piQRfENUnmndvt8_ybd4Q52JScP5YZ3mJ-27wrl-bxXDNgNt2MAe9g5sTIJze8ie12RwTEgo7pjZOJ-afuwlVyBCTBLt9ykCC2RRoxdpt03jYbGj7wXqD2VxiVImJ6ueP1W1jyGBhME1-RJLzn4tQL2X-3FtoiRcqgRQSQ'})

        self.assertEqual(res.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
    