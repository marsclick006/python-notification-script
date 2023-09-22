import requests
import socket
import time
import os


# Define environment variables

url = f'{os.environ.get("REQUEST_URL")}'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'{os.environ.get("AUTH")}'
}
data = f'{os.environ.get("REQUEST_DATA")}'
webhookUrl = f'{os.environ.get("WEBHOOK_URL")}'
webhookHeaders = {
    'Content-Type': 'application/json'
}

# The ip address of the response
parsed_url = requests.utils.urlparse(url)
host = parsed_url.netloc
ip = socket.gethostbyname(host)


while True:
    time.sleep(5)
    response = requests.post(url, headers=headers, data=data, verify=False)
    # İsteğin süresi
    response_time = response.elapsed.total_seconds() * 1000
    # HTTP durum kodu
    http_code = response.status_code
    # Response
    response_body = response.text
    Response = (
        "```API RESPONSE REPORT```\n"
        f"```Response Süresi: {response_time:.2f} ms```\n"
        f"```Dönen IP Adresi: {ip}```\n"
        f"```HTTP Code: {http_code}```\n"
        f"```Response Body: {response_body}```\n"
    )
    responsePayload = {
        'text': Response,
    }
    if response_time > 650.00:
        webhookResponse = requests.post(url=webhookUrl, headers=webhookHeaders, json=responsePayload)
        print(response_time)

