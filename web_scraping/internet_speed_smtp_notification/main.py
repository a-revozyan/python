from internetspeed import InternetSpeedBot
from smtplib import SMTP
import os

DRIVER_PATH = "C:\Selenium\chromedriver.exe"
ARGS_DICT_GIS = {
    "urls": "https://www.speedtest.net/",
    "x_button": "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a",
    "x_up": "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span",
    "x_down": "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span",
    "x_screen": "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span"
}
ARGS_DICT_SN = {
    "speed_up": "",
    "speed_down": "",
    "my_email": EMAIL@OUTLOOK.COM
    "my_password": os.environ["MAILPASSWORD"],
    "rec": RECEPIENT_EMAIL
}

def smtp_notification(speed_up, speed_down, my_email, my_password, rec):
    with open("letter.txt") as letter:
        letter = letter.read()
        letter = letter.replace("[NAME]", "BotUser")
        letter = letter.replace("[up_speed]", speed_up)
        letter = letter.replace("[down_speed]", speed_down)
    with SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=rec,
                            msg=f"Subject:Internet speed report\n\n {letter}")

bot = InternetSpeedBot(path=DRIVER_PATH)
bot.get_internet_speed(**ARGS_DICT_GIS)
ARGS_DICT_SN["speed_up"] = bot.up
ARGS_DICT_SN["speed_down"] = bot.down
smtp_notification(**ARGS_DICT_SN)

