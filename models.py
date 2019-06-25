from sqlalchemy import Column, Integer, String, ForeignKey, Table, BLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Actress(Base):
    __tablename__ = "actresses"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    movies = relationship("Movie", back_populates="actress") # movies  back_populates from Movie

    def __repr__(self):
        return "<Actress (name: {})>".format(self.name)


movie_tags = Table("movie_tags", Base.metadata,
    Column('movie_id', ForeignKey("movies.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True)
)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    actress_id = Column(Integer, ForeignKey("actresses.id"))
    actress = relationship("Actress", back_populates="movies")
    # cover_path = Column(String)
    cover = Column(BLOB)
    video_path = Column(String)

    tags = relationship("Tag",
                        secondary=movie_tags,
                        back_populates="movies")

    def __repr__(self):
        return "<Movie (title: {}, actress: {}), tags: {}>".format(self.title, self.actress.name, self.tags)
    

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    text = Column(String, unique=True)

    movies = relationship("Movie", 
                          secondary=movie_tags,
                          back_populates="tags")

    def __repr__(self):
        return "<Tag (text: {})>".format(self.text)