import sys

from dirwallthrough import walkthrough
from models import Actress, Movie, Tag
from dbcontroller import Session, create_db, query_movie, query_actress, query_tag

# path = "./video_test_dir"
path = "D:/a"


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "initdb":
        create_db()

    # walkthrough(path)

    # test

    # session = Session()

    # # Actress test
    # actress = session.query(Actress).filter_by(name="北川ゆず").first()
    # print(actress.movies[0].tags)
    #
    # # Tag test
    # all_tags = session.query(Tag).all()
    # tag = session.query(Tag).filter_by(text="北川").first()
    # print(all_tags)
    # print(tag.movies)
    #
    # # Movie test
    # print(session.query(Movie).filter(Movie.title.like("%AP-510%")).count())

    # query_result = query_movie()
    # for id in query_result.keys():
    #     print(query_result[id])
    # print(query_actress())
    # print(query_tag())
    # print(query_movie())