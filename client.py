import time
import requests
import schedule

def send_request(server, port):
    try:
        response = requests.get(f'http://{server}:{port}/hello', headers={'Connection':'close'})
        print(f"Sent request to {server}:{port}, received: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {server}:{port}: {e}")

def job():
    send_request('server1', 8080)
    time.sleep(1)
    send_request('server2', 8081)
    time.sleep(1)

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
