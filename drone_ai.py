import random
import time

print("=== Anti-Jamming Drone System Demo ===")

هدف = {"x": 100, "y": 100}
الدرون = {"x": 0, "y": 0, "الهدف": هدف}

def التحرك_نحو_الهدف(الدرون):
    if الدرون["x"] < الدرون["الهدف"]["x"]: الدرون["x"] += 10
    if الدرون["y"] < الدرون["الهدف"]["y"]: الدرون["y"] += 10
    return الدرون

def التشويش(): return random.random() < 0.3

for دقيقة in range(12):
    حالة = "JAMMING! ❌" if التشويش() else "Connection OK ✅"
    الدرون = التحرك_نحو_الهدف(الدرون)
    print(f"Minute {دقيقة}: {حالة}")
    print(f"Drone Position: x={الدرون['x']} y={الدرون['y']}")
    if الدرون["x"] >= 100 and الدرون["y"] >= 100:
        print("=== MISSION SUCCESS! ==="); break
    time.sleep(1)
