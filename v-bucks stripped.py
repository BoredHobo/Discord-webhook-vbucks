from selenium import webdriver
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook
import undetected_chromedriver as uc

#Opens the website (in this case, FortniteDB to get V-Buck missions) using undetected_chromedriver to bypass the robot detector
driver = uc.Chrome()
driver.get("https://fortnitedb.com")

#takes screenshot of the V-Bucks, and saves it as a png to wherever you decide, then closes Chrome
driver.implicitly_wait(5)
vbucks = driver.find_element(By.CLASS_NAME, "new_block_block.mt-0")
vbucks.screenshot("/vbucks.png")
driver.quit

#uses Discord MarkDown to make a link and @ a couple people
content = "[FortniteDB](<https://fortnitedb.com/>) <@> <@> <@> <@>"

#without this, it can't @ anyone, could also change it to a role
allowed_mentions = {
    "users": ["", "", "", ""]
}
#replace with your webhook url
webhook = DiscordWebhook(url='Place URL Here', username="V-Bucks", content=content)

#gives the webhook permission to read the vbucks.png file and attach it to the message
with open("/vbucks.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='vbucks.png')
response = webhook.execute()