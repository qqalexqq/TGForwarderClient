FROM python:3.9-slim

ADD requirements.txt ./
RUN pip install -r requirements.txt -U
ADD tgforwarderclient/ ./
ADD export_session.py ./

CMD ["python", "-m", "tgforwarderclient"]
