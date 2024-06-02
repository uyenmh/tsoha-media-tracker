from db import db
from flask import abort, request, session
from sqlalchemy import text

def get_all_shows():
    sql = text("SELECT id, title FROM shows ORDER BY title")
    return db.session.execute(sql).fetchall()

def get_show_info(show_id):
    sql = text("""SELECT s.title, s.type, s.description, s.release_date FROM shows s
             WHERE s.id=:show_id""")
    result = db.session.execute(sql, {"show_id": show_id}).fetchone()
    return result
    
def add_show(title, type, description, release_date):
    sql = text("""INSERT INTO shows (title, type, description, release_date)
             VALUES (:title, :type, :description, :release_date) RETURNING id""")
    show_id = db.session.execute(sql, {"title": title, "type": type, "description": description, "release_date": release_date}).fetchone()[0]

    db.session.commit()
    return show_id
    
def remove_show(show_id):
    sql = text("DELETE FROM shows WHERE id=:id")
    db.session.execute(sql, {"id": show_id})
    db.session.commit()
 
#def get_reviews(show_id):
#    sql = text("""SELECT u.name, r.stars, r.comment FROM reviews r, users u
#             WHERE r.user_id=u.id AND r.show_id=:show_id ORDER BY r.id""")
#    return db.session.execute(sql, {"show_id": show_id}).fetchall()

#def add_review(show_id, user_id, stars, comment):
#    sql = text("""INSERT INTO reviews (show_id, user_id, stars, comment)
#             VALUES (:show_id, :user_id, :stars, :comment)""")
#    db.session.execute(sql, {"show_id": show_id, "user_id": user_id,
#                             "stars": stars, "comment": comment})
#    db.session.commit()
