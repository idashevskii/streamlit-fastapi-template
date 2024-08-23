
## Local Development

Copy file `.env.example` to `.env` and adjust configuration.

Run:

```bash
docker compose up -d --build
```

Open in browser:
- [API Docs](http://localhost/api/docs)
- [UI](http://localhost/)


### OPTIONAL: Install dependecies on host

In folders `./backend` and `./frontend` run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
```


## Deploy to Production

Copy file `.env.example` to `.env` and adjust configuration.

Run:

```bash
./scripts/prod-run.sh
```
