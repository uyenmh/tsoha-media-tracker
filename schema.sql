CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT,
    role INTEGER
);

CREATE TABLE shows (
    id SERIAL PRIMARY KEY,
    title TEXT UNIQUE,
    type TEXT,
    description TEXT,
    release_date DATE
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    show_id INTEGER REFERENCES shows,
    stars INTEGER,
    comment TEXT
);

CREATE TABLE watchlists (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    show_id INTEGER REFERENCES shows,
    time_added TIMESTAMP
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE shows_genres (
    PRIMARY KEY (show_id, genre_id),
    show_id INTEGER REFERENCES shows,
    genre_id INTEGER REFERENCES genres
);
