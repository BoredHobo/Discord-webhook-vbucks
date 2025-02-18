from selenium import webdriver
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
import undetected_chromedriver as uc

#Opens the website (in this case, FortniteDB to get V-Buck missions) using undetected_chromedriver to bypass the robot detector
driver = uc.Chrome()
driver.get("https://fortnitedb.com")

#Clicks the pre-defined xxMistaBeastxx filter
filter = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div/div/span").click()

# Finds table that displays the missions
vbucks = driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/div[2]/div/div[3]/table/tbody")

# Scrolls about half-way down, may need to be tweaked based on your monitor
driver.execute_script("window.scrollTo(0, 700)")
vbucks.screenshot("/vbucks.png")
driver.quit

#uses Discord MarkDown to make a link and @ a couple people
content = "[FortniteDB](<https://fortnitedb.com/>) <@> <@> <@> <@>"

# without this, it can't @ anyone, could also change it to a role
allowed_mentions = {
    "users": ["user-id"],
    "roles": ["role-id"]
}

#replace with your webhook url
webhook = DiscordWebhook(url='Place URL Here', username="V-Bucks", content=content)

#gives the webhook permission to read the vbucks.png file and attach it to the message
with open("/vbucks.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='vbucks.png')
response = webhook.execute()