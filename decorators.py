import time

def timed(f):
  def wrapper(*args, **kwds):
	start = time.time()
	result = f(*args, **kwds)
	elapsed = time.time() - start
	print "%s took %d seconds to finish" % (f.__name__, elapsed)
	return result
  return wrapper

def named(f):
  def wrapper(*args, **kwds):
  	result = f(*args, **kwds)
	print f.func_name
	print "args: " + str(args)
	return result
  return wrapper


@timed
@named
def my_function(x, y, z):
	num_list = []
	time.sleep(5)
	for num in (range(0, 10000)):
		num_list.append(num)
	print("\nSum of all the numbers: " + str((sum(num_list))))


my_function(1, 2, 3)
