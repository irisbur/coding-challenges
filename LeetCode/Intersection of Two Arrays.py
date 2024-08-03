
# In this approach we iterate through the values is nums1 and look for them in nums2,
# if they appear in nums2 as well we add them to a list. If nums1 is in length n amd nums2 is in
# length m, since were using sets the average time complexity is O(n+m) but at worst case it might be O(n*m).
def find_intersection(nums1, nums2):
    nums_set1 = set(nums1)
    nums_set2 = set(nums2)
    intersection = []
    for num in nums_set1:
        if num in nums_set2:
            intersection.append(num)

    return intersection
