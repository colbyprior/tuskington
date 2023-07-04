#!/bin/sh

OUT=${ACCESS_LOG:-/proc/1/fd/1}
gunicorn app:app \
    -w 1 \
    --threads 3 \
    -b 0.0.0.0:5000 \
    --reload \
    --access-logfile "$OUT" \
    --error-logfile "$OUT" \
    --log-level 'info' \
    --access-logformat '%({x-forwarded-for}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
