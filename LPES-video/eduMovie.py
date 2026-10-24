#!/usr/bin/env python3

# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sys, os, re, json, hashlib, subprocess, traceback
import pygments, pygments.lexers, pygments.formatters
import moviepy.editor as mpy
import pyte
import asciicast2movie
import text2audioFile, webRender


#
# module level variable for paths (must end with /)
#

mainDir  = os.path.dirname(os.path.realpath(__file__)) + "/"
cacheDir           = "cache/"
globalCacheBaseDir = mainDir + "../"
buildDir           = mainDir + "../tmp-build/"


#
# terminal colors, etc.
#

default = "\u001b[0m"
cyan    = "\u001b[96m"
yellow  = "\u001b[93m"
red     = "\u001b[91m"
clear   = default + "\u001b[H\u001b[J"

def logInfo(text, color=None):
	if color:
		print(color + text + default)
	else:
		print(text)
	sys.stdout.flush()


#
# audio, video and images cache support
#

def getCachedFilename(data, idStr=None, idStrAlt=None, ext="", cacheDir=cacheDir):
	if isinstance(data, str):
		data = data.encode()
	elif not isinstance(data, bytes):
		data = data.__repr__().encode()
	
	if idStr:
		return cacheDir + idStr + "_" + hashlib.md5(data).hexdigest() + ext, idStr
	else:
		return cacheDir + hashlib.md5(data).hexdigest() + ext, idStrAlt

def checkCachedFile(fileName, info=""):
	if not os.path.isfile(fileName):
		# create local cache dir
		try:
			os.mkdir(fileName.rsplit("/", 1)[0])
		except FileExistsError:
			pass
		# try move cached file from global cache dir to local cache dir
		try:
			if os.path.getsize(globalCacheBaseDir + fileName) > 0:
				os.rename(globalCacheBaseDir + fileName, fileName)
			else:
				return False
		except FileNotFoundError:
			return False
	
	if info:
		logInfo("use cached file \"" + fileName.rsplit("/", 1)[-1] + "\" for: " + info, cyan)
	
	return True


#
# images generations and converts
#

def addMargins(filePath, size = 8, negate = False, opts = {}):
	if "margins" in opts:
		size = opts["margins"]
	if "negate" in opts:
		negate = bool(opts["negate"])
	
	if size:
		size = str(size * 2)
		os.system("convert '" + filePath + "' -background white -gravity center -extent $(identify -format '%[fx:W+" +size+ "]x%[fx:H+" +size+ "]' '" + filePath + "') " + '-negate' * negate + " -define png:color-type=6 '" + filePath + "'")
	elif negate:
		os.system("convert '" + filePath + "' -negate -define png:color-type=6 '" + filePath + "'")

def LaTex2Image(inFilePath, convertTeX = None, convertTeXAgs = None, dpi = 170, margins = 0, viaCairo=False, negate=False):
	if convertTeXAgs:
		idStr = convertTeXAgs.__repr__() + "–" + os.path.basename(inFilePath)
	else:
		idStr = os.path.basename(inFilePath)
	
	fileName, _ = getCachedFilename( idStr + "\n\r" + inFilePath + "\n\r" + open(inFilePath).read(), cacheDir="" )
	outFilePath = cacheDir + fileName + ".tex.png"
	
	if not checkCachedFile(outFilePath, idStr):
		# convert source
		if convertTeX:
			convertTeX(inFilePath, buildDir + fileName + ".tex", convertTeXAgs)
		else:
			os.system("ln -sf \"$(realpath '" + inFilePath + "')\" '" + buildDir + fileName + ".tex" + "'")
		
		# build image
		os.system("cd '" + buildDir + "' && tex2pdf.sh '" + fileName + ".tex' -shell-escape")
		if viaCairo:
			os.system("pdftocairo -svg '" + buildDir + fileName + ".pdf' '" + buildDir + fileName + ".svg'")
			os.system("inkscape --without-gui --file='" + buildDir + fileName + ".svg' --export-area-drawing --export-dpi=" + str(dpi) + " --export-background=white --export-png='" + outFilePath + "'")
		else:
			os.system("inkscape --without-gui --file='" + buildDir + fileName + ".pdf' --export-area-drawing --export-dpi=" + str(dpi) + " --export-background=white --export-png='" + outFilePath + "'")
		addMargins(outFilePath, margins, negate)
	
	return outFilePath

def convertFile(inFilePath, convertSource = None, convertSourceAgs = None, outFilePath = None, **opts):
	ext = inFilePath.rsplit(".", 1)[-1]
	
	if ext == 'tex':
		return LaTex2Image(inFilePath, **opts)
	
	if convertSourceAgs:
		idStr = convertSourceAgs.__repr__() + "–" + os.path.basename(inFilePath)
	else:
		idStr = os.path.basename(inFilePath)
	
	if not outFilePath:
		outFilePath, _ = getCachedFilename( (idStr + "\n\r" + inFilePath + "\n\r").encode() + open(inFilePath, "rb").read() )
	
	if ext == 'svg':
		outFilePath += ".svg.png"
		if not checkCachedFile(outFilePath, idStr):
			logInfo("convert \"" + inFilePath + "\" into \"" + outFilePath + "\"", yellow)
			
			if convertSourceAgs:
				inFilePath = convertSource(inFilePath, buildDir + os.path.basename(outFilePath) + ".svg", convertSourceAgs)
			
			dpi, area = "", "--export-area-drawing"
			if "dpi" in opts:
				dpi = "--export-dpi=" + str(opts["dpi"])
			if "area" in opts:
				area = "--export-area-" + opts["area"]
			
			os.system("inkscape --without-gui --file='" + inFilePath + "' " + area + " " + dpi + " --export-background=white --export-png='" + outFilePath + "'")
			addMargins(outFilePath, opts=opts)
	elif ext == 'sch':
		outFilePath += ".sch.png"
		if not checkCachedFile(outFilePath, idStr):
			logInfo("convert \"" + inFilePath + "\" into \"" + outFilePath + "\"", yellow)
			
			if convertSourceAgs:
				inFilePath = convertSource(inFilePath, buildDir + os.path.basename(outFilePath) + ".sch", convertSourceAgs)
			
			dpi = "--dpi=250"
			if "dpi" in opts:
				dpi = "--dpi=" + str(opts["dpi"])
			
			os.system("sch2img.sh --output='" + outFilePath + "' " + dpi + " '" + inFilePath + "'")
			addMargins(outFilePath, opts=opts)
	else:
		raise BaseException("Unsupported input file extension: " + ext)
	
	return outFilePath


#
# text to audio and subtitles functions
#

def getAudioFiles(txt, idStr=None):
	fileName, idStr = getCachedFilename(txt, idStr, txt[:30])
	fileName += ".text"
	
	if not checkCachedFile(fileName + ".audio", idStr) or not checkCachedFile(fileName + ".info"):
		logInfo("generate new audio files for \"" + idStr + "\": " + fileName, yellow)
		txt = re.sub(r"<[^<>]*?>\[(.*?)\]", "\\1", txt)
		i = 1
		while '<m>' in txt:
			txt = txt.replace('<m>', '<mark name="m_' + str(i) + '"/>', 1)
			i += 1
		text2audioFile.text2audioFile(txt, fileName)
	
	return fileName

def getAudioClipAndSubtitles(txt, startOffset, localStartOffset, speed=1.0):
	# don't add marks at begin and end of text
	txt = re.sub("^ *<m>", "", txt)
	txt = re.sub("<m> *$", "", txt)
	
	# create audio sub clip
	audioFile = getAudioFiles(txt)
	audioClip = mpy.AudioFileClip(audioFile + ".audio").fx( mpy.vfx.speedx, speed )
	
	# load time points info from json
	times = json.load( open(audioFile + ".info") )
	if not "m_0" in times:
		times["m_0"] = 0.0
	
	# create subtitles
	subtitles = []
	txt = re.sub(r"<([^<>]*?)>\[.*?\]", "\\1", txt) # pronunciation tips <world>[pronunciation] -> world
	txt = re.sub(r"<break[^<>]*?>", "", txt)
	txt = re.sub(r"<mark [^<>]*?>", "<m>", txt)
	txt = txt.split("<m>")
	timepoints = sorted(times.values())
	for t, s in zip( timepoints, txt ):
		subtitles.append( (startOffset + localStartOffset + t, s.strip()) )
	
	# create timepoints dict for named marks
	timepoints = {}
	for t in times:
		if not re.fullmatch("m_[0-9]*", t):
			timepoints[t] = localStartOffset + times[t]
	return audioClip, subtitles, timepoints


#
# circuitjs simulation to video
#

circuitjsBaseURL = "http://cs.opcode.eu.org/circuitjs.html?hideMenu=true&"
circuitjsSimulationList = mainDir + "simulations.txt"

def runActionOnCircuitjs(browser, action, test=None):
	if (action[0] == "switch"):
		webRender.clickElement(browser, action[1], action[2] + 60, "/html/body/div[2]/div[2]/div/div[4]/canvas", test)
	elif (action[0] == "setSlider"):
		num   = action[1]
		val   = action[2]
		xpath = "/html/body/div[2]/div[2]/div/div[2]/table/tbody/tr[" + str (10+num*2) + "]/td/table/tbody/tr/td/canvas"
		webRender.clickElement(browser, int(127 * val - 64), 0, xpath, test, originAtCenter=True)
	else:
		webRender.runAction(browser, action, test)

def getCircuitjsURL(simID):
	for x in open(circuitjsSimulationList):
		x = x.replace("\n", "")
		if x == "" or x[0] == "#":
			continue
		
		x = x.split(maxsplit=1)
		if x[0] == simID:
			return x[1]

def circuitjs(simID, preTime, postTime, actions=[], preActions=[], idStr=None, test=False, baseURL=circuitjsBaseURL):
	url = getCircuitjsURL(simID)
	
	if test:
		browser, winfo = webRender.createBrowser(1260, 700)
		browser.get( baseURL + url )
		return browser
	
	fileName = simID + url + preTime.__repr__() + actions.__repr__() + postTime.__repr__() + preActions.__repr__()
	fileName, idStr = getCachedFilename(fileName, idStr, simID, ".circuitjs.mp4")
	
	if not checkCachedFile(fileName, idStr):
		logInfo("generate new simulation video for \"" + idStr + "\": " + fileName, yellow)
		webRender.render( baseURL + url, preTime, postTime, actions, preActions, fileName, 1260, 700, 25, runAction = runActionOnCircuitjs )
	
	return fileName


#
# asciicast code manual manipulation
#

defaultHost="dragon"
defaultUser="rrp"

def prompt(cwd="/tmp", host=defaultHost, user=defaultUser, prompt="$ ", color=True, clear=True):
	if clear:
		clear = "\r"
	else:
		clear = ""
	if color:
		return clear + "\u001b[01;31m" + user + "@" + host + "\u001b[0m:\u001b[01;36m" + cwd + "\u001b[0m" + prompt
	else:
		return user + "@" + host + ":" + cwd + prompt

def editBegin(up):
	return "\u001b[" + str(up) + "A\u001b[1G\u001b[0K"

def editEnd(down, right=None):
	if right==None:
		right = len(prompt(color=False))+1
	return "\u001b[" + str(down) + "B\u001b[" + str(right) + "G"

markBegin="\u001b[01;7m"

markEnd="\u001b[01;0m"

def markLines(txt, lines = [], edit = True, end = "\r\n", extraOffset = 0):
	txt = txt.split('\n')
	
	if txt[-1] == "":
		del txt[-1]
	
	if edit:
		out = editBegin(len(txt) + extraOffset)
	else:
		out = ""
	
	for i in range(len(txt)):
		if i in lines:
			out += markBegin + txt[i].replace('\x1b[39;00m', '\x1b[39;00m' + markBegin).replace('\x1b[39;49;00m', '\x1b[39;49;00m' + markBegin) + markEnd + "\r\n"
		else:
			out += txt[i] + "\r\n"
	
	if end == "\r\n":
		return out
	else:
		return out[:-2] + end


#
# code and code output to console string
#

def code2console(code, lang, first=1, last=-1, limit=16):
	code = code.strip()
	formatted = pygments.highlight(
		code,
		pygments.lexers.get_lexer_by_name(lang),
		pygments.formatters.Terminal256Formatter(style='native')
	)
	lines = formatted.split('\n')
	
	if lines[-1] == "":
		del lines[-1]
	
	if last == -1:
		last = len(lines) + (last+1)
	
	if limit and (last-first)+1 > limit:
		logInfo("  Warning: too much lines (" + str((last-first)+1) + ") in code2console output", red)
		logInfo("    " + code.__repr__()[:74])
		logInfo("    " + traceback.format_stack()[-2] )
		last = first+limit+1
	
	return str.join("\n\r", lines[first-1:last])


def runCode(code, args=[], cmd="python3", filename=None, stdin=None, run=True):
	if not filename:
		if cmd == "python3":
			filename = "przykład.py"
		elif cmd == "bash":
			filename = "przykład.sh"
		elif cmd == "gcc":
			filename = "przykład.c"
		elif cmd == "g++":
			filename = "przykład.cpp"
		else:
			logInfo("  Warning: unknown command and no filename in runCode", red)
			filename = "przykład"
	
	f = open("/tmp/" + filename, "w")
	f.write(code)
	f.close()
	
	if run:
		return runCommandString(cmd + " " + filename + " " + str.join(" ", [str(a) for a in args]), cwd="/tmp", stdin=stdin)
	else:
		return ""

def runCommandString(command, hiddenargs="", prompt=prompt(), cwd=None, env=None, stdin=None):
	if hiddenargs:
		exec_command = command.split(" ", 1)
		exec_command = exec_command[0] + " " + hiddenargs + " " + exec_command[1]
	else:
		exec_command = command
	if isinstance(stdin, str):
		stdin = stdin.encode()
	
	res = subprocess.run(exec_command, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd, env=env, input=stdin)
	return prompt + command + "\n\r" + res.stdout.decode(errors='ignore').replace("\n", "\n\r") + prompt


#
# console string to videoclip
#

def sequenceToClip(cdata, timepoints, length, mode, screen = None, overlay=False):
	# process string (like "mark_name + 13") values as time
	lasttime = 0
	for i in range(len(cdata)):
		if isinstance(cdata[i][0], str):
			logInfo("  Processing timepoints named tag: " + cdata[i][0])
			cdata[i][0] = eval(cdata[i][0], {'__builtins__': None}, timepoints) # if "TypeError: 'NoneType' object is not subscriptable" here, probably cdata[i][0] marker is missing in timepoints
		if lasttime > cdata[i][0]:
			logInfo("  Warning: not monotonic time values in clip data (" + str(lasttime) + " " + str(cdata[i][0]) + ")", red)
		lasttime = cdata[i][0]
	#print(cdata)
	
	# check showing time for last clip frame
	lastFrameDuration = length - (cdata[-1][0] - cdata[0][0])
	#print("   → ", lastFrameDuration, length, cdata[-1][0], cdata[0][0])
	if lastFrameDuration < 0.5:
		logInfo("  Warning: last frame duration in clip too short (" + str(lastFrameDuration) + ")", red)
		lastFrameDuration = 0.5
	
	# render console clip
	if mode == 'console':
		return asciicast2movie.render_asciicast_frames(
			cdata, screen[0], screen[1], blinkingCursor=screen[2], lastFrameDuration=lastFrameDuration, renderOptions={'fontSize':24}
		)
	
	# compose image / video clips
	clips = []
	
	for i in range(len(cdata)-1):
		cdata[i].append( cdata[i+1][0]-cdata[i][0] )
	cdata[-1].append( lastFrameDuration )
	
	overLength = 0
	for x in cdata:
		if x[1]:
			ext = x[1].rsplit(".",1)[-1].lower()
			if ext in ["png", "jpg", "jpeg"]:
				clips.append( mpy.ImageClip(x[1]).set_duration(x[-1]) )
			elif ext in ["mp4"]:
				video = mpy.VideoFileClip(x[1])
				videoLen   = x[-1] - overLength
				overLength = 0
				if video.duration > videoLen:
					logInfo("  Warning: video duration (" + str(video.duration) + ") greater than clip length (" + str(videoLen) + ") for " + x[1], red)
					overLength = video.duration - videoLen
				clips.append( video.set_duration(videoLen) )
			else:
				raise BaseException("Unknown image / video format for file " + x[1])
		else:
			clips.append( mpy.ImageClip(mainDir + "blank.png").set_duration(x[-1]) )
	
	return mpy.concatenate_videoclips(clips, method="compose")


#
# titles
#

titleBoardSVGPath = mainDir + "TitleBoard.svg"

def createTitleClip(data, length = None):
	if length == None:
		length = 3.5
	
	idStr = str.join("\\n", data)
	fileName, _ = getCachedFilename(idStr, ext=".title.png")
	
	if not checkCachedFile(fileName, idStr[:30]) or os.path.getmtime(titleBoardSVGPath) > os.path.getmtime(fileName):
		titleBoard = open(titleBoardSVGPath).read()
		titleBoard = titleBoard.replace('#XX.XX', data[0]).replace('TITLE LINE1 XXX', data[1]).replace('TITLE LINE2 XXX', data[2]).replace('TITLE LINE3 XXX', data[3])
		subprocess.run("inkscape --without-gui --export-png='" + fileName + "' /dev/stdin", shell=True, input=titleBoard.encode())
	
	return mpy.ImageClip(fileName).set_duration(length)

def createSectionTitle(data, length = None):
	if length == None:
		length = 2.15
	try:
		return mpy.TextClip(data, fontsize = 64, font = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", color = "cyan").set_duration(length).fx(mpy.vfx.fadein,0.75,(30,30,30)).fx(mpy.vfx.fadeout,0.75,(30,30,30))
	except:
		err = "\n\nIf you get 'operation not allowed by the security policy' error above, try remove '/etc/ImageMagick-6/policy.xml' file.\n"
		raise IOError(err)


#
# screenplay proccessing
#

def parseSubClipData(data, screens, startOffset, onlyAudio = False, outputSize = (1280, 720)):
	TopDownOffset,TopDownBgColor = 8, (150,150,150)
	length, audio, video, subtitles, timepoints = None, None, None, [], {}
	if 'text' in data:
		clips = []
		localStartOffset = 0
		for txt in data['text']:
			audioClip, sub, times = getAudioClipAndSubtitles(txt, startOffset, localStartOffset)
			clips.append( audioClip )
			subtitles += sub
			timepoints.update(times)
			localStartOffset += audioClip.duration
		audio = mpy.concatenate_audioclips(clips)
		length = audio.duration
	elif 'length' in data:
		length = data['length']
	
	#print(" → ", startOffset, length, timepoints)
	
	if 'title' in data:
		video = createTitleClip(data['title'], length)
		length = video.duration
	elif 'section' in data:
		logInfo("processing: " + data['section'].__repr__())
		video = createSectionTitle(data['section'], length)
		length = video.duration
	
	if not length:
		raise BaseException("No text nor length in sub-clip data")
	if onlyAudio:
		return audio, subtitles
	
	if 'image' in data:
		video = sequenceToClip(data['image'], timepoints, length, 'image')
	elif 'console' in data:
		video = sequenceToClip(data['console'], timepoints, length, 'console', screens[0])
	elif 'consoleTop' in data and 'consoleDown' in data:
		videoTop = sequenceToClip(data['consoleTop'], timepoints, length, 'console', screens[1])
		videoDown = sequenceToClip(data['consoleDown'], timepoints, length, 'console', screens[2])
		size = (
			max(videoTop.size[0], videoDown.size[0]),
			videoTop.size[1] + TopDownOffset + videoDown.size[1]
		)
		videoDown = videoDown.set_position( (0, videoTop.size[1] + TopDownOffset) )
		video = mpy.CompositeVideoClip([videoTop, videoDown], size=size, bg_color=TopDownBgColor)
	
	if not video:
		raise BaseException("No image, video nor console in sub-clip data")
	if video.size[0] > outputSize[0] or video.size[1] > outputSize[1]:
		logInfo("  Warning: sub-clip resolution too big: " + str(video.size), red)
	
	# TODO: overlay image ... to musi być tutaj aby dostosować rozmiar obrazka do rozmiaru video ...   jako lista list (czas początku, obrazek, polozenie, autoscale=True/False) ... też z użyciem sequenceToClip
	
	lengthDiff = video.duration - length
	if lengthDiff > 0.001 or lengthDiff < -0.001:
		raise BaseException("Video length error: length=" + str(length) + ", video=" + str(video.duration))
	
	video.audio = audio
	
	return video, subtitles


def parseClipData(data, outDir = None, filename = None, endTitle = None, endTitleTime = 5, writeInBackground = False, overlayImg = None, onlyAudio = False, outputSize = (1280, 720)):
	def consoleReset(width = 80, height = 24, blinkingCursor=0.5):
		screen = pyte.Screen(width, height)
		stream = pyte.Stream(screen)
		return (screen, stream, blinkingCursor)
	
	currentLength = 0
	videos, subtitles = [], []
	screens = [consoleReset(), consoleReset(height=16, blinkingCursor=None), consoleReset(height=7)]
	for subClipData in data:
		if 'comment' in subClipData:
			logInfo("processing: " + subClipData['comment'])
		# TODO wpis ustawiający parametry wybranych elementów screens
		else:
			video, sub = parseSubClipData(subClipData, screens, currentLength, onlyAudio=onlyAudio, outputSize=outputSize)
			if video:
				videos.append(video)
				subtitles += sub
				currentLength += video.duration
	subtitles.append( (currentLength, "") )
	
	if onlyAudio:
		video = mpy.concatenate_audioclips(videos)
	else:
		if endTitle and endTitleTime:
			videos.append( mpy.ImageClip(endTitle).set_duration(endTitleTime) )
		
		video = mpy.concatenate_videoclips(videos, method="compose")
		
		if overlayImg:
			overlayImg = mpy.ImageClip(overlayImg).set_duration(video.duration)
			video = mpy.CompositeVideoClip([video, overlayImg])
	
	logInfo("Clip length (mm:ss) is {:02d}:{:02d}".format(int(video.duration // 60), int(video.duration % 60)))
	
	try:
		os.remove(buildDir + "prepareRender.lock")
	except:
		pass
	
	if filename:
		writeVTT(subtitles, buildDir + filename)
		
		audio = video if onlyAudio else video.audio
		audio.write_audiofile(buildDir + filename + ".mka", 44100, codec="libvorbis", ffmpeg_params=["-ac", "1"])
		
		if not onlyAudio:
			video.write_videofile(buildDir + filename + ".mkv", fps=24, codec="libx265", audio=False, ffmpeg_params=["-crf", "32"])
			if 'title' in data[0]:
				title = "LPES " + data[0]['title'][0] + ": " + " ".join(data[0]['title'][1:]).strip()
				title_cmd = '-metadata title="' + title + '"'
			else:
				title_cmd = ''
			os.system("ffmpeg -i " + buildDir + filename + ".mkv -i " + buildDir + filename + ".mka -i " + buildDir + filename + ".vtt -c copy " + title_cmd + " " + outDir + filename + ".mkv")
	
	return video, subtitles


#
# writing subtitles to file
#

def writeVTT(subtitles, filename):
	def formatTime(time):
		ms   = int(time%1 * 1000)
		time = int(time)
		s    = time % 60
		time = time // 60
		m    = time % 60
		h    = time // 60
		return '{:02d}:{:02d}:{:02d}.{:03d}'.format(h, m, s, ms)
	
	o = open(filename + ".vtt", 'wt')
	o.write("WEBVTT Kind: captions; Language: en\n\n")
	for i in range( len(subtitles) - 1 ):
		o.write(formatTime(subtitles[i][0]) + ' --> ' + formatTime(subtitles[i+1][0] - 0.1) + '\n')
		o.write(subtitles[i][1] + '\n\n')


def mkdir(path):
	try:
		os.mkdir(path)
	except FileExistsError:
		pass
	return path

if __name__ == "__main__":
	import sys, os, traceback, pprint
	import eduMovie
	
	if len(sys.argv) < 2:
		print("USAGE: " + sys.argv[0] + " path_to/screenplay_file.py [...]", file=sys.stderr)
		exit(2)
	
	# printing exception on red
	def myexcepthook(type, value, tb):
		sys.stderr.write(eduMovie.red + ''.join(traceback.format_exception(type, value, tb)) + eduMovie.default)
	sys.excepthook = myexcepthook
	
	workdir = None
	
	# create output dir (must end with /)
	outDir = mkdir(eduMovie.mainDir + "/../output/")
	
	# init endTitleSVG variable, can be override in included files
	endTitleSVG = "default.svg"
	
	# proces all command line args as screenplay files
	for i in range (1, len(sys.argv)):
		# split arg into screenplay dir path and filename
		screenplay = sys.argv[i].rsplit("/", maxsplit=1)
		
		logInfo("\u001b[01;7mUse " + screenplay[1] + " screenplay file from " + screenplay[0] + "\u001b[01;0m")
		
		# go to screenplay dir
		if not workdir:
			os.chdir(screenplay[0])
			workdir = screenplay[0]
			movieid = screenplay[0].split("/")[-1]
		elif workdir != screenplay[0]:
			raise BaseException("different workdir extracted from cmdline args:\n   " + workdir + " vs " + screenplay[0])
		
		# include screenplay file
		exec( open(screenplay[1]).read() )
	
	# create end title
	if endTitleSVG:
		endTitleSVG = eduMovie.mainDir + "EndTitles/" + endTitleSVG
		endTitlePNG, _ = eduMovie.getCachedFilename(open(endTitleSVG).read(), ext=".svg.png")
		endTitlePNG = eduMovie.globalCacheBaseDir + endTitlePNG
		if not os.path.isfile(endTitlePNG) or os.path.getmtime(endTitleSVG) > os.path.getmtime(endTitlePNG):
			eduMovie.convertFile(endTitleSVG, outFilePath=endTitlePNG.rsplit(".", 2)[0], margins=0)
	
	#print("clipData =", pprint.pformat(clipData, width=1024))
	#eduMovie.parseClipData(clipData, onlyAudio=True)
	#eduMovie.parseClipData(clipData)
	#eduMovie.parseClipData(clipData, outDir, movieid + "_beta", endTitle=endTitlePNG, overlayImg=eduMovie.globalCacheBaseDir + eduMovie.cacheDir + 'draft.png')
	eduMovie.parseClipData(clipData, outDir, movieid, endTitle=endTitlePNG)
