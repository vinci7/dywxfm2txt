import os

# ffmpeg -i 0-16k.wav -acodec pcm_s16le -ar 16000  \\ 
# -ac 1 -f segment -segment_time 55 out/0-out%03d.wav

dirName = "dywx-audio"
project = "dywx"
fileType = "mp3"


path = "{}/{}".format(os.getcwd(), dirName)
files = os.listdir(path)

def getFileType(path):
    return path.split('.')[-1]

def checkDir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

for file in files:
	if getFileType(file) != fileType:
		continue 

	cutDirName = file.split('.')[0]
	index = cutDirName.replace(project, "")

	checkDir("{}-cut".format(dirName))
	checkDir("{}-cut/{}".format(dirName, cutDirName))

	cmd = "ffmpeg -i {}/{} -acodec pcm_s16le -ar 16000 -ac 1 -f segment -segment_time 40 {}-cut/{}/out{}.wav".format(dirName, file, dirName, cutDirName, "%03d")
	print(cmd)

	os.system(cmd)