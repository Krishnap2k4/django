#!/bin/bash
set -e

echo "Waiting for MySQL..."
while ! python -c "import pymysql; pymysql.connect(host='$MYSQL_HOST', port=int('$MYSQL_PORT'), user='$MYSQL_USER', password='$MYSQL_PASSWORD')" 2>/dev/null; do
    sleep 1
done
echo "MySQL is ready!"

echo "Waiting for Redis..."
while ! python -c "import redis; redis.Redis(host='$REDIS_HOST', port=int('$REDIS_PORT')).ping()" 2>/dev/null; do
    sleep 1
done
echo "Redis is ready!"

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput 2>/dev/null || true

exec "$@"
