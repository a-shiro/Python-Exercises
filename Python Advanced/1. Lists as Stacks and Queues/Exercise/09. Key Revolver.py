from collections import deque

bullet_price = int(input())
gun_clip_size = int(input())

bullets = [int(b) for b in input().split()]
locks = deque([int(lock) for lock in input().split()])

intelligence_value = int(input())

gun_clip = gun_clip_size
money_earned = intelligence_value

while locks:

    bullet, lock = bullets[-1], locks[0]

    if bullet <= lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    bullets.pop()
    gun_clip -= 1
    money_earned -= bullet_price

    if len(bullets) == 0:
        break
    elif gun_clip == 0:
        print("Reloading!")
        gun_clip = gun_clip_size

if len(locks) == 0:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

