import time
print('123')
time.sleep(2)
with open('models.py', 'a') as f:
    f.write('print("123")')
print('456')
