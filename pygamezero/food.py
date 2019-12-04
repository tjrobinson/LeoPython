import time
import random

leoeaten = 0
daddyeaten = 0
mummyeaten = 0
minutes = random.randint(0,5)

if minutes != 0:
    if minutes > 1:
        print("They have just over", minutes, "minutes!")
    else:
        print("They have just over", minutes, "minute!")
for x in range(minutes):
    if minutes != 0:
        def after():
            global leoeaten
            global daddyeaten
            global mummyeaten
            time.sleep(random.randint(50,60))
            leoeaten = leoeaten + 1
            print("Leo ate a sweet!")
            time.sleep(random.randint(0,10))
            mummyeaten = mummyeaten + 1
            print("Mummy ate one too!")
            time.sleep(random.randint(0,5))
            daddyeaten = daddyeaten + 1
            print("So did Daddy!")
        after()
print("Daddy ate", daddyeaten, "sweets!")
print("Mummy ate", mummyeaten, "sweets!")
print("Leo ate", leoeaten, "sweets!")
