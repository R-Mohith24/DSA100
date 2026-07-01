import bisect

def minimumTime(binary, coordinates):

    # Store coordinates of all initial 1s
    sources = []

    for i in range(len(binary)):
        if binary[i] == 1:
            sources.append(coordinates[i])

    # No source exists
    if len(sources) == 0:
        return -1

    answer = 0

    # Process every 0
    for i in range(len(binary)):

        if binary[i] == 0:

            current = coordinates[i]

            # Position where current would be inserted
            pos = bisect.bisect_left(sources, current)

            nearest = float("inf")

            # Check left source
            if pos > 0:
                nearest = min(nearest, current - sources[pos - 1])

            # Check right source
            if pos < len(sources):
                nearest = min(nearest, sources[pos] - current)

            # Keep the maximum time
            answer = max(answer, nearest)

    return answer