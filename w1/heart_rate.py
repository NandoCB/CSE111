heartbeat = 220
age = int(input('Please enter your age: '))

heart_rate = (heartbeat - age)

max_heart_rate = (heart_rate*85)/100

min_heart_rate = (heart_rate*65)/100

print(f'When you exercise to strengthen your heart, you should keep your heart rate between {min_heart_rate:.0f} and {max_heart_rate:.0f} beats per minute.'.format(max_heart_rate, min_heart_rate))