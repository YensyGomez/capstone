
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actors

# assigning env variables to contants
ASSISTANT_JWT = os.environ.get('ASSISTANT')
DIRECTOR_JWT = os.environ.get('DIRECTOR')
PRODUCER_JWT = os.environ.get('PRODUCER')

if not ASSISTANT_JWT and not DIRECTOR_JWT and not PRODUCER_JWT:
    ASSISTANT_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxLX2M0R3lfMWlFeUw3eGpBWGtQVSJ9.eyJpc3MiOiJodHRwczovL3llaGVnb3ZpNDUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwY2UyNGEyMmI5MjJiMDA2YTcxMGEyMiIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYyNDUzODQwMSwiZXhwIjoxNjI0NTQ1NjAxLCJhenAiOiJ3ZzZ0VjdrTWpNN0dwd2lPZGhIY3dqbEgyN2txVTExciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.ffmu2xtsVRw99UByzKaYDEBs75uHO1Wti9xGvtWQQHYTeiMWb5ilu4hkaNaQG42VcwyHYBpIM4_p4l0mNLPTlhpQ07y7ih1-ObQj64qujHEUCcfUdwq5-km_hv1zBgC7L09T2p6dUsLCtMMOTWMXXdml-furkO_-iVcGz17NbiW97rtNZTrAaHHs5A8Ir2f97wELZoNJqi1DD3UHnaYhmc-tM3XFAkvOXV62N8h_5-Q3AvMlwYeGTzBfQKO4zdwCJLEzgHCQV3OzrBZqlvC0ovAiiWUFC3cw66yn7JGBW6n61-GBgDJ_Kq_681h99vzBZyvKRh4WQX5hVLnpqdFd6g'
    DIRECTOR_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxLX2M0R3lfMWlFeUw3eGpBWGtQVSJ9.eyJpc3MiOiJodHRwczovL3llaGVnb3ZpNDUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwY2U0NGMzYjcyYTlmMDA2YTI4OWJkZSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYyNDUzODU1MCwiZXhwIjoxNjI0NTQ1NzUwLCJhenAiOiJ3ZzZ0VjdrTWpNN0dwd2lPZGhIY3dqbEgyN2txVTExciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.JQTwFPT53UGO4vfdAYIGR6My0mPfRVEYlpUSFzpuHjmFg36aX-3AeKA-mpXNT1UKgdsBPO52Ho9VE4U8g3gTrS3TO9xcJJZAiBD5Nx5LL4K8rKonc5ah0HNp__7ushSsm0bxSl1Ro5LNtMRefGYxwX4asnAIFr9mZHqJOABC1sap88bKvc20nR1jfHUb8ah_BA0k6Yk2g8ziL_689IbhFOwkjq3iT4Bg6abwSHsGnsn7JMw3qTdgSWSkvAlZozHRsdehCxbVGbHELgbPwgq9A_BPz5Ebx7SU3lg0qZurXuFOrRlqesd5rEaSi6Y7HHeey7WfIMZcPI915KOXNBcQ_A'
    PRODUCER_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxLX2M0R3lfMWlFeUw3eGpBWGtQVSJ9.eyJpc3MiOiJodHRwczovL3llaGVnb3ZpNDUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwY2U0NTQxMmI5MjJiMDA2YTcxMTE3ZCIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYyNDUzODYzNiwiZXhwIjoxNjI0NTQ1ODM2LCJhenAiOiJ3ZzZ0VjdrTWpNN0dwd2lPZGhIY3dqbEgyN2txVTExciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.jPr4vh1P4b047wwRg98SvNa6TfTLY1ohNzfA2srDn0C7RCcbdQAWj8OFQZbCFWfNTenzzcEqybUJENk3rsg4Ioz52Sfx8dBU37tYx4REXx2G16t0CktEmCgbeXjpr0J9QXdlqY4ZS-LGy9hejqmw9viFgEnsUcJa1p92nlUKd_jBKXW4WMoHyJHqrLKqJsuBHLeSHYpvMANLz0HQHyAS8TxqV_AtWtuD04sWnC3Kty_GNfZjtP77fyfc0PE0IErCWvMk-2nGlQ3wKAHHQvndN2atsWbl77jaU3fWZdVq4_4nFgfr3sKAMOeQWDkz9qXYTj2H5q4GjvfwYecx0Kyg1g'

def get_headers(token):
    return {'Authorization': f'Bearer {token}'}

class AgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstonedb_test"
        #self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_name)
        # self.database_path

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    # test and error tests for each enpoint (get, delete, post, patch)
    # Assistant get movies
    def test_get_movies(self):
        res = self.client().get('/movies', headers=get_headers(ASSISTANT_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_movies'])
        self.assertTrue(len(data['movies']))

    # Error Assistant get movie 
    def test_404_sent_requesting_non_existing_movies(self):
        res = self.client().get('/movies/9999', headers=get_headers(ASSISTANT_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    # Assistant get actors
    def test_get_actors(self):
        res = self.client().get('/actors', headers=get_headers(ASSISTANT_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    # Error Assistant get movie 
    def test_404_sent_requesting_non_existing_actors(self):
        res = self.client().get('/actors/9999', headers=get_headers(ASSISTANT_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    # Error Assistan create actor
    def test_create_new_actor_by_assistant(self):
        res = self.client().post('/actors',
            json={'name': 'Rachel McAdams','age': 41,'gender': 'Mujer'},
            headers=get_headers(ASSISTANT_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    # Insert actors by director
    def test_create_new_actor(self):
        res = self.client().post('/actors',
            json={'name': 'Rachel McAdams','age': 41,'gender': 'Mujer'},
            headers=get_headers(DIRECTOR_JWT))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_actors'])
        self.assertTrue(len(data['actors']))

    #Error create new actor.
    def test_error_create_actor(self):
        res = self.client().post('/actors/200',
            json={'name': 'Penelope Cruz', 'age': 36,'gender': 'Mujer'},
            headers=get_headers(DIRECTOR_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')
    
    #update actor 
    def test_update_actor(self):
        res = self.client().patch('/actors/6',
                                  json={'name': 'Pedro Infante'},
                                  headers=get_headers(DIRECTOR_JWT))
        data = json.loads(res.data)
     
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #Error update actor
    def test_error_update_actor(self):
        res = self.client().patch('/actors/1000',
            json={'age': 50},
            headers=get_headers(DIRECTOR_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    #update Movie
    def test_update_movie(self):
        res = self.client().patch('/movies/3',
                                  json={'release_date': '11-11-2015'},
                                  headers=get_headers(DIRECTOR_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    #Error update movie
    def test_error_update_movie(self):
        res = self.client().patch('/movies/1000',
                                  json={'release_date': '11-11-2015'},
                                  headers=get_headers(DIRECTOR_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')
    
    def test_create_new_movie(self):
        res = self.client().post(
            '/movies',
            json={'title': 'Aguilas descalzas','release_date': '10-30-2018'},
            headers=get_headers(PRODUCER_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['movies']))

    def test_error_create_new_movie(self):
        res = self.client().post(
            '/movies/200',
            json={'title': 'Mi mamá tambien', 'release_date': '01-12-1976'},
            headers=get_headers(PRODUCER_JWT))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
