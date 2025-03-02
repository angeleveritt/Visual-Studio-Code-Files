def merge_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    mid_point = len(unsorted) // 2
    left_half_half = unsorted[:mid_point]
    right_half_half = unsorted[mid_point:]

    left_half_half = merge_sort(left_half_half)
    right_half_half = merge_sort(right_half_half)
    return merge(left_half_half, right_half_half)


def merge(left_half, right_half):
    result = []
    left_half_idx = 0
    right_half_idx = 0

    # Compare and add smaller to result
    while left_half_idx < len(left_half) and right_half_idx < len(right_half):
        if left_half[left_half_idx] <= right_half[right_half_idx]:
            result.append(left_half[left_half_idx])
            left_half_idx += 1
        else:
            result.append(right_half[right_half_idx])
            right_half_idx += 1

    # Add remainder from left_half
    result.extend(left_half[left_half_idx:])

    # Add any remainder from right_half
    result.extend(right_half[right_half_idx:])

    return result


if __name__ == "__main__":
    test_list = [5, 100, 23, 54, 8, 0, -4, 76]
    print("original:", test_list)

    sorted_list = merge_sort(test_list)
    print("sorted:", sorted_list)

    test_list = [49, 23, 12, 0, -1, 100, 101]
    print("original:", test_list)

    sorted_list = merge_sort(test_list)
    print("sorted:", sorted_list)
