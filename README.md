# Media Tracker

The application allows the user to browse series and movies, add them to their personal watchlist, as well as add reviews. Each user is a regular user or an admin.

## Application features

* The user/admin can log in and log out, as well as make a new account.
* The user/admin can browse series and movies.
* The user can add/remove shows to/from their personal watchlist.
* The user can view their personal watchlist to see the shows they have added.
* The user can rate and review shows, as well as read reviews made by other people.
* While browsing through shows, the user/admin can sort the shows based on various criteria, such as their title, ratings or release date.
* The user/admin can search for shows by title or genre.
* The admin can add and remove shows.
* The admin can add and remove genres.
* The admin can remove user reviews if necessary.

## Instructions for installation and use

### Requirements

* Python 3.9 or higher
* SQLite 3.35 or higher

### Installation

1. Clone this repository and move to its root directory:

```bash
git clone https://github.com/uyenmh/tsoha-media-tracker.git
cd tsoha-media-tracker
```

2. Create a secret key in Python:

```bash
import secrets
secrets.token_hex(16)
```

3. Create an .env file in the root directory and specify its content as follows:

```bash
DATABASE_NAME = media_tracker.db
SECRET_KEY=<secret-key>
```

4. Next, activate the virtual environment and install the application's dependencies using the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

5. Define the database schema with the command:

```bash
sqlite3 media_tracker.db < schema.sql
```

### Use

Activate the virtual environment with the command:

```bash
source venv/bin/activate
```

Launch the application with the command:

```bash
flask run
```

#### Admin functions

After the first startup, it's recommended that you create an admin account. To create a new account, click on "Login" at the top right corner. This leads to a login page, which has a "Register" button if you don't have an account yet. You'll be logged in automatically after registration.

You'll see an admin dashboard on the home page after logging in. You can add new shows through "Add new show", remove existing shows through "Remove show", and manage genres through "Manage genres". Shows will be listed below the admin dashboard as they are added.

An admin user can also remove reviews of regular users if necessary. To do this, click on any show. If there are reviews, you should be able to see a "Remove" button next to each of them.

#### Regular user functions

After creating a regular user account, you'll first see the home page, where all the shows are listed. Clicking on any show will lead you to a page with more details of the show. On that page, you can add shows to your watchlist by clicking "Add to my watchlist", review shows by choosing a rating, leaving an optional comment and clicking submit, and remove your own review by clickin "Remove" next to your review. If a show is already on your watchlist, you can remove it by clicking "Remove from my watchlist". Clicking "My watchlist" on the top right corner will show you a list of all the shows you've added to your watchlist.

On the home page, you can also search for shows by their title (doesn't need to be full title) or genre. You can also sort the shows by title, rating or release date.