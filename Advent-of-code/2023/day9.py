
# Part 1 #

def predict_next_value(sequence):
    nums = [int(num) for num in sequence]
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    last_values = [nums[-1]]
    while diffs != [0] * len(diffs):
        last_values.append(diffs[-1])
        diffs = [diffs[i] - diffs[i - 1] for i in range(1, len(diffs))]
    return sum(last_values)


def sum_predictions():
    with (open("input.txt", "r") as input_file):
        sequences = input_file.readlines()
        return sum([predict_next_value(seq.split()) for seq in sequences])

# Part 2 #


def predict_prev_value(sequence):
    nums = [int(num) for num in sequence]
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    first_values = [nums[0]]
    while diffs != [0] * len(diffs):
        first_values.append(diffs[0])
        diffs = [diffs[i] - diffs[i - 1] for i in range(1, len(diffs))]
    previous_value = 0
    for i in range(len(first_values) - 1, -1, -1):
        previous_value = first_values[i] - previous_value
    return previous_value


def sum_predictions_previous_value():
    with (open("input.txt", "r") as input_file):
        sequences = input_file.readlines()
        return sum([predict_prev_value(seq.split()) for seq in sequences])

if __name__ == "__main__":
    print(sum_predictions_previous_value())