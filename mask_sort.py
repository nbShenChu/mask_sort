import time

def ostrich_sort(arr):
    data = arr.copy()
    for i in range(len(data)-1):
        if data[i+1] < data[i]:
            data[i+1] = data[i] + 1
    return data


if __name__ == "__main__":
    test_data = [12, 15, 9, 22, 17, 5, 8, 13, 4, 19, 1, 6, 25, 28]
    print("===== Mask‑Sort Ostrich Sort Start =====")

    start = time.perf_counter()
    result = ostrich_sort(test_data)
    end = time.perf_counter()

    print("Original array:", test_data)
    print("Mask‑Sort final output:", result)
    print(f"Execution time: {(end - start)*1000:.6f} ms")

    input("\nPress Enter to close the window……")
