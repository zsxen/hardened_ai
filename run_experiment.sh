#!/bin/bash
set -e
# 1) 빌드와 기동
docker-compose build
docker-compose up -d
sleep 2

# 2) 수집 시작 (background) - collector/collect.sh 를 실행
bash collector/collect.sh &

# 3) benign traffic generator (간단)
python3 scripts/benign_generator.py &

# 4) Start fuzzer after short wait
sleep 5
python3 fuzz/fuzzer.py

# 5) 종료: docker-compose down 등은 수동으로