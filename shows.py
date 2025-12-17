from sqlalchemy import text
from db import db

def get_all_shows(sort_by="Title"):
    if sort_by == "Rating":
        sql = text("""
            SELECT id, title
            FROM shows
            ORDER BY avg_rating DESC NULLS LAST
        """)
    elif sort_by == "Release date":
        sql = text("""
            SELECT id, title
            FROM shows
            ORDER BY release_date DESC
        """)
    else:
        sql = text("""
            SELECT id, title
            FROM shows
            ORDER BY title
        """)
    return db.session.execute(sql).fetchall()

def get_show_info(show_id):
    sql = text("""
        SELECT s.title, s.type, s.description, s.release_date
        FROM shows s
        WHERE s.id=:show_id
    """)
    result = db.session.execute(sql, {"show_id": show_id}).fetchone()
    return result

def add_show(title, show_type, description, release_date, genre_ids=None):
    sql = text("""
        INSERT INTO shows (title, type, description, release_date)
        VALUES (:title, :type, :description, :release_date)
        RETURNING id
    """)
    show_id = db.session.execute(
        sql, {
            "title": title,
            "type": show_type,
            "description": description,
            "release_date": release_date
        }
    ).fetchone()[0]

    if genre_ids:
        for genre_id in genre_ids:
            db.session.execute(
                text("""
                    INSERT INTO shows_genres (show_id, genre_id)
                    VALUES (:show_id, :genre_id)
                """),
                {"show_id": show_id, "genre_id": genre_id}
            )

    db.session.commit()
    return show_id

def remove_show(show_id):
    sql = text("""
        DELETE FROM shows_genres
        WHERE show_id=:show_id
    """)
    db.session.execute(sql, {"show_id": show_id})

    sql = text("""
        DELETE FROM watchlists
        WHERE show_id=:show_id
    """)
    db.session.execute(sql, {"show_id": show_id})

    sql = text("""
        DELETE FROM reviews
        WHERE show_id=:show_id
    """)
    db.session.execute(sql, {"show_id": show_id})

    sql = text("""
        DELETE FROM shows
        WHERE id=:id
    """)
    db.session.execute(sql, {"id": show_id})
    db.session.commit()

def get_reviews(show_id):
    sql = text("""
        SELECT r.id AS review_id,
               u.id AS user_id,
               u.name AS username,
               r.stars AS stars,
               r.comment AS comment
        FROM reviews r
        JOIN users u ON r.user_id = u.id
        WHERE r.user_id=u.id AND r.show_id=:show_id
        ORDER BY r.id
    """)
    return db.session.execute(sql, {"show_id": show_id}).fetchall()

def add_review(show_id, user_id, stars, comment):
    sql = text("""
        INSERT INTO reviews (show_id, user_id, stars, comment)
        VALUES (:show_id, :user_id, :stars, :comment)
    """)
    db.session.execute(sql, {"show_id": show_id, "user_id": user_id,
                             "stars": stars, "comment": comment})
    db.session.commit()

def remove_own_review(show_id, user_id):
    sql = text("""
        DELETE FROM reviews
        WHERE show_id=:show_id AND user_id=:user_id
    """)
    db.session.execute(sql, {"show_id": show_id, "user_id": user_id})
    db.session.commit()

def has_user_reviewed(show_id, user_id):
    sql = text("""
        SELECT COUNT(*)
        FROM reviews
        WHERE show_id=:show_id AND user_id=:user_id
    """)
    result = db.session.execute(sql, {"show_id": show_id, "user_id": user_id}).fetchone()
    return result[0] > 0

def remove_review_admin(review_id):
    sql = text("""
        DELETE FROM reviews
        WHERE id=:review_id
    """)
    db.session.execute(sql, {"review_id": review_id})
    db.session.commit()

def search_shows(keyword):
    sql = text("""
        SELECT DISTINCT s.id, s.title
        FROM shows s
        LEFT JOIN shows_genres sg ON s.id = sg.show_id
        LEFT JOIN genres g ON g.id = sg.genre_id
        WHERE s.title ILIKE :keyword
           OR g.name ILIKE :keyword
        ORDER BY s.title
    """)
    result = db.session.execute(sql, {"keyword": f"%{keyword}%"}).fetchall()
    return result

def calculate_avg_rating(show_id):
    sql = text("""
        SELECT AVG(stars)
        FROM reviews
        WHERE show_id=:show_id
    """)
    result = db.session.execute(sql, {"show_id": show_id}).fetchone()

    if result[0] is None:
        result = "N/A"
    else:
        result = round(result[0], 2)
        save_avg_rating(show_id, result)

    return result

def save_avg_rating(show_id, avg_rating):
    sql = text("""
        UPDATE shows
        SET avg_rating=:avg_rating
        WHERE id=:show_id
    """)
    db.session.execute(sql, {"avg_rating": avg_rating, "show_id": show_id})
    db.session.commit()

def add_genre(genre_name):
    sql = text("""
        INSERT INTO genres (name)
        VALUES (:genre_name)
    """)
    db.session.execute(sql, {"genre_name": genre_name})
    db.session.commit()

def remove_genre(genre_id):
    sql = text("""
        DELETE FROM shows_genres
        WHERE genre_id=:genre_id
    """)
    db.session.execute(sql, {"genre_id": genre_id})

    sql = text("""
        DELETE FROM genres
        WHERE id=:genre_id
    """)
    db.session.execute(sql, {"genre_id": genre_id})

    db.session.commit()

def get_all_genres():
    sql = text("""
        SELECT id, name
        FROM genres
        ORDER BY name
    """)
    return db.session.execute(sql).fetchall()

def get_show_genres(show_id):
    sql = text("""
        SELECT g.id, g.name
        FROM genres g
        JOIN shows_genres sg ON g.id = sg.genre_id
        WHERE sg.show_id = :show_id
        ORDER BY g.name
    """)
    return db.session.execute(sql, {"show_id": show_id}).fetchall()

def get_watchlist(user_id):
    sql = text("""
        SELECT s.id, s.title
        FROM watchlists w
        JOIN shows s ON w.show_id = s.id
        WHERE w.user_id = :user_id
        ORDER BY s.title
    """)
    return db.session.execute(sql, {"user_id": user_id}).fetchall()

def add_to_watchlist(user_id, show_id):
    sql = text("""
        INSERT INTO watchlists (user_id, show_id)
        VALUES (:user_id, :show_id)
    """)
    db.session.execute(sql, {"user_id": user_id, "show_id": show_id})
    db.session.commit()

def remove_from_watchlist(user_id, show_id):
    sql = text("""
        DELETE FROM watchlists
        WHERE user_id=:user_id AND show_id=:show_id
    """)
    db.session.execute(sql, {"user_id": user_id, "show_id": show_id})
    db.session.commit()

def is_in_watchlist(user_id, show_id):
    sql = text("""
        SELECT COUNT(*)
        FROM watchlists
        WHERE user_id=:user_id AND show_id=:show_id
    """)
    result = db.session.execute(sql, {"user_id": user_id, "show_id": show_id}).fetchone()
    return result[0] > 0
