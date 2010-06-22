import glib

IO_IN = glib.IO_IN
IO_OUT = glib.IO_OUT
IO_ERR = glib.IO_ERR
IO_HUP = glib.IO_HUP
IO_NVAL = glib.IO_NVAL

def io_in(n):
	return n & IO_IN

def io_out(n):
	return n & IO_OUT

def io_err(n):
	return n & IO_ERR or n & IO_HUP or n & IO_NVAL

def watch_fd(sk, cb, *args):
	return glib.io_add_watch(sk, IO_IN | IO_ERR | IO_HUP | IO_NVAL,
					cb, *args)

def watch_fd_err(sk, cb, *args):
	return glib.io_add_watch(sk, IO_ERR | IO_HUP | IO_NVAL,
					cb, *args)

def timeout_call(to, cb, *args):
	return glib.timeout_add(to, cb, *args)

def idle_call(cb, *args):
	return glib.idle_add(cb, *args)