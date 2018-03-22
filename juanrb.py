#encoding=utf-8
import urllib.request
import requests,os,time
from bs4 import BeautifulSoup
class downloader(object):
	def __init__(self):
		self.reba='http://www.jj20.com/plus/search.php?q=%B5%CF%C0%F6%C8%C8%B0%CD'
		self.headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
		self.nums=0
		self.urlHeader='http://www.jj20.com'
		self.picHeader='http://www.jj20.com/bz/nxxz/nxmt/'
		self.album=[]
		self.pic=[]
		self.bigpic=[]

	def albumUrl(self,target):
		try:
			html=requests.get(url=target,headers=self.headers)
		except:
			print("**sleep 5s")
			time.sleep(5)
			html=requests.get(url=target,headers=self.headers)
		html=BeautifulSoup(html.text)
		albumUrl=html.find_all('a',class_='pic')
		for each in albumUrl:
			each=BeautifulSoup(str(each))
			each=each.find('a')
			each=each.get('href')
			self.album.append(each)

	def picUrl(self,picHeader):
		for aUrl in self.album:
			aUrl=self.urlHeader+aUrl
			try:
				time.sleep(0.6)
				html=requests.get(url=aUrl,headers=self.headers)
			except:
				printf("**sleep 5s")
				time.sleep(5)
				html=requests.get(url=target,headers=self.headers)
			html=BeautifulSoup(html.text)
#			print(html)
			singlePic=html.find_all('ul',id='showImg')
			singlePic=BeautifulSoup(str(singlePic))
			singlePic=html.find_all('li')
#			print(singlePic)
#			print("\n\n")
			for each in singlePic:
				time.sleep(0.3)
				each=BeautifulSoup(str(each))
				each=each.find('a')
				if each==None:
					continue
#				print(each.get('href'))
				url=picHeader+each.get('href')
				self.pic.append(url)
			self.pic=self.pic[0:-6]
#		print(self.pic,"  ",len(self.pic))
		print("\n load over")
		for big in self.pic:
#			time.sleep(10)
			try:	
				html=requests.get(url=big,headers=self.headers)
			except:
				time.sleep(3)
				html=requests.get(url=big,headers=self.headers)
			html=BeautifulSoup(html.text)
			bigpic=html.find('img',id='bigImg')
			self.bigpic.append(bigpic.get('src'))
#		print(self.bigpic,"\n",len(self.bigpic))
		print("2)load over")
		for down in self.bigpic:
			self.nums+=1
			try:
				picture=requests.get(url=down,headers=self.headers)
			except:
				time.sleep(3)
				picture=requests.get(url=down,headers=self.headers)
			else:
				time.sleep(0.2)
			with open(str(self.nums)+'.jpg','wb') as f:
				f.write(picture.content)
			

if __name__=='__main__':
	dl=downloader()
	dl.albumUrl(dl.reba)
	dl.picUrl(dl.picHeader)
