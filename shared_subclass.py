import asyncio
import random
class LilClass:
  def __init__(self, name):
    self.name = f"dude i'm subclass {name}"
    self.calls = 1

  async def mylilcoroutine(self, caller):
    """
    OtherSubClass does mylilcoroutines
    """
    await asyncio.sleep(random.random())
    print(f"{self.name}, called: {self.calls} by {caller}")
    self.calls+= 1

  async def acouplelilcoroutines(self, caller):
    coros = []
    for i in range(0,5):
      coros.append(self.mylilcoroutine(caller))
    await asyncio.gather(*coros)
    


class TopClass:
  def __init__(self, name, subs):
    self.name = name
    self.formal_name = f"dude i'm main {name}"
    self.subs = subs

  async def bigolecoroutine(self):
    await asyncio.sleep(2)
    await asyncio.gather(*[s.acouplelilcoroutines(self.name) for s in self.subs])
    print(self.formal_name)


async def main():
  sub = LilClass("lil")
  t1 = TopClass("one", 
                subs=[sub])
  t2 = TopClass("two", 
                subs=[sub])

  await asyncio.gather(*[t1.bigolecoroutine(), t2.bigolecoroutine()])
if __name__ == "__main__":
  asyncio.run(main())
  
