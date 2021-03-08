"""Range example."""

start: int = 0
stop: int = 101  # stop is 10, start is 1, and step is 1 by default
step: int = 10  

a_range: range = range(start, stop, step)
print(a_range.start)
print(a_range.stop)
print(a_range.step)
