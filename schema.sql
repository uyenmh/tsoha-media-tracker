CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE shows (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE,
    type TEXT,
    description TEXT,
    release_date DATE,
    avg_rating REAL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    show_id INTEGER REFERENCES shows(id),
    stars INTEGER,
    comment TEXT
);

CREATE TABLE watchlists (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    show_id INTEGER REFERENCES shows(id)
);

CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE shows_genres (
    show_id INTEGER REFERENCES shows(id),
    genre_id INTEGER REFERENCES genres(id),
    PRIMARY KEY (show_id, genre_id)
);
