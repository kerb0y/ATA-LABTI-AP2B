import threading
import time

list_provinsi = [
    "Aceh",
    "Sumatera Utara",
    "Sumatera Barat",
    "Riau",
    "Kepulauan Riau",
    "Jambi",
    "Sumatera Selatan",
    "Bangka Belitung",
    "Bengkulu",
    "Lampung",
    "DKI Jakarta",
    "Jawa Barat",
    "Jawa Tengah",
    "DI Yogyakarta",
    "Jawa Timur",
    "Banten",
    "Bali",
    "Nusa Tenggara Barat",
    "Nusa Tenggara Timur",
    "Kalimantan Barat",
    "Kalimantan Tengah",
    "Kalimantan Selatan",
    "Kalimantan Timur",
    "Kalimantan Utara",
    "Sulawesi Utara",
    "Sulawesi Tengah",
    "Sulawesi Selatan",
    "Sulawesi Tenggara",
    "Gorontalo",
    "Sulawesi Barat",
    "Maluku",
    "Maluku Utara",
    "Papua",
    "Papua Barat",
]

def print_provinsi(provinsi):
    time.sleep(1)
    print(f"Provinsi: {provinsi}")

start_time = time.time()

lock = threading.Lock()

threads = []
for provinsi in list_provinsi:
    thread = threading.Thread(target=print_provinsi, args=(provinsi,))
    threads.append(thread)
    thread.start()
    
with lock:
    for thread in threads:
        thread.join()

waktu_berlalu = time.time() - start_time

print(f"Waktu yang berlalu: {waktu_berlalu:.2f} detik")