# Copyright (c) 2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
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


from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from pyvirtualdisplay import Display
import os, time, subprocess

geckodriverPath = '/usr/local/bin/geckodriver'

def createBrowser(width, height, headless = False, fullScreen = False):
	if headless:
		options = Options()
		options.add_argument('-headless')
	elif fullScreen:
		options = Options()
		options.add_argument('--kiosk')
	else:
		options = None
	
	service = Service(executable_path=geckodriverPath)
	browser = Firefox(service=service, options=options)
	windowInfo = browser.execute_script(
		"return [window.outerWidth, window.innerWidth, window.outerHeight, window.innerHeight, window.mozInnerScreenX, window.mozInnerScreenY];"
	)
	windowInfo = [int(x) for x in windowInfo]
	
	browser.set_window_size( windowInfo[0] - windowInfo[1] + width, windowInfo[2] - windowInfo[3] + height )
	
	return browser, windowInfo

def clickElement(browser, x, y, xpath="/html/body", wait=None, originAtCenter=False):
	print(f" -> clickElement: {xpath} + offest({x}, {y})")
	canvas = browser.find_element("xpath", xpath)
	if not originAtCenter:
		x -= canvas.size['width']/2
		y -= canvas.size['height']/2
	print(f"   element center = {canvas.location}, offret from center = ({x}, {y})")
	
	if wait == None:
		ActionChains(browser).move_to_element_with_offset(canvas, x, y).click().perform()
	else:
		ActionChains(browser).move_to_element_with_offset(canvas, x, y).click_and_hold().perform()
		time.sleep(wait)
		ActionChains(browser).move_to_element_with_offset(canvas, x, y).release().perform()
	ActionChains(browser).move_to_element_with_offset(canvas, 0, 0).perform()

def runAction(browser, action, test=None):
	if (action[0] == "click"):
		clickElement(browser, *action[1::], wait=test)
	if (action[0] == "longClick"):
		clickElement(browser, *action[1:-1], wait=action[-1])
	elif (action[0] == "wait"):
		time.sleep(action[1])

def render(url, preTime, postTime, actions = [], preActions = [], outfile="/dev/shm/out.mp4", width = 1280, height = 720, fps = 25, runAction = runAction):
	display = Display(visible=False, size=(width, height), color_depth=24, extra_args=['-nocursor'])
	display.start()
	display_id = os.environ.get('DISPLAY', ':99')
	
	browser, winfo = createBrowser(width, height, fullScreen=True)
	browser.get(url)
	
	time.sleep(1)
	
	for action in preActions:
		print("make (pre) action:", action)
		runAction(browser, action)
	
	print("start recorder")
	
	recorder = subprocess.Popen(f'ffmpeg -f x11grab -framerate {fps} -video_size {width}x{height} -t {preTime+postTime} -i {display_id}+{winfo[4]},{winfo[5]} -y {outfile}', shell=True)
	# use ffmpeg, browser.save_screenshot is too slow for:
	#   for i in range(int(preTime * fps)):   browser.save_screenshot("/dev/shm/in/rend_A{:04d}.png".format(i))
	
	print("rendering preTime:", preTime)
	time.sleep( preTime )
	
	for action in actions:
		print("make action:", action)
		runAction(browser, action)
	
	print("rendering postTime:", postTime)
	time.sleep( postTime )
	
	print("wait for end recorder")
	recorder.wait()
	
	browser.quit()
	display.stop()
	
	return outfile
