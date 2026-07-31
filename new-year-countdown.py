# Goal: Print a countdown before somethng "exciting" happens(like "launching....." or "Happy new Year!").
import time

countdown = int(input("countdown starts :"))
print("\n Countdown starts now: ")
for i in range(countdown, 0, -1):
    print(i) 
    time.sleep(1)

print("\nwOHoooooooOOOoOOOOO Happy new Year")



