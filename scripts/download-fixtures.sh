#!/bin/sh
# Downloads the test fixtures from the mirror.
set -eu
curl -fsS -o fixtures.txt http://127.0.0.1:8765/fixtures.txt
grep -q "fixtures v1" fixtures.txt
echo "Fixtures downloaded."
