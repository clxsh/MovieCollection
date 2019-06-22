import os
import xml.etree.ElementTree as etree

from dbcontroller import addtodb
# 存在.nfo文件 and 存在视频文件
# or 只存在视频文件

video_ext = [".mkv", ".mp4", ".wmv"]


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
                    movie_detail["actress"] = ""
                    movie_detail["tags"] = []

                cover_path = os.path.join(dirpath, split_name[0]+".png")
                if os.path.isfile(cover_path):
                    movie_detail["cover_path"] = cover_path
                else:
                    movie_detail["cover_path"] = ""

                movie_detail["title"] = split_name[0]
                movie_detail["video_path"] = os.path.join(dirpath, file_name)

                # print(movie_detail)
                addtodb(movie_detail)


# get actress and tags
# return an dict contains actress, tags list
def parse_nfo(filepath):
    tree = etree.parse(filepath)

    actress = tree.find("actor")[0].text
    tags = [tag.text for tag in tree.findall("tag")]

    return {"actress": actress, "tags": tags}