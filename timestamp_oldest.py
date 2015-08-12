import datetime
# If you need help, look up datetime.datetime.fromtimestamp()
# Also, remember that you *will not* know how many timestamps
# are coming in.

def timestamp_oldest(*args):
  posix_list = []
  for arg in args:
    posix_list.append(arg)
  posix_list.sort()
  return datetime.datetime.fromtimestamp(posix_list[0])