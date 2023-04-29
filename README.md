# Requirement

- docker-compose

# Setup

## 0. Set environment variables

### 0.1. Env for docker-compose

Create `./.env` file and update like following.

```
### develop & production ###
COMPOSE_FILE=docker-compose.develop.yml # or docker-compose.production.yml
PROCESSES=1 # sohuld be same as the number of CPU cores
###

### only production ###
DOMAIN=example.com # server domain

# HTTPS_PORTAL_STAGE: local / staging / production
# Only "production" option publishes valid certificate.
# Before using "production", try "staging"!
# Please check https://github.com/SteveLTN/https-portal
HTTPS_PORTAL_STAGE=local
###
```

### 0.2. Env for Django

Create `./app/.django-env` file and update like following.

```
### develop & production ###
CLIENT_ORIGIN_URL=http://127.0.0.1:3000
ALLOWED_HOST=127.0.0.1

### only production ###
SECRET_KEY=

###
```

## 1. Setup container

```bash
docker-compose build
```

```bash
docker-compose up -d
```

Wait several seconds.

In production env, Server is run automatically.

## 2. [Only develop env] Run server

You can skip this step in production envronment.

```bash
docker-compose exec app python3 manage.py runserver 0.0.0.0:8000
```

## 3. Test API

develop

```bash
curl http://http://127.0.0.1:8000/
```

production

```bash
curl https://{domain}/
```

In production, SSL certificate problem may be returned depending on HTTPS_PORTAL_STAGE.
But it's OK.

## 4. [Only production env] SSL setting

### 4.1. Run with staging option

Set environment variable `HTTPS_PORTAL_STAGE=staging` and run docker compose. (Already done)

Access to `https://{domain}` from any browser. If it works, it's ok.

### 4.2. Reset server

```
docker-compose down
```

### 4.3. Run server with production mode

Edit `.env`, set environment variable `HTTPS_PORTAL_STAGE=production`.

Run docker compose again.

```
docker-compose up -d
```

Finally you can access to server with `https://{domain}` .

# Maintenance

## Restart server

When something issue happens

```bash
docker-compose restart
```

## Code update

```bash
git pull
```

```bash
docker-compose restart
```

Don't worry. DB data and certificate data are kept.

## Backup DB data

Backup

```bash
docker-compose exec db mysqldump --single-transaction --no-tablespaces -u django --password="django" --databases trivia-map-db > output.dump
```

Restore

```bash
docker-compose exec -T db mysql -u django --password="django" trivia-map-db < output.dump
```

## Clean up

Remove unused images.

```bash
docker image prune
```

Remove unused containers.

```bash
docker container prune
```

Remove unused volumes.

```bash
docker volume prune
```

## Caution!: Reset containers totally

All volume data including DB data and certificate data is removed.

```bash
docker-compose down -v
```

# Log files

- http-portal log: `server/log`
- Django log: `app/log/`
