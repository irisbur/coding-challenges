# The relatively naive solution I quickly came up with involves iterating over all values in nums2 and finding
# the best fit for each value in the nums1 array.
# This solution takes no extra memory, so it has O(1) space complexity.
# It iterates over both arrays, nums1 and nums2, exactly once, giving us O(n + m) time complexity.
# However, inserting into a Python list takes O(n) time, resulting in O(n^2 + mn) time complexity, which is not optimal.
# By using a linked list we can achieve O(1) insertion time and get O(n + m) running time.

def merge(nums1, m, nums2, n):
    if m == 0:
        nums1[:] = nums2
        return
    if n == 0:
        return
    if nums1[m - 1] <= nums2[0]:
        nums1 = nums1[:m] + nums2
    if nums2[n - 1] <= nums1[0]:
        nums1 = nums2 + nums1[:m]
    i, j = 0, 0
    while i < n:
        while j < m:
            if nums1[j] > nums2[i]:
                nums1.insert(j, nums2[i])
                m += 1
                j += 1
                i += 1
                break
            elif j == m - 1:
                nums1[m:] = nums2[i:]
                i = n  # this is to exit outer while
                break
            j += 1
    return


# I can improve this solution by using a copy of nums1 and copying the relevant value to nums1.
# this will provide a solution with space complexity O(m) and time complexity O(n+m).
def merge_with_copy(nums1, m, nums2, n):
    copy_in1 = nums1[:m]
    i, j = 0, 0

    while i < n and j < m:
        if copy_in1[j] <= nums2[i]:
            nums1[i + j] = copy_in1[j]
            j += 1
        else:
            nums1[i + j] = nums2[i]
            i += 1
    if i < n:
        nums1[i+j:] = nums2[i:]
    if j < m:
        nums1[i+j:] = copy_in1[j:]


# A solution that does not use extra memory is copying the biggest value to the correct index from the end
# into nums1, that way we can utilize the empty space and take advantage of that space to get a solution in
# O(n+m) time complexity as we wanted and use O(1) memory as intended in the question.
def merge_constant_space(nums1, m, nums2, n):
    if n == 0:
        return
    if m == 0:
        nums1[:] = nums2
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]


if __name__ == '__main__':
    in1 = [1,2,3,0,0,0]
    in2 = [2,5,6]
    merge_constant_space(nums1=in1, m=3, nums2=in2, n=3)
    print(in1)

