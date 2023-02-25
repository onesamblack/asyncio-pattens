import asyncio
import time
from datetime import datetime



def print_time():
  t = time.time()
  ts = datetime.fromtimestamp(t)
  print(ts.strftime("%H:%M:%S"))
  
async def dosomething():
  print_time()
  await asyncio.sleep(10)
  print("did something")
  print_time()
  
async def dosomething_butwithargs(arg1):
  print_time()
  await asyncio.sleep(5)
  print(f"did {arg1}")
  print_time()

async def main():
  r1 = asyncio.create_task(dosomething())
  await asyncio.wait({r1})
  r2 = asyncio.create_task(dosomething_butwithargs("duuuuuuude"))
  await asyncio.wait({r2})
  r3 = asyncio.create_task(dosomething())
  await asyncio.wait({r3})
if __name__ == "__main__":
  asyncio.run(main())
