#!/bin/sh

dropdb latpro
createdb latpro
psql -d latpro -f prometheus_genesis.sql
./gen.py gen.sql
psql -d latpro -f gen.sql
