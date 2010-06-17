from mcap_defs import *
from mcap import *

# The API of MCAPInstance mimics closely the mcap_test_plugin implemented
# for BlueZ / OpenHealth HDP and MCAP. D-BUS methods are normal methods,
# and D-BUS signals are callback methods implemented by a subclass of
# MCAPInstance.
#
# The major difference is that there are no async command methods; 
# the async feedback comes via callbacks, while in D-BUS API only "passive"
# events provoked by remote side come via signals.

# So, the application must take into account that it will receive callbacks
# upon events it started by itself, otherwise there might be infinite loops.


class MCAPInstance:
	def __init__(self, adapter, listen):
		self.adapter = adapter
		self.listener = listen
		self.cpsm = 0
		self.dpsm = 0
		self.ccl = self.dcl = None
		if listen:
			self.do_listen()

	def do_listen(self):
		self.ccl = ControlChannelListener(adapter, self)
		self.cpsm = self.ccl.psm
		self.dcl = DataChannelListener(adapter, self)
		self.dpsm = self.ccl.psm

### Commands

	# feedback via callback
	def CreateMCL(self, addr):
		pass # FIXME5
		# return mcl
	
	def DeleteMCL(self, mcl):
		pass # FIXME

	def CloseMCL(self, mcl):
		pass # FIXME

	def CreateMDL(self, mcl, mdep_id, conf):
		''' followed by ConnectMDL/AbortMDL, which should be '''
		''' invoked when MDLRequested callback is triggered '''
		pass # FIXME
		# return mdl

	def AbortMDL(self, mdl):
		pass # FIXME

	def ConnectMDL(self, mdl):
		pass # FIXME

	# feedback via callback
	def DeleteMDL(self, mdl):
		pass # FIXME

	# feedback via callback
	def DeleteAll(self, mcl):
		pass # FIXME

	def CloseMDL(self, mdl):
		pass # FIXME

	# feedback via callback
	def ReconnectMDL(mdl):
		pass # FIXME

	def Send(self, mdl, data):
		pass # FIXME

### Callback methods that must be implemented by subclass

	def Recv(self, mdl, data):
		raise Exception("Not implemented")

	def MCLConnected(self, mcl, remote_addr):
		raise Exception("Not implemented")

	def MCLDisconnected(self, mcl):
		raise Exception("Not implemented")

	def MCLReconnected(self, mcl):
		raise Exception("Not implemented")

	def MCLUncached(self, mcl):
		raise Exception("Not implemented")
	
	def MDLRequested(self, mcl, mdep_id, conf):
		''' Followed by MDLAborted or MDLConnected '''
		raise Exception("Not implemented")

	def MDLAborted(self, mcl, mdl):
		raise Exception("Not implemented")

	def MDLConnected(self, mcl, mdl):
		raise Exception("Not implemented")

	def MDLDeleted(self, mdl):
		raise Exception("Not implemented")

	def MDLClosed(self, mdl):
		raise Exception("Not implemented")

	def MDLReconnected(self, mdl):
		raise Exception("Not implemented")

	def Watch(self, fd, activity_cb, error_cb):
		raise Exception("Not implemented")

	def Timeout(self, to, cb, *args):
		raise Exception("Not implemented")

	def Idle(self, cb, *args):
		raise Exception("Not implemented")

### Internal callbacks

	def watch_cc(self, listener, fd, activity_cb, error_cb):
		self.Watch(fd, activity_cb, error_cb)

	def new_cc(self, listener, sk, remote_addr):
		mcl = MCL(self, self.adapter, MCAP_MCL_ROLE_ACCEPTOR, remote_addr)
		mcl.accept(sk)
		# FIXME mcl handling
		# FIXME feedback

	def error_cc(self, listener):
		pass # FIXME

	def watch_dc(self, listener, fd, activity_cb, error_cb):
		self.Watch(fd, activity_cb, error_cb)

	def new_dc(self, listener, sk):
		pass # FIXME

	def error_dc(self, listener):
		pass # FIXME

# FIXME incorporate test1
# FIXME call the callbacks
# FIXME MCL = (instance, remote_addr)
# FIXME mcl.create_mdl() method
# FIXME Crossed connections protection (MCL/MDL)
# FIXME incoming MDLs
# FIXME watcher adater
# FIXME timeout adapter
# FIXME MDL observer read / error separate
# FIXME notify close MDL sk
# FIXME test existing MDL ID
# FIXME test2
# FIXME activity_mcl (for debug)
# FIXME CreateMCL == initator role
