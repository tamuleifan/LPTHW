#tell the difference between s() and r()
# repr() is special in that(for types where this is possible) it conventionally
# returns a result that is valid Python syntax
import datetime
d = datetime.date.today()
str(d)
repr(d)