import sys
import time

if __name__ == '__main__':

 try:
    duration = int(sys.argv[1])
 except ValueError:
    print("Usage: python main.py <duration_in_seconds>")
    sys.exit()

for i in range(duration):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)
    time.sleep(1)

print("Hello Teacher") #цей запис я додав в gnu-nano
