import sys,requests,os,re
from bs4 import BeautifulSoup as bs

n = input("Enter the number of comics you want to download.\n")
foldername = raw_input("Enter the folder name to store in.\n")

if(os.path.exists(foldername)):
	print "Folder already exists.\nSystem exiting.\n"
	sys.exit()

else:
	print "Creating folder..."
	os.mkdir(foldername)
	os.chdir(foldername)
	print "Folder created. Downloading files..."
	#initial request
	data = requests.get("http://explosm.net")
	htmldata = bs(data.text,"lxml")

	comicImageLink = "http:" + htmldata.select('#featured-comic')[0].get('src')
	imageFileRegex = re.compile(r"comics/\w+/(.+)")

	imageData = requests.get(comicImageLink)
	imageFileName = imageFileRegex.search(comicImageLink).group(1) 
	imageFile = open(imageFileName,"w")

	for chunk in imageData.iter_content(100000):
		imageFile.write(chunk)
	imageFile.close()

	for i in range(n-1):
		prevLink = "http://explosm.net" + htmldata.select('.previous-comic')[0].get('href')
		data = requests.get(prevLink)
		htmldata = bs(data.text,"lxml")

		if(htmldata.select('body')[0].getText() == "Could not find comic"):
			print "No comics found. System exiting.\n"
			sys.exit()
		else:
			comicImageLink = "http:" + htmldata.select('#main-comic')[0].get('src')
			imageData = requests.get(comicImageLink)
			imageFileName = imageFileRegex.search(comicImageLink).group(1)
			imageFile = open(imageFileName,"w")

			for chunk in imageData.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
	print "Your files have been downloaded. Enjoy! \n"