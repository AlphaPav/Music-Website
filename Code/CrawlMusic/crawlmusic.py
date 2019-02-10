import requests,os,json,re
from scrapy.selector import Selector
from urllib import request
import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
import urllib, time
from pydub import AudioSegment

class song:
    SongID=""
    Domain= ""
    AlbumName=""
    SingerName=""
    SongName = ""
    AlbumImgPath=""
    AlbumImgOnlinePath = ""
    SongPath=""
    Lyrics=""


class NetEaseMusic():
    def __init__(self):
        self.headers = {
            'Host': 'music.163.com',
            'Referer': 'https://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }
        self.main_url='http://music.163.com/'
        self.session = requests.session()
        self.session.headers.update(self.headers)

    def get_songids(self,playlist):
        url=self.main_url+'playlist?id=%d'% playlist
        r = self.session
        r = BeautifulSoup(r.get(url, headers=self.headers).content, "html.parser")
        result = r.find('ul', {'class': 'f-hide'}).find_all('a')
        mysongs = []
        #count=1
        for music in result:
            #count+=1

            song_id = music['href'].strip("/song?id=")
            mysongs.append(song_id)



        return mysongs   #所有歌曲id组成的list

    def save_img(self,url,file_name):
        img= requests.get(url)
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, ' Save and convert image into png successfully!')
        f.close()


    def sava_song(self,song_id):
        try:
            song_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % song_id
            song_name= '%s.mp3' % song_id
            urllib.request.urlretrieve(song_url, song_name)
            mp3 = AudioSegment.from_mp3(song_name)
            mp3[:60 * 1000].export(song_name, format="mp3")  # 切割前60秒并覆盖保存
            print('%s.mp3' % song_id, " Save and cut song successfully!")
            return 1
        except:
            print("[error] Please confirm whether the song id is correct or whether the song is charged.")
            return 0

    def save_json(self, a):
        file_name=   a.SongID+".json"
        temp_dict={}
        temp_dict['SongID'] =a.SongID
        temp_dict['Domain'] = a.Domain
        temp_dict['AlbumName'] = a.AlbumName
        temp_dict['SingerName'] = a.SingerName
        temp_dict['SongName'] = a.SongName
        temp_dict['AlbumImgPath'] = a.AlbumImgPath
        temp_dict[' AlbumImgOnlinePath'] = a. AlbumImgOnlinePath
        temp_dict['SongPath'] = a.SongPath
        temp_dict['Lyrics'] = a.Lyrics
        print("Song: "+ a.SongName,"Singer: "+  a.SingerName, "Album: "+  a.AlbumName)

        with open(file_name, 'w') as f:
            json.dump(temp_dict,f)


    def get_songinfos(self,mysongs,domain):
        '''根据songid进入每首歌对应的url，拿到歌手名字，url就是:"http://music.163.com/song?id=64006"'''
        count= 1
        for myid in mysongs:

            print (count)
            if count > 25:
                break

            a= song()
            a.SongID  = myid

            a.SongPath = a.SongID + '.mp3'
            if self.sava_song(a.SongID) == 0:  #保存到本地音乐失败
                continue

            url=self.main_url+"song?id="+ a.SongID
            r = self.session
            r = BeautifulSoup(r.get(url, headers=self.headers).content, "html.parser")
            a.SongName = r.find('em', {'class': 'f-ff2'}).text

            result= r.find_all('p', {'class': 'des s-fc4'}) #有两个class一样的，第一个是歌手名字，第二个是专辑名字
            a.SingerName=result[0].find('a',{'class': 's-fc7'}).text
            a.AlbumName= result[1].find('a',{'class': 's-fc7'}).text

            a.AlbumImgOnlinePath= r.find('div',{'class': 'u-cover u-cover-6 f-fl'}).find('img')['data-src']
            a.AlbumImgPath= a.SongID +'.png'     # 格式转化成png
            self.save_img(a.AlbumImgOnlinePath, a.AlbumImgPath)  #保存到本地

            a.Lyrics=  self.get_music_lyric(a.SongID)
            a.Domain= domain
            self.save_json(a)
            count += 1




    def get_music_lyric(self,song_id):
        url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(song_id)
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        }

        cookies = {'appver': '1.5.2'}

        try:
            r = requests.get(url, headers=headers, cookies=cookies)
            if 'lrc' in r.json() and 'lyric' in r.json()['lrc'] and r.json()['lrc']['lyric'] is not None:
                lrc = r.json()['lrc']['lyric']
                pat = re.compile(r'\[.*\]')  # 把每行歌词前面的时间点去掉
                lrc = re.sub(pat, "", lrc)
                return lrc
            else:
                return []
        except requests.exceptions.RequestException as e:
            print(e)
            return []

    def work(self,playlist,domain):
        mysongs=self.get_songids(playlist)
        self.get_songinfos(mysongs,domain)

d=NetEaseMusic()
#d.work(167900089,"Classical")
#d.work(517575568,"Electronic")
#d.work(498708023,"Folk")
#d.work(102656381,"Blues")
#d.work(715331683,"Game")
#d.work(710865932,"Japanese")
#d.work(432705321,"Pop")
d.work(467058152,"Urban")