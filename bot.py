# importing required tools
import requests
from datetime import date
import telebot
import socket

today = date.today()
d1 = today.strftime("%d-%m-%Y")

# ----------------------------------------------------------------------------

API_KEY = "xxxxxx"# add here your api key
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 "Hey! Hows it going? To get information about vaccine centers join our discussion group and send "
                 "your area's pincode. \nDiscussion Group Link: https://t.me/joinchat/RkPTpETFr8rx_DAs")

@bot.message_handler(commands=["ip"])
def show(message):
    if message == "ip":
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        bot.reply_to(message,f"Your current server ip is {ip_addr}")
    else:
        bot.reply_to(message,"Please Provide correct command")


def pincode_request(message):
    request = message.text.split()
    if len(request) < 2 or request[0].lower() not in "pincode":
        return False
    else:
        return True


@bot.message_handler(func=pincode_request)
def send_message(message):
    pincode = message.text.split()[1]
    for i in pincode:
        if i == "." or (i >= 'A' and i <= 'z') or len(pincode) != 6:
            bot.reply_to(message, "Invalid PIN! Please enter a valid PINCODE.")
            exit()

    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'.format(pincode,
                                                                                                               d1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
    x = requests.get(url, headers=headers)
    data = x.json()

    # ============================FOR 45+=======================================

    cnt = 1
    listOfAllCentresFor45 = []

    for d in data["sessions"]:
        if d["min_age_limit"] == 45:
            centre_detail = "Centre {0}: ".format(cnt) + "\nCentre Adrress: " + d['name'] + ", " + d[
                "address"] + "\nVaccine: " + d['vaccine'] + "\nAvailable Capacity dose 1: " + str(
                d["available_capacity_dose1"]) + "\nAvailable Capacity dose 2: " + str(
                d["available_capacity_dose2"]) + '\n'
            listOfAllCentresFor45.append(centre_detail)
            centre_detail = ''
            cnt = cnt + 1

    # print(listOfAllCentresFor45)
    if (len(listOfAllCentresFor45) == 0):
        print("Pincode: " + str(pincode) +
              "\nVaccine for age 45 or above is not available!")
    else:
        print("Are you 45+ .. then go and get ur vaccine!")

    # ============================FOR 18+=======================================

    cnt = 1
    listOfAllCentresFor18 = []

    for d in data["sessions"]:
        if d["min_age_limit"] == 18:
            centre_detail = "Centre {0}: ".format(cnt) + "\nCentre Adrress: " + d['name'] + ", " + d[
                "address"] + "\nVaccine: " + d['vaccine'] + "\nAvailable Capacity dose 1: " + str(
                d["available_capacity_dose1"]) + "\nAvailable Capacity dose 2: " + str(
                d["available_capacity_dose2"]) + '\n'
            listOfAllCentresFor18.append(centre_detail)
            centre_detail = ''
            cnt = cnt + 1

    if (len(listOfAllCentresFor18) == 0):
        print("Pincode: " + str(pincode) +
              "\nVaccine for age 18 and above is not available!")
    else:
        print("Are you 18+ .. then go and get ur vaccine!")

    # ============================Sending TELEGRAM MESSAGE=======================================

    messageFor45 = ""

    if len(listOfAllCentresFor45) > 0:
        messageFor45 = messageFor45 + "Pincode: " + str(
            pincode) + "\nAvailable vaccination centres for age 45 and above:\n\n"
        for mess in listOfAllCentresFor45:
            messageFor45 = messageFor45 + mess
            messageFor45 = messageFor45 + "\n"

    else:
        messageFor45 = messageFor45 + "No slot available for 45 and above age"

    base_url = 'https://api.telegram.org/bot_xxxx_/sendMessage?chat_id=-_xxxx_&text={0}'.format(
        messageFor45)
    print("Response:", requests.get(base_url))
    print("Message Sent for 45+!")

    # ----------------------------------------------------------------------------
    messageFor18 = ""

    if len(listOfAllCentresFor18) > 0:
        messageFor18 = messageFor18 + "Pincode: " + str(
            pincode) + "\nAvailable vaccination centres for age 18 and above:\n\n"
        for mess in listOfAllCentresFor18:
            messageFor18 = messageFor18 + mess
            messageFor18 = messageFor18 + "\n"

    else:
        messageFor18 = messageFor18 + "No slot available for 18 and above age"

    base_url = 'https://api.telegram.org/bot_xxxx_/sendMessage?chat_id=-_xxxx_&text={0}'.format(
        messageFor18)
    print("Response:", requests.get(base_url))
    print("Message Sent for 18+!")


bot.polling()
