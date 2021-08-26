from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time
import login_info
#You have to login in your account.


class Insta:
    follow_set = set()
    following_set = set()

    def __init__(self):
        self.read_files()

    def read_files(self):
        with open("followers.txt", "r+", encoding="UTF-8")as file0:
            file_data = file0.read()
            self.follow_set = set()
            follower1 = file_data.split("\n")
            for a in follower1:
                self.follow_set.add(a)

        with open("following.txt", "r+", encoding="UTF-8")as file1:
            file_data1 = file1.read()
            self.following_set = set()
            following = file_data1.split("\n")
            for k in following:
                self.following_set .add(k)

    def followers_crud(self):
        for c in self.follow_set:
            print("************")
            print(c)

    def following_crud(self):
        for d in self.following_set:
            print("************")
            print(d)

    def compare(self):
        for f in self.following_set .difference(self.follow_set):
            print("***********************")
            print(f)


username = input("Write the person you want to check:")
time.sleep(5)
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/")
time.sleep(5)


username_field = browser.find_element_by_name("username")
password_field = browser.find_element_by_name("password")
username_field.send_keys(login_info.username)
password_field.send_keys(login_info.password)
time.sleep(4)

login = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
login.click()
time.sleep(6)

browser.get("https://www.instagram.com/{}/".format(username))
time.sleep(6)

following_path = browser.find_elements_by_css_selector(".Y8-fY")
following_button = following_path[2]
following_button.click()
time.sleep(5)

jscommand = """
followers=document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage =followers.scrollHeight;
return lenOfPage;
"""

lenOfPage = browser.execute_script(jscommand)
match = False

while match == False:
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(2)

following_list = []
following_who = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
for follow in following_who:
    following_list.append(follow.text)

with open("following.txt", "w", encoding="UTF-8") as file:
    for follow in following_list:
        file.write(follow + "\n")

i = 0

while i < 20:
    try:
        exit = browser.find_elements_by_css_selector(".wpO6b  ")
        exit_button = exit[i]
        exit_button.click()
    except ElementClickInterceptedException:
        print("It's not clickable but it is still in progress.")
        print(".....")
    except IndexError:
        print(".....")

    i += 1

#############
followers = browser.find_elements_by_css_selector(".Y8-fY")
followers_button = followers[1]
followers_button.click()
time.sleep(2)

lenOfPage = browser.execute_script(jscommand)
match1 = False

while match1 == False:
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match1 = True
time.sleep(2)

followers_list = []
followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")
for follower in followers:
    followers_list.append(follower.text)

with open("followers.txt", "w", encoding="UTF-8") as file:
    for follower2 in followers_list:
        file.write(follower2 + "\n")

browser.close()
insta = Insta()
insta.compare()
