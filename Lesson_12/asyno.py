import asyncio
# async def count_to_three():
#     print('Subprocess_1')
#     await asyncio.sleep(0)
#     print('Subprocess_2')
#     await asyncio.sleep(0)
#     print('Subprocess_3')
#     await asyncio.sleep(0)
#
# coroutine = count_to_three()
#
# coroutine.send(None)

async def foo():
    print('Running in foo')
    await asyncio.sleep(0)
    print('Explicit context swich to foo again')

async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Imlicit context swith back to bar')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()