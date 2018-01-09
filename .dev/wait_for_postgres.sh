#!/bin/bash
# wait-for-postgres.sh

set -e

host="db"
user="mydbuser"
shift
cmd="$@"

until pg_isready -h "$host" -U "$user"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 3
done

>&2 echo "Postgres is up - executing command"
exec ${cmd}
