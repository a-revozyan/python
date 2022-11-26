from human_population import human_population
from requests import post
from os import environ

DRIVER_PATH = "C:\Selenium\chromedriver.exe"
TELEGRAM_TOKEN = environ["TOKEN"]
TELEGRAM_CHAT_ID = "-863117164"
apiURL = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
POPULATION_DICT = {
    "total": "",
    "births_today": "",
    "deaths_today": "",
    "added_today": "",
}

def add_dict(total, births, deaths):
    POPULATION_DICT["total"] = str(total).replace(',', '.')
    POPULATION_DICT["births_today"] = str(births).replace(',', '.')
    POPULATION_DICT["deaths_today"] = str(deaths).replace(',', '.')
    POPULATION_DICT["added_today"] = round(float(POPULATION_DICT["births_today"]) - float(POPULATION_DICT["deaths_today"]), 3)

def send_to_telegram():
    try:
        population_info = f"Total population of meatbags: {POPULATION_DICT['total']}\nBirths today of meatbags: {POPULATION_DICT['births_today']}\n" \
                     f"Deaths today of meatbags: {POPULATION_DICT['deaths_today']}\nAdded today of meatbags: {POPULATION_DICT['added_today']}"

        post(apiURL, json={'chat_id': TELEGRAM_CHAT_ID, 'text': population_info})
    except Exception as e:
        print(e)

bot = human_population(path=DRIVER_PATH)
bot.get_population()
add_dict(total=bot.total, births=bot.births_today, deaths=bot.deaths_today)
send_to_telegram()
