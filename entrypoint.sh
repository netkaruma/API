

set -e


echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Database started"


echo "Waiting for Redis..."
while ! nc -z redis 6379; do
  sleep 0.1
done
echo "Redis started"

python API/manage.py migrate --noinput

python API/manage.py collectstatic --noinput --clear


if [ "$CREATE_SUPERUSER" = "true" ]; then
  python API/manage.py createsuperuser --noinput || true
fi

exec "$@"