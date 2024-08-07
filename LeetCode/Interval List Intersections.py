
# This is a solution in runtime complexity O(n +m) where n
# is the length of 'firstList' and m is the length of 'secondList'.
# were using O(n+m) space to store the output.
def interval_intersection(firstList, secondList):
    i, j = 0, 0
    output = []
    while i < len(firstList) and j < len(secondList):
        l = max(firstList[i][0], secondList[j][0])
        r = min(firstList[i][1], secondList[j][1])
        if l <= r:
            output.append([l, r])

        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return output
