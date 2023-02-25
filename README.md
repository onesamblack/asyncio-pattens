# asyncio-pattens
Patterns used in python's asyncio lib.
(This is also me whining about asyncio) 

**Warning**: Asyncio in python is really annoying. If you're starting a fresh project: use a language where you can control threading directly (e.g. golang, C++). But, if you're going to use it, here's some patterns to use to cut through debugging nightmares. 

FYI - use at your own risk. See warning above.

## Patterns

### Sequential 

See `sequential.py`

Sometimes you need to do one thing, then wait for the result, then do another thing. This is frowned upon in asyncio, where everything needs to be a callback to a callback to a callback to a callback, ad infinitum.

Uses 

### Shared subclass

See `shared_subclass.py`

Multiple instances of a higher order class run a coroutine that uses the same instance of another class: `shared_subclass_coroutines.py`

This pattern is for an async class [multiple instances] in an application using the same instance [one instance] of another class to do it's function. Lots of `asyncio.gather()`

Examples:
  - you have multiple chat clients (`ChatClient()`) who all use the same metadata class (`Metadata()`) to retrieve and store information about chats
  - you have multiple worker classes (`Workers()`) who all use the same db client to store data (`MyAsyncDB()`)
 
 Caveats:
  - check for threadsafety
  - watch where you use `await`, lest you could run things non-concurrently!
  - if not threadsafe, RUN!


## Testing

Nothing is tested. Everything is live.

![live](https://media.tenor.com/VyodLiYTspcAAAAd/bill-o-reilly-fuck-it.gif)
