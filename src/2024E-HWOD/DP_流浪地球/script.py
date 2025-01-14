def simulate_engine_startup(n, manual_starts):
    engines = [False] * n  # Initialize all engines as not started
    start_times = [float('inf')] * n  # Initialize start times as infinity

    for t, p in manual_starts:
        start_times[p] = min(start_times[p], t)  # Update manual start time

    time = 0
    while not all(engines):
        time += 1
        for i in range(n):
            if start_times[i] == time:
                engines[i] = True
                # Handle adjacent engines
                left = (i - 1) % n
                right = (i + 1) % n
                if not engines[left]:
                    start_times[left] = min(start_times[left], time + 1)
                if not engines[right]:
                    start_times[right] = min(start_times[right], time + 1)

    # Find the latest started engines
    latest_start_time = max(start_times)
    latest_engines = [i for i in range(n) if start_times[i] == latest_start_time]

    print(len(latest_engines))
    print(' '.join(map(str, sorted(latest_engines))))

# Example usage:
n, e = map(int, input().split())
manual_starts = []
for _ in range(e):
    t, p = map(int, input().split())
    manual_starts.append((t, p))

simulate_engine_startup(n, manual_starts)
