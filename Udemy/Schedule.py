#pip install schedule
import schedule
import time

'''
def hello():
    print('hello...')

def hi():
    print('hi...')

schedule.every(10).seconds.do(hello)
schedule.every(5).seconds.do(hi)

while True:
    schedule.run_pending()
'''
def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)