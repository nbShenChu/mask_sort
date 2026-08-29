from typing import List


def mask_sort(arr: List[int]) -> List[int]:
    """
    Mask Sort (Alias: Cover‑Ears Bell Sort) 🎭

    Time Complexity: O(n)
    Space Complexity: O(n)  # Recursion stack + new list created by slicing
    Property: Non‑stable, lossy joke algorithm, recursive implementation.

    ⚠️ IMPORTANT: This is a humorous joke algorithm, NOT real sorting! DO NOT use in production!
    Logic: Scan the array from left to right. When the first out‑of‑order pair is found,
    discard all left‑side data and recursively process the remaining right‑hand suffix.
    Only the naturally incremental suffix at the end will be returned; most input elements will be lost.

    :param arr: Input integer list
    :return: New list of the right‑hand continuous incremental suffix
    """
    if not arr or len(arr) == 1:
        return arr

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            right_part = arr[i + 1:]
            return mask_sort(right_part)

    return arr


if __name__ == "__main__":
    data = [12, 15, 9, 22, 17, 5, 8, 13, 4, 19, 1, 6, 25, 28]
    res = mask_sort(data)
    print(f"Original: {data}")
    print(f"Output: {res}")

    # Hold console window, press Enter to exit, prevent window from closing instantly
    input("\nPress Enter to close window……")
