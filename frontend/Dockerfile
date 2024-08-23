FROM python:3.12.3

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN --mount=type=cache,mode=0755,target=/root/.cache \
  pip install -r requirements.txt

COPY ./src ./src

CMD ["python", "-m", "streamlit", "run", "src/streamlit_app.py", "--server.port=80", "--server.address=0.0.0.0"]
