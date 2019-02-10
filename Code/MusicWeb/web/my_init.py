
from web.models import Song
import os
import json
#coding:utf-8


def setup():
    cwd = os.getcwd()  # Get the current working directory (cwd)

    path = "./static/resources/"
    dirs = os.listdir(path)
    '''
    if Song.objects.exists():
        print("Song.objects.exists()")
        Song.objects.all().delete()
'''
    if not Song.objects.exists():
        for i in dirs:
            if os.path.splitext(i)[1] == ".json":  # 筛选json文件
                with open(path + i) as f:
                    data = json.load(f)
                    print("Loading: "+ data['Domain']+" : "+ data['SongID'])
                    Song.objects.create(SongID=data['SongID'],Domain= data['Domain'],
                                        AlbumName=data['AlbumName'], SingerName=data['SingerName'],
                                        SongName=data['SongName'], SongPath= "/static/resources/"+ data['SongPath'],
                                        AlbumImgPath= "/static/resources/"+ data['AlbumImgPath'], Lyrics=data['Lyrics'],
                                        )

    else: #已经存在了
        print("")
        #Song.objects.all().delete()