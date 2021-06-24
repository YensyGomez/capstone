# capstone
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

# URLs Heroku app:
[heroku-agency-capstone]( https://heroku-agency-capstone.herokuapp.com/)

[git-heroku-agency-capstone]( https://git.heroku.com/heroku-agency-capstone.git)

# Generate token: 
 
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

# Local Testing
## Set up
Create a testing database usg psql.

```bash
createdb captonedb_test
```
If the testing db was already created:

```bash
dropdb captonedb_test_test && createdb captonedb_test_test
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







