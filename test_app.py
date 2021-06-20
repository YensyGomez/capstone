
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actors

ASSISTANT_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxLX2M0R3lfMWlFeUw3eGpBWGtQVSJ9.eyJpc3MiOiJodHRwczovL3llaGVnb3ZpNDUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwY2UyNGEyMmI5MjJiMDA2YTcxMGEyMiIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYyNDE5MDY5MCwiZXhwIjoxNjI0MTk3ODkwLCJhenAiOiJ3ZzZ0VjdrTWpNN0dwd2lPZGhIY3dqbEgyN2txVTExciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.OXirBVace7KyWkOYYFsUoDHGBD_gaH7kY1WmXYYrOLUQdSbk8OA12uQvZEjihnTu8j8hIVBn7o3sq-2v8g6CbrL45R7b9ybns5aMKaNXcXEOgvda-EBmD71wkAsAtY6uuqhpkvM51Z8JyOk5lw06I0J5mWW9WJceZmOa2rdkr_nuN3gwihEfwdGykKhnCbPIbiq-2OckFToPN663C9FtDUWtH9Y04KXhIDHjBLqEzGAYumi9fW7OWV6_iDOIa9thxTn9B0AriD0IdFVst-rtQTUN3_trpEb8O75hDzkaHoy9Y7nSPP0UPQSMANp66XCTznsRC3TA3M6OjgAUU3y3uw'
DIRECTOR_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxLX2M0R3lfMWlFeUw3eGpBWGtQVSJ9.eyJpc3MiOiJodHRwczovL3llaGVnb3ZpNDUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwY2U0NGMzYjcyYTlmMDA2YTI4OWJkZSIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYyNDE5NTM1OSwiZXhwIjoxNjI0MjAyNTU5LCJhenAiOiJ3ZzZ0VjdrTWpNN0dwd2lPZGhIY3dqbEgyN2txVTExciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.XYPBYSBzG9HB_uiLLkKiGz33xbJei7AYHhSiK2CdUNrfna6OpBYqa9aldffXBzS5QnpSNISKCTWhVM-W7XMsnBpdfld2ZGiwvrbXsTonSfjD7WAHI-CwuBfhsogFH_-VZQFEkZHiM77oh9DThPQc3uD1rE64ymVdhzGVGfWa8uCtb00_ELd9TqgxkqN32dXDWjX3nTn0WtCv2Op6OpDzhRPIeWCC3Xn8Hbqm6_L-dII0BQtBZ6W_-AwcaC0WwE4ADzLyVQb4uyPqEwWJCaVSuLoThy50bkEcraUtZGLOvsEjEHnAB_GxaiM-oQofHJ2QQklYskGGkOFBM-glSkLFdQ'
PRODUCER_JWT = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxLX2M0R3lfMWlFeUw3eGpBWGtQVSJ9.eyJpc3MiOiJodHRwczovL3llaGVnb3ZpNDUuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwY2U0NTQxMmI5MjJiMDA2YTcxMTE3ZCIsImF1ZCI6ImFnZW5jeSIsImlhdCI6MTYyNDE5NDU0MiwiZXhwIjoxNjI0MjAxNzQyLCJhenAiOiJ3ZzZ0VjdrTWpNN0dwd2lPZGhIY3dqbEgyN2txVTExciIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.SADYgORlYBtCKNE7VcsbWG9lQ0zeM9eV9-CB5vig10Jhd8PTVeSsdLlKK_LFY0F-WKYKHbVqBoMvSahgs1PJ7Z6p_-GtQv2dJq0vyWiEF_6D5moqyNb_t9EbIzxQERDA1AR2bShefmn4hc1ml8-bsr942pTJd8I_jW6JkMLE2GrRQWpRTBFtEwET1zyXGTjG8Eu-AHDBNaReGXMmWSC0235ceDuQ0J4pNFEFzkW-FnTmUdt08WYWxaxINi4wq3hpZGgAciC_xthLexwAJ6tuqBzP_-o23wgij2yUpPO_Bz713dxNnmJ9tmajSZalW9O5mrE7zIr3SgJiKSuufiHv-g'

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
        print(data)

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
        print(data)

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
