#!/usr/bin/env bash

rq worker --url redis://redis-server:6379 orders
