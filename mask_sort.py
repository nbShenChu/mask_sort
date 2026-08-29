from typing import List


def mask_sort(arr: List[int]) -> List[int]:
    """
    Mask Sort（掩耳盗铃排序）
    时间复杂度: O(n)
    空间复杂度: O(n)  # 递归栈 + 切片产生新列表
    特性: 非稳定、【有损算法！会丢弃大量数据】、递归实现

    ⚠️ IMPORTANT：这是趣味恶搞算法，**不是真正排序！禁止业务环境使用！**
    逻辑：从左向右扫描，遇到第一处逆序，直接抛弃左侧全部数据，递归处理后缀。
    只会返回数组末尾一段天然连续递增片段，大量输入元素会直接丢失。

    :param arr: 输入整数列表
    :return: 右侧连续递增的新列表
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
    print(f"原始:{data}")
    print(f"输出:{res}")

    # 卡住控制台窗口，按回车才关闭，防止直接闪退
    input("\n按回车键关闭窗口……")