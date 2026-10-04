#!/usr/bin/env bash
set -euo pipefail
cd /home/labuser
sudo docker exec netprog-p4-lab4 bash -lc 'cd /tutorials/exercises/basic; make build; python3 /lab/additional/run_checks.py basic' 2>&1 | tee lab4/additional/evidence/basic.log
sudo docker exec netprog-p4-lab4 bash -lc 'cd /tutorials/exercises/basic_tunnel; make build; python3 /lab/additional/run_checks.py basic_tunnel' 2>&1 | tee lab4/additional/evidence/basic_tunnel.log
