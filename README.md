# Media Tracker

The application allows the user to browse series and movies, add them to their personal watchlist, as well as add reviews. Each user is a basic user or an admin. 

## Application features

* The user can log in and log out, as well as make a new account.
* The user can browse series and movies, and add them to their personal watchlist.
* The user can view their personal watchlist to see the shows they have added. 
* The user can rate and review shows, as well as read reviews made by other people.
* While browsing through shows, the user can sort the shows based on various criteria, such as their ratings or release date.
* The user can search for shows by title or other criteria (e.g. genre).
* The admin can add and remove shows.
* The admin can remove reviews if necessary. 

## Current status

* The user can log in and log out, as well as make a new account. Granted, anyone can also make an admin account, which will need to be fixed.
* The user can browse series and movies, but there is no watchlist function yet.
* There is also no sort function for the shows. 
* The user can rate and review shows, as well as read reviews made by other people.
* The user can also delete their own reviews.
* The admin can add and remove shows.
* The admin can remove reviews if necessary.

## Instructions for use

1. Clone this repository to your own device and move to its root directory. Create an .env file in the folder and specify its content as follows:

```bash
DATABASE_URL=<database-local-address>
SECRET_KEY=<secret-key>
```

2. Next, activate the virtual environment and install the application's dependencies using the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install -r ./requirements.txt
```

3. Define the database schema with the command:

```bash
psql < schema.sql
```

Launch the application with the command:

```bash
flask run
```
