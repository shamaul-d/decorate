import time

def timed(f):
  def wrapper(*args, **kwds):
	start = time.time()
	result = f(*args, **kwds)
	elapsed = time.time() - start
	print "%s took %d seconds to finish" % (f.__name__, elapsed)
	return result
  return wrapper


@timed
def my_function(x, y, z):
	num_list = []
	time.sleep(5)
	for num in (range(0, 10000)):
		num_list.append(num)
	print("\nSum of all the numbers: " + str((sum(num_list))))


print(my_function(1, 2, 3))
