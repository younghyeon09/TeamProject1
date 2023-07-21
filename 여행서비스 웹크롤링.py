from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

#셀레니움 버전이 업그레이드 되면서 기존 명령어가 적용되지 않을 때
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#웹페이지 해당 주소로 이동
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.agoda.com/ko-kr/")

#페이지 로딩 시간
time.sleep(5)

#팝업창을 없애는 코드
popup_box = driver.find_element(By.XPATH,"/html/body/div[12]/div[2]/button")
popup_box.click()
time.sleep(5)

#로스엔젤레스로 검색한다
search_box = driver.find_element(By.XPATH,'//*[@id="textInput"]')
search_box.send_keys("로스엔젤레스")
search_box.send_keys(Keys.RETURN)
time.sleep(1)

autocomplete_tab = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/ul/li[1]')
autocomplete_tab.click()
time.sleep(1)

#날짜 설정
next_month_button = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/div[1]/div/div[1]/span[2]')
next_month_button.click()
time.sleep(1)

start_date = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[5]')
start_date.click()
time.sleep(1)

end_date = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[1]/div/div[2]/div/div/div[6]/div/div/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[6]')
end_date.click()
time.sleep(1)

#이용 인원 수 설정
human_num = driver.find_element(By.XPATH,'//*[@id="occupancy-selector"]/div/div/div[2]/div[2]/div[1]')
human_num.click()
time.sleep(1)

#검색
search_button = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[2]/button/div')
search_button.click()
time.sleep(1)

search_button = driver.find_element(By.XPATH,'//*[@id="SearchBoxContainer"]/div[2]/button/div')
search_button.click()
time.sleep(3)

hotel_score = driver.find_element(By.XPATH,'//*[@id="SideBarLocationFilters"]/div[8]/div[2]/ul/li[1]/span/span[1]/span')
hotel_score.click()
time.sleep(1)

#상품정보 div
items = driver.find_elements_by_css_selector()
