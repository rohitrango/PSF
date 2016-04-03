import pyperclip,requests,sys

link = ""
if len(sys.argv) == 1:
	link = pyperclip.paste()
	print "Link has been extracted from clipboard."
else:
	link = sys.argv[1]
	print "Link has been extracted from terminal/command line.\n"

download = requests.get(link)

if(download.status_code != 200):
	print "Some error occured! Check the link !\n"
	exit()
else:
	fileName = raw_input("Enter the name of the file. (With proper format)\n")
	myFile = open(fileName,"wb")
	for i in download.iter_content():
		myFile.write(i)
	print "Download success!\n"
	myFile.close()



