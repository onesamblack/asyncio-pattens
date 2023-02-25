# asyncio-pattens
Patterns used in python's asyncio lib.
(This is also me whining about asyncio) 

**Warning**: Asyncio in python is really annoying. If you're starting a fresh project: use a language where you can control threading directly (e.g. golang, C++). But, if you're going to use it, here's some patterns to use to cut through debugging nightmares. 

FYI - use at your own risk. See warning above.

## Patterns

- Sequential tasks: `sequential.py`

Sometimes you need to do one thing, then wait for the result, then do another thing. This is frowned upon in asyncio, where everything needs to be a callback to a callback to a callback to a callback, ad infinitum.


## Testing

Nothing is tested. Everything is live.

![live](https://media.tenor.com/VyodLiYTspcAAAAd/bill-o-reilly-fuck-it.gif)
