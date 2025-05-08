import time
import threading
from multiprocessing import Process

def heavy_task():
    total = 0
    for _ in range(10_000_000):
        total += 1

### ✅ 멀티스레딩 테스트
def run_threading():
    print("🔁 스레드 시작")
    start = time.time()

    threads = [threading.Thread(target=heavy_task) for _ in range(8)]
    for t in threads: t.start()
    for t in threads: t.join()

    print(f"🕒 스레드 걸린 시간: {time.time() - start:.2f}초")

### ✅ 멀티프로세싱 테스트
def run_multiprocessing():
    print("⚙️ 프로세스 시작")
    start = time.time()

    processes = [Process(target=heavy_task) for _ in range(8)]
    for p in processes: p.start()
    for p in processes: p.join()

    print(f"🚀 프로세스 걸린 시간: {time.time() - start:.2f}초")

### 🚀 실행
if __name__ == '__main__':
    run_threading()
    print()
    run_multiprocessing()