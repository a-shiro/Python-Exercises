string = input()

occurrence_count = {}

for ch in string:

    if ch not in occurrence_count:
        occurrence_count[ch] = 0
    occurrence_count[ch] += 1
[print(f"{k}: {v} time/s") for k, v in sorted(occurrence_count.items())]