# Music-Website
- It's a personal music website. Songs are crawled from Netease Cloud Music.
- Language & framework: Python3.6 + Django + SQLite + HTML+ CSS + Javascript
- IDE: Pycharm Professional 2018.2.4
- **Video**: https://youtu.be/UZnU3j95uH0

## Usage ##
### Crawl Music ###
- In pycharm: click `run`
- Or in console: under the path `/Code/CrawlMusic`, in `venv` mode, use `python crawlmusic.py`

The program will be terminared by error if you are trying to download paid songs or VIP-only songs. If it is successfully finished, you will get a `png` image, a `mp3` song and a `json` file about needed infomation for each song. The files are all crawled from Netease Cloud Music and named by the song's ID in Netease Cloud Music.

<img src="/ScreenShots/pic1.jpg" width="300"/>

### Music Website ###

- In pycharm: click `run`
- Or in console: under the path `/Code/MusicWeb`, in `venv` mode, use `python manage.py runserver 127.0.0.1:8001`
- Then open `http://127.0.0.1:8001/` in chrome.


<img src="/ScreenShots/1.png" width="1000"/>
	
<img src="/ScreenShots/2.png" width="1000"/>
	
<img src="/ScreenShots/3.png" width="1000"/>
	
<img src="/ScreenShots/4.png" width="1000"/>
	
<img src="/ScreenShots/5.png" width="1000"/>
	
<img src="/ScreenShots/7.png" width="1000"/>