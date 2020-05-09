import schedule
import jsonify
import time
import requests


def cronJob():
    try:
        r = requests.get("http://nginx:80/cron")
        print(r.status_code)
    except:
        print("Error")


if __name__ == "__main__":
    schedule.every(1).minutes.do(cronJob)
    while True:
        schedule.run_pending()
        time.sleep(1)
