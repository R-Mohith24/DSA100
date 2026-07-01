```python
def minimumPlatforms(arrival, departure):

    arrival.sort()
    departure.sort()

    i = 0
    j = 0

    platforms = 0
    answer = 0

    while i < len(arrival) and j < len(departure):

        if arrival[i] <= departure[j]:

            platforms += 1
            answer = max(answer, platforms)
            i += 1

        else:

            platforms -= 1
            j += 1

    return answer
```