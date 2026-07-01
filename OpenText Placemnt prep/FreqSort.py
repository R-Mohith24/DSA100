def frequencySort(arr):

    # Step 1: Count frequency
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Create (frequency, value) pairs
    pairs = []

    for num in freq:
        pairs.append((freq[num], num))

    # Step 3: Sort in descending order
    pairs.sort(reverse=True)

    # Step 4: Build answer
    answer = []

    for frequency, value in pairs:
        for i in range(frequency):
            answer.append(value)

    return answer