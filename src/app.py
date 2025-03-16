from fastapi import FastAPI
import os
import socket
import random
import time

app = FastAPI()
VERSION = os.getenv("APP_VERSION", "1.0.0")
HOSTNAME = socket.gethostname()

@app.get("/")
def read_root():
    return {
        "message": "Hello from Istio Demo Service!",
        "version": VERSION,
        "hostname": HOSTNAME
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/data")
def get_data():
    # 가끔 지연 시뮬레이션 (Istio 타임아웃 테스트용)
    if random.random() < 0.1:  # 10% 확률로 지연
        time.sleep(2)
    return {"data": "Sample data from v1", "source": HOSTNAME}

@app.get("/api/v2/data")
def get_data_v2():
    return {"data": "Enhanced data from v2", "source": HOSTNAME}
