from db import db
from flask import abort, request, session
from sqlalchemy import text

def get_all_shows():
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
    
def add_show(title, type, description, release_date):
    sql = text("""
        INSERT INTO shows (title, type, description, release_date)
        VALUES (:title, :type, :description, :release_date)
        RETURNING id
    """)
    show_id = db.session.execute(sql, {"title": title, "type": type, "description": description, "release_date": release_date}).fetchone()[0]

    db.session.commit()
    return show_id
    
def remove_show(show_id):
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
        SELECT id, title
        FROM shows
        WHERE title ILIKE :keyword
        ORDER BY title
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

    return result