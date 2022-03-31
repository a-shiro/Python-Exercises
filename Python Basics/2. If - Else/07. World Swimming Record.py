world_record = float(input())
meters = float(input())
time_for_1_meter = float(input())

need_to_swim = meters * time_for_1_meter
added_swim_time = meters // 15 * 12.5
total_time = need_to_swim + added_swim_time

if total_time >= world_record:
    total_time = total_time - world_record
    print(f"No, he failed! He was {total_time:.2f} seconds slower.")

elif total_time < world_record:

    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")