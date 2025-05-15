import threading
import time
from multiprocessing import Process

def cpu_bound_task():
    # CPU를 사용하는 계산 작업
    count = 0
    for i in range(100_000_000):
        count += i
    return count

def run_threads():
    start_time = time.time()
    
    # 두 개의 스레드 생성
    threads = []
    for _ in range(2):
        thread = threading.Thread(target=cpu_bound_task)
        threads.append(thread)
        thread.start()
    
    # 모든 스레드가 완료될 때까지 대기
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    return end_time - start_time

def run_processes():
    start_time = time.time()
    
    # 두 개의 프로세스 생성
    processes = []
    for _ in range(2):
        process = Process(target=cpu_bound_task)
        processes.append(process)
        process.start()
    
    # 모든 프로세스가 완료될 때까지 대기
    for process in processes:
        process.join()
    
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    print("스레드 실행 시간 (GIL의 영향으로 더 오래 걸림):", run_threads())
    print("프로세스 실행 시간 (GIL의 영향 없음):", run_processes())
