import threading
import time

def handler(started=0, finished=0):
    result  = 0
    for i in range(started, finished):
        result += 1
    results.append(result)

results = []

# Start with threading

task_1 = threading.Thread(
    target=handler,
    kwargs={'finished': 2 ** 12, }
)

task_2 = threading.Thread(
    target=handler,
    kwargs={'started': 2 ** 12, 'finished': 2 ** 24 }
)

strted_at = time.time()

task_1.start()
task_2.start()

task_1.join()
task_2.join()

print('RESULTS 1')
print(f'Time: {time.time() - strted_at}')
print('Value: ', sum(results))


# Start without threading
results = []
strted_at = time.time()
handler(finished=2 ** 24)
print('RESULTS 2')
print(f'Time {time.time() - strted_at}')
print('Value: ', sum(results))