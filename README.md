# API Response Notification

This script requests to your API. It takes response, response time, http code and the server's ip address that responses. After that, it sends notification that you want to send notification channel's webhook like Slack and Mattermost.


## Environment Variables

| Environment Variables             | Description                 | Example |
| ----------------- |:-----------------------|:-----------------------|
| REQUEST_URL       | The URL that you want to request | https://www.example.com/api/v1/post 
| WEBHOOK_URL       | Webhook URL that you will send notification | https://www.slack.com/hooks/xxxxxxxxxxxxxxxxxxxxxxx
| REQUEST_DATA       | Request body that you requests to REQUEST_URL  | {"fruit": "apple"}
| AUTH       | Authentication headers for requesting to REQUEST_URL | Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


