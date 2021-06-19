from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import time

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

time.sleep(5)
playlistURL = input('\n\n\nEnter Youtube playlist URL: ')

# Open playlist
driver.get(playlistURL)
time.sleep(5)

# Get total no of videos
try:
	videoNum = (driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-playlist-sidebar-renderer/div/ytd-playlist-sidebar-primary-info-renderer/div[1]/yt-formatted-string[1]/span[1]')).get_attribute('innerHTML')
except NoSuchElementException:
	print('    Element not found')

#calculate total Time
totalTime = 0
try:
	for i in range(1, int(videoNum)+1):
		timePath = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[' + str(i) + ']/div[2]/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span')
		videoTime = timePath.get_attribute('innerHTML').split(':')
		if len(videoTime) == 1:
			totalTime += int(videoTime[0])
		elif len(videoTime) == 2:
			totalTime += int(videoTime[0])*60 + int(videoTime[1])
		else:
			totalTime += int(videoTime[0]) * 3600 + int(videoTime[1]) * 60 + int(videoTime[2])
except NoSuchElementException:
	print('    Video number ' + str(i) + ' not found')

# Print playlist Name
try:
	playlistName = driver.find_element_by_css_selector('a.yt-simple-endpoint.style-scope.yt-formatted-string').get_attribute('innerHTML')
	print('\n\n    ' + playlistName)
except NoSuchElementException:
	print('    Playlist Name not found')

# Print total time
hours = 0
minutes = 0
seconds = 0

print('\n\n    ' + str(totalTime) + ' Seconds')

if totalTime >= 3600:
	hours = int(totalTime / 3600)

seconds = totalTime % 3600
if seconds >= 60:
	minutes = int(seconds / 60)

seconds = seconds % 60
print('\n\n    ' + str(hours) + ' Hours ' + str(minutes) + ' Minutes ' + str(seconds) + ' Seconds')

time.sleep(2)
driver.close()