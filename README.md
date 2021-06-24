# capstone
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

# URLs Heroku app:
[heroku-agency-capstone]( https://heroku-agency-capstone.herokuapp.com/)

[git-heroku-agency-capstone]( https://git.heroku.com/heroku-agency-capstone.git)

# Generate token heroku: 
 
```bash
https://yehegovi45.eu.auth0.com/authorize?audience=agency&response_type=token&client_id=wg6tV7kMjM7GpwiOdhHcwjlH27kqU11r&redirect_uri=https://heroku-agency-capstone.herokuapp.com
```
# Rol account:
## Assistant:

email: [assistant@myagency.com](mailto:assistant@casting.com)

Password: Ftg&*901

## Director:

email:[director@myagency.com](mailto:director@casting.com)

Password: Ftg&*901

## Producer:

email:producer@myagency.com

Password:Ftg&*901

# Getting Started
## Installing Dependencies
## Virtual Enviornment
I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. 

## PIP Dependencies
Once the virtual environment is setup and running, install dependencies by navigating to the working project directory and running:

```bash
pip install -r requirements.txt
```
# Running the local server 

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
# Authentication:

## Permissions: 
get:actors: get actors
post:actors: create a new actor
patch:actors: modify an existing actor
delete:actors: delete an actor
get:movies: get movies
post:movies: create a new movie
patch:movies: modify an existing movie
delete:movies: delete a movie

## Roles Permissions:
### Assistant:
1.Casting Assistant
 * Can view actors and movies.
 * Has permissions:
   * get:actors: get actors
   * get:movies: get movies
2. Casting Director
 * All permissions a Casting Assistant has and…
 * Add or delete an actor from the database
 * Modify actors or movies
 * Has permissions:
   * delete:actors
   * get:actors
   * get:movies
   * patch:actors
   * patch:movies
   * post:actors
3. Executive Producer
 * All permissions a Casting Director has and…
 * Add or delete a movie from the database
 * Has permissions:
   * delete:actors
   * delete:movies
   * get:actors
   * get:movies	
   * patch:actors
   * patch:movies	
   * post:actors
   * post:movies

# Generate Local Token:

```bash
https://yehegovi45.eu.auth0.com/authorize?audience=agency&response_type=token&client_id=wg6tV7kMjM7GpwiOdhHcwjlH27kqU11r&redirect_uri=http://127.0.0.1:5000/movies
```
# Local Testing
## Set up
Create a testing database using psql.

```bash
createdb capstonedb_test
```
If the testing db was already created:

```bash
dropdb capstonedb_test && createdb capstonedb_test
psql capstonedb_test < capstonedb.sql 
```
Make sure the environment variables are set:

```bash
source setup.sh
```
Run the tests
To test the local install, run the following command from the root folder.
```bash
python test_app.py

```

# Endpoins
## GET '/movies'

* First checks that the token provided is allowed to perform this operation. If authorized, then fetches a dictionary of movies.
* Request Arguments: token
* Returns: Each object in the movies dictionary and an object showing the total number of movies.
```json
{
    "movies": [
        {
            "id": 5,
            "release_date": "Tue, 30 Oct 2018 00:00:00 GMT",
            "title": "Aguilas descalzas"
        },
        {
            "id": 3,
            "release_date": "Wed, 11 Nov 2015 00:00:00 GMT",
            "title": "Amor indio"
        },
        {
            "id": 4,
            "release_date": "Thu, 12 Oct 1950 00:00:00 GMT",
            "title": "Amor mio"
        },
        {
            "id": 1,
            "release_date": "Mon, 12 Nov 1990 00:00:00 GMT",
            "title": "selena"
        },
        {
            "id": 2,
            "release_date": "Tue, 12 Oct 1999 00:00:00 GMT",
            "title": "spawn"
        }
    ],
    "success": true,
    "total_movies": 5
}

```
## Get Actors

* First checks that the token provided is allowed to perform this operation. If authorized, then fetches a dictionary of actors.
* Request Arguments: token
* Returns: Each object in the actors dictionary and an object showing the total number of actors.
```json
{
    "actors": [
        {
            "age": 36,
            "gender": "Hombre",
            "id": 2,
            "name": "Gael Garcia"
        },
        {
            "age": 50,
            "gender": "Mujer",
            "id": 3,
            "name": "jennifer Lopez"
        },
        {
            "age": 50,
            "gender": "Hombre",
            "id": 4,
            "name": "John Leguisamo"
        },
        {
            "age": 32,
            "gender": "Hombre",
            "id": 1,
            "name": "Pedro Navajas"
        },
        {
            "age": 41,
            "gender": "Mujer",
            "id": 5,
            "name": "Rachel McAdams"
        }
    ],
    "success": true,
    "total_actors": 5
} 
```

# Delete Actors

* First checks that the token provided is allowed to perform this operation. If authorized, then takes in a actor ID, if the actor exists, then it is deleted from the database
* Request Arguments: token, actor_id
* Returns: The ID of the deleted actor and each object in the list of modified actors and an object showing the total number of actors.
```json
{
    "actors": [
        {
            "age": 36,
            "gender": "Hombre",
            "id": 2,
            "name": "Gael Garcia"
        },
        {
            "age": 50,
            "gender": "Mujer",
            "id": 3,
            "name": "jennifer Lopez"
        },
        {
            "age": 50,
            "gender": "Hombre",
            "id": 4,
            "name": "John Leguisamo"
        },
        {
            "age": 41,
            "gender": "Mujer",
            "id": 5,
            "name": "Rachel McAdams"
        }
    ],
    "deleted": 1,
    "success": true,
    "total_actors": 4
}
```


# Delete Movies

* First checks that the token provided is allowed to perform this operation. If authorized, then takes in a movie ID, if the movie exists, then it is deleted from the database
* Request Arguments: token, movie_id
* Returns: The ID of the deleted movie and each object in the list of modified movies and an object showing the total number of movies.

```json
{
    "deleted": 1,
    "movies": [
        {
            "id": 2,
            "release_date": "Tue, 12 Oct 1999 00:00:00 GMT",
            "title": "spawn"
        },
        {
            "id": 3,
            "release_date": "Wed, 11 Nov 2015 00:00:00 GMT",
            "title": "Amor indio"
        },
        {
            "id": 4,
            "release_date": "Thu, 12 Oct 1950 00:00:00 GMT",
            "title": "Amor mio"
        },
        {
            "id": 5,
            "release_date": "Tue, 30 Oct 2018 00:00:00 GMT",
            "title": "Aguilas descalzas"
        }
    ],
    "success": true,
    "total_movies": 4
}

```

# Patch Movie

* First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the desired fields to be changes.
* Request Arguments: token, movie_id
* Returns: An object containing the updated movie.

```json

{
    "movie": {
        "id": 5,
        "release_date": "Tue, 30 Oct 2018 00:00:00 GMT",
        "title": "Aguilas descalzas extreno 2 "
    },
    "success": true
}
```

# Patch Actors:


* First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the desired fields to be changes.
* Request Arguments: token, actor_id
* Returns: An object containing the updated actor.
```json
{
    "actor": {
        "age": 40,
        "gender": "Hombre",
        "id": 4,
        "name": "John Leguisamo "
    },
    "success": true
}
```

# Post Actors

* First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the new actor namely the name, age and gender.
* Request Arguments: token
* Returns: An object containing the newly created actors's id, each object in the list of modified actors and an object showing the total number of actors.
```json
{
    "actors": [
        {
            "age": 36,
            "gender": "Hombre",
            "id": 2,
            "name": "Gael Garcia"
        },
        {
            "age": 50,
            "gender": "Mujer",
            "id": 3,
            "name": "jennifer Lopez"
        },
        {
            "age": 40,
            "gender": "Hombre",
            "id": 4,
            "name": "John Leguisamo "
        },
        {
            "age": 41,
            "gender": "Mujer",
            "id": 5,
            "name": "Rachel McAdams"
        },
        {
            "age": 34,
            "gender": "Hombre",
            "id": 6,
            "name": "Jose Lopez "
        }
    ],
    "created": 6,
    "success": true,
    "total_actors": 5
}
```

# Post Movie

* First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the new movie namely the title and release_date.
* Request Arguments: token
* Returns: An object containing the newly created movie's id, each object in the list of modified movies and an object showing the total number of movies.
```json
{
    "created": 6,
    "movies": [
        {
            "id": 2,
            "release_date": "Tue, 12 Oct 1999 00:00:00 GMT",
            "title": "spawn"
        },
        {
            "id": 3,
            "release_date": "Wed, 11 Nov 2015 00:00:00 GMT",
            "title": "Amor indio"
        },
        {
            "id": 4,
            "release_date": "Thu, 12 Oct 1950 00:00:00 GMT",
            "title": "Amor mio"
        },
        {
            "id": 5,
            "release_date": "Tue, 30 Oct 2018 00:00:00 GMT",
            "title": "Aguilas descalzas extreno 2 "
        },
        {
            "id": 6,
            "release_date": "Thu, 30 Oct 1986 00:00:00 GMT",
            "title": "la vida es mia y solo mia "
        }
    ],
    "success": true,
    "total_movies": 5
}
```







