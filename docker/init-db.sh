#!/bin/sh
set -e

# Environment variables
export PGPASSWORD="$POSTGRES_PASSWORD"

# Create database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE treasury;
    GRANT ALL PRIVILEGES ON DATABASE treasury TO $POSTGRES_USER;
EOSQL

# Create test database
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE treasury_test;
    GRANT ALL PRIVILEGES ON DATABASE treasury_test TO $POSTGRES_USER;
EOSQL
