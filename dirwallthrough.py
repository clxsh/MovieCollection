import os
from enum import Enum
import xml.etree.ElementTree as etree

from dbcontroller import addtodb, Session
from models import Tag, Movie
# 存在.nfo文件 and 存在视频文件
# or 只存在视频文件

video_ext = [".mkv", ".mp4", ".wmv", ".avi"]


# dict{title:, actress:, tags:, video_path:, cover_path:}
def walkthrough(path):
    # dirpath：当前文件夹路径(绝对相对看给出的路径) dirname：当前文件夹下面所有文件夹列表 files：当前文件夹下面所有文件列表
    for dirpath, dirname, files in os.walk(path):
        for file_name in files:
            split_name = os.path.splitext(file_name)
            if split_name[1] in video_ext:
                movie_detail = {}

                nfo_path = os.path.join(dirpath, split_name[0]+".nfo")
                if os.path.isfile(nfo_path):
                    movie_detail = parse_nfo(nfo_path)
                else:
                    create_nfo(nfo_path)
                    movie_detail["actress"] = ""
                    movie_detail["tags"] = []

                cover_path = os.path.join(dirpath, split_name[0]+".png")
                if os.path.isfile(cover_path):
                    with open(cover_path, "rb") as f:
                        movie_detail["cover"] = f.read()
                else:
                    movie_detail["cover"] = None

                movie_detail["title"] = split_name[0]
                movie_detail["video_path"] = os.path.join(dirpath, file_name)

                # print(movie_detail)
                addtodb(movie_detail)


# get actress and tags
# return an dict contains actress, tags list
def parse_nfo(filepath):
    tree = etree.parse(filepath)

    actress = tree.find("actor")[0].text
    if actress is not None:
        actress = actress.strip()
    if actress == None:
        actress = ""
    tags = [tag.text for tag in tree.findall("tag")]

    return {"actress": actress, "tags": tags}


def create_nfo(nfopath):
    movie = etree.Element("movie")
    actor = etree.SubElement(movie, "actor")
    name = etree.SubElement(actor, "name")
    name.text = ""

    tree = etree.ElementTree(movie)
    tree.write(nfopath, "UTF-8")


def addtonfo(nfopath, tagtext):
    tree = etree.parse(nfopath)
    root = tree.getroot()

    tags = [tag.text for tag in tree.findall("tag")]
    if tagtext not in tags:
        element = etree.Element("tag")
        element.text = tagtext

        root.append(element)
        tree.write(nfopath, "UTF-8")
    


def delfromnfo(nfopath, tagtext):
    tree = etree.parse(nfopath)
    root = tree.getroot()

    for tag in tree.findall("tag"):
        if tag.text == tagtext:
            root.remove(tag)
            tree.write(nfopath, "UTF-8")
            return


class MType(Enum):
    ADD = 0
    DEL = 1

"""
type: manipulate type(add a tag or del a tag from a movie)
movie_id: as name suggests
tagtext: the tag to manipulate
"""
def alter_tag(type, movie_id, tagtext):
    session = Session()
    # tags表中存在与否， 添加到movie表中， 添加到.nfo
    if type == MType.ADD:
        tag = session.query(Tag).filter_by(text=tagtext).first()
        if tag is None:
            tag = Tag(text=tagtext)
            session.add(tag)

        movie = session.query(Movie).filter_by(id=movie_id).first()
        if tag not in movie.tags:
            movie.tags.append(tag)
            session.add(movie)

            session.commit()

        addtonfo(os.path.join(os.path.dirname(movie.video_path), movie.title + ".nfo"), tagtext)
    
    # 从movies表中删除关系，自.nfo文件删除
    if type == MType.DEL:
        tag = session.query(Tag).filter_by(text=tagtext).first()
        movie = session.query(Movie).filter_by(id=movie_id).first()
        movie.tags.remove(tag)

        session.add(movie)
        session.commit()

        tag = session.query(Tag).filter_by(text=tagtext).first()
        print("alter_tag: ")
        print(tag.movies)
        if len(tag.movies) == 0:
            session.delete(tag)
            session.commit()

        delfromnfo(os.path.join(os.path.dirname(movie.video_path), movie.title + ".nfo"), tagtext)
        