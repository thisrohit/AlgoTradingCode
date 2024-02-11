import time
from selenium import webdriver

video_link = 'https://www.youtube.com/watch?v=uXRZXuRpoLQ'
views = 1000
video_duration = 5 * 60

driver = webdriver.Chrome()
driver.get(video_link)

for i in range(views):
    time.sleep(video_duration)
    driver.refresh()