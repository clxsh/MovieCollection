from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from models import Actress, Tag, Movie

sql_address = "sqlite:///sqlite.db"

engine = create_engine(sql_address)
Session = sessionmaker(bind=engine)


def addtodb(movie_detail):
    session = Session()

    if session.query(Movie).filter_by(title=movie_detail["title"]).first() is not None:
        return

    name = movie_detail["actress"]  # only one actress supported
    actress = session.query(Actress).filter_by(name=name).first()
    if actress is None:
        actress = Actress(name=name)
        session.add(actress)

    tags = []
    for tagtext in movie_detail["tags"]:
        tag = session.query(Tag).filter_by(text=tagtext).first()
        if tag is None:
            tag = Tag(text=tagtext)
            session.add(tag)

        tags.append(tag)

    movie = Movie(title=movie_detail["title"], actress_id=actress.id, actress=actress,
                  cover_path=movie_detail["cover_path"], video_path=movie_detail["video_path"], tags=tags)

    session.add(movie)

    session.commit()


def query_movie(actress = None, tag=None):
    session = Session()

    if actress is not None:
        movies = session.query(Actress).filter_by(name=actress).first().movies

    elif tag is not None:
        movies = session.query(Tag).filter_by(text=tag).first().movies

    else:
        movies = session.query(Movie).all()

    movie_dict = dict()
    for movie in movies:
        movie_detail = dict()
        movie_detail["title"] = movie.title
        movie_detail["actress"] = movie.actress.name
        movie_detail["tags"] = [t.text for t in movie.tags]
        movie_detail["cover_path"] = movie.cover_path
        movie_detail["video_path"] = movie.video_path

        movie_dict[movie.id] = movie_detail

    return movie_dict


def query_actress():
    session = Session()

    actresses = session.query(Actress).all()
    actress_list = [actress.name for actress in actresses if actress.name != ""]
    actress_list.append("未知姓名")

    return actress_list


def query_tag():
    session = Session()

    tags = session.query(Tag).all()
    tag_list = [tag.text for tag in tags]

    return tag_list


def create_db():
    """
    init_db
    """

    from dbcontroller import engine
    from models import Base

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
