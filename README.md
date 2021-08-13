## TGForwarderClient - forward messages from channels to chats in Telegram

### Tutorial

1. Visit [Telegram Apps API](https://my.telegram.org/apps) and login with your Telegram Account.
2. Fill out the form to register a new Telegram application.
3. After registration you get an API key. It consists of two parts: `api_id` and `api_hash` - set those as env variables to `$API_ID` and `$API_HASH` (you can save them for persistence to `.env` file).
4. Run the app interactively:
```docker run -it -e API_ID -e API_HASH qqalexqq/tgforwarderclient:latest python export_session.py```
5. Input your data:
```Enter phone number or bot token: 9876543210
Is "+9876543210" correct? (y/N): y
The confirmation code has been sent via Telegram app
Enter confirmation code: 123456
The two-step verification is enabled and a password is required
Password hint: None
Enter password (empty to recover): verysecurepassword
---
abcdefghijklmnopqrstuvwxyz (ver long string)
```
6. Copy the last long string from the output. Set it to an env var `$SESSION_KEY`.
7. Set forwarding variables in docker-compose.yml: `BOT_CHANNELS` (from where we forward) and `BOT_CHATS` (to which chats we forward). Examples are provided in the file.

8. After all things done you can start the container:
```
docker-compose build
docker-compose up -d
```

### Usage

with docker...

```shell
docker run ghcr.io/qqalexqq/tgforwarderclient --help
```

... or as python module

```shell
python3 -m tgforwarderclient --help
```
