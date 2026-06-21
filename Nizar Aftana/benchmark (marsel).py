import time
import random
import sys
import matplotlib.pyplot as plt

# Meningkatkan batas rekursi untuk data besar pada Merge Sort jika diperlukan
sys.setrecursionlimit(200000)

# 1. Implementasi 3 Algoritma Sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 2. Setup Pengujian
sizes = [100, 1000, 10000, 50000]
runs = 3
algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Merge Sort': merge_sort
}

results = {alg: [] for alg in algorithms}

print("Memulai Benchmarking... (Mohon tunggu, ukuran data besar memerlukan waktu)\n")

# 3. Proses Benchmarking
for size in sizes:
    print(f"Ukuran Data: {size}")
    for name, alg in algorithms.items():
        # Jangan jalankan O(n^2) pada data 50.000 jika terlalu lama,
        # namun kode ini tetap mencoba menjalankannya.
        if size == 50000 and name in ['Bubble Sort', 'Insertion Sort']:
            print(f"  - {name}: Dilewati atau membutuhkan waktu sangat lama...")
            continue
            
        total_time = 0
        for r in range(runs):
            # Generate data acak yang sama untuk setiap run agar adil
            data = [random.randint(1, 100000) for _ in range(size)]
            
            start_time = time.time()
            alg(data.copy())
            end_time = time.time()
            
            total_time += (end_time - start_time)
            
        avg_time = total_time / runs
        results[name].append(avg_time)
        print(f"  - {name} Rata-rata: {avg_time:.6f} detik")
    print("-" * 40)

# 4. Cetak Tabel Hasil
print("\n=== TABEL HASIL BENCHMARKING (Rata-rata Waktu dalam Detik) ===")
print(f"{'Algoritma':<16} | {'100':<10} | {'1.000':<10} | {'10.000':<10} |")
print("-" * 65)

for name in algorithms:
    # Berikan indentasi (Tab/Spasi) pada 3 baris di bawah ini:
    times = [f"{t:.6f}" if t != float('inf') else "N/A (>5 mnt)" for t in results[name]]
    formatted_times = " | ".join(f"{t:<10}" for t in times)
    print(f"{name:<16} | {formatted_times}")
# 5. Visualisasi Grafik
plt.figure(figsize=(10, 6))
for name, alg_results in results.items():
    # Menggunakan zip untuk menyatukan ukuran dan waktu secara aman
    plot_sizes = []
    plot_times = []
    
    for size, t in zip(sizes, alg_results):
        if t != float('inf'):
            plot_sizes.append(size)
            plot_times.append(t)
            
    plt.plot(plot_sizes, plot_times, marker='o', label=name)
    plot_times = [t for t in alg_results if t != float('inf')]
    plt.plot(plot_sizes, plot_times, marker='o', label=name)

plt.title('Sorting Algorithm Performance Comparison')
plt.xlabel('Ukuran Data (n)')
plt.ylabel('Waktu Eksekusi Rata-rata (detik)')
plt.grid(True)
plt.legend()
plt.savefig('sorting_benchmark_graph.png') # Menyimpan grafik sebagai gambar
plt.show()