#!/usr/bin/env bash

set -o errexit
set -o nounset

uvicorn --host 0.0.0.0 --port 4000 --reload app.main:app
