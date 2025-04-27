# Password Cracker Drill

## Summary
Python script that brute-forces a local web server protected by a 3-digit PIN using raw sockets.

## How I found the server address and port
- Observed executable logs / used Wireshark.

## How I determined the HTTP request
- Used Postman to manually craft a working POST request.
- Observed correct format, headers, and body.

## Challenges
- Server introduced slowdown → Added time.sleep(0.5) between requests.

## Security Improvements
- Implement rate limiting, CAPTCHA, account lockouts after failed attempts.

## Video Tutorial
[YouTube Link or Embedded Link]
