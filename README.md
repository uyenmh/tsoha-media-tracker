# Media Tracker

The application allows the user to browse series and movies, add them to their personal watchlist, as well as add reviews. Each user is a regular user or an admin.

## Application features

* The user/admin can log in and log out, as well as make a new account.
* The user can browse series and movies, and add them to their personal watchlist.
* The user can view their personal watchlist to see the shows they have added.
* The user can rate and review shows, as well as read reviews made by other people.
* While browsing through shows, the user can sort the shows based on various criteria, such as their title, ratings or release date.
* The user can search for shows by title or genre.
* The admin can add and remove shows.
* The admin can remove reviews if necessary.

## Instructions for installation and use

### Installation

1. Clone this repository to your own device and move to its root directory. Create an .env file in the directory and specify its content as follows:

```bash
DATABASE_URL=<database-local-address>
SECRET_KEY=<secret-key>
```

2. Next, activate the virtual environment and install the application's dependencies using the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```

3. Define the database schema with the command:

```bash
psql < schema.sql
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

You'll see an admin dashboard on the home page after logging in. You can add new shows through "Add new show", remove existing shows through "Remove show", and add and view genres through "Manage genres". Shows will be listed below the admin dashboard as they are added.

An admin user can also remove reviews of regular users if necessary. To do this, click on any show. If there are reviews, you should be able to see a "Remove" button next to each of them.

#### Regular user functions

After creating a regular user account, you'll first see the home page, where all the shows are listed. Clicking on any show will lead you to a page with more details of the show. On that page, you can add shows to your watchlist by clicking "Add to my watchlist", review shows by choosing a rating, leaving an optional comment and clicking submit, and remove your own review by clickin "Remove" next to your review. If a show is already on your watchlist, you can remove it by clicking "Remove from my watchlist". Clicking "My watchlist" on the top right corner will show you a list of all the shows you've added to your watchlist.

On the home page, you can also search for shows by their title (doesn't need to be full title) or genre. You can also sort the shows by title, rating or release date.