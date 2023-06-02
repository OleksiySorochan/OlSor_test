import time
import asyncio

start = time.time()

def tic():
    return 'at %1.1f seconds' % (time.time() - start)

async def grl():
    print('grl started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('grl ended work: {}'.format(tic()))

async def grl_2():
    print('grl_2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('grl_2 ended work: {}'.format(tic()))

async def grl_3():
    print("Let's go do some stuff while the coroutines are blocked {}".format(tic()))
    await asyncio.sleep(3)
    print('done')

ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(grl()),
    ioloop.create_task(grl_2()),
    ioloop.create_task(grl_3())
]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()

