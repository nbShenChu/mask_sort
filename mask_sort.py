def mask_sort(arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            right_part = arr[i+1:]
            return mask_sort(right_part)
    return arr


test_data = [12, 15, 9, 22, 17, 5, 8, 13, 4, 19, 1, 6, 25, 28]
print("===== Mask‑Sort (Ostrich Sort) Start =====")
result = mask_sort(test_data)

print("Original array:", test_data)
print("Mask‑Sort final output:", result)

input("\nPress Enter to close the window……")
