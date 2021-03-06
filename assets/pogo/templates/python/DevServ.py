#	"$Name:  $";
#	"$Header: /cvsroot/tango-cs/tango/tools/pogo/templates/python/DevServ.py,v 1.6 2007/01/08 07:03:01 pascal_verdier Exp $";
#=============================================================================
#
# file :        TemplateDevServ.py
#
# description : Python source for the TemplateDevServ and its commands. 
#                The class is derived from Device. It represents the
#                CORBA servant object which will be accessed from the
#                network. All commands which can be executed on the
#                TemplateDevServ are implemented in this file.
#
# project :     TANGO Device Server
#
# $Author: taurel $
#
# $Revision: 16150 $
#
# $Log: DevServ.py,v $
# Revision 1.6  2007/01/08 07:03:01  pascal_verdier
# *** empty log message ***
#
# Revision 1.5  2006/11/24 14:29:22  pascal_verdier
# Implements first Python gurus remarks.
#
# Revision 1.4  2006/11/09 14:05:30  pascal_verdier
# Change overwriting property.
#
# Revision 1.3  2006/11/07 14:57:45  pascal_verdier
# Header tags added.
#
# Revision 1.2  2006/11/06 15:41:33  pascal_verdier
# Put property methods in Util class.
#
# Revision 1.1  2006/11/02 11:43:30  pascal_verdier
# Python code generation added.
#
#
# copyleft :    European Synchrotron Radiation Facility
#               BP 220, Grenoble 38043
#               FRANCE
#
#=============================================================================
#  		This file is generated by POGO
#	(Program Obviously used to Generate tango Object)
#
#         (c) - Software Engineering Group - ESRF
#=============================================================================
#


import PyTango
import sys



class TemplateDevServ(PyTango.Device_4Impl):

#--------- Add you global variables here --------------------------

#------------------------------------------------------------------
#	Device constructor
#------------------------------------------------------------------
	def __init__(self,cl, name):
		PyTango.Device_4Impl.__init__(self,cl,name)
		TemplateDevServ.init_device(self)

#------------------------------------------------------------------
#	Device destructor
#------------------------------------------------------------------
	def delete_device(self):
		print "[Device delete_device method] for device",self.get_name()


#------------------------------------------------------------------
#	Device initialization
#------------------------------------------------------------------
	def init_device(self):
		print "In ", self.get_name(), "::init_device()"
		self.set_state(PyTango.DevState.ON)
		self.get_device_properties(self.get_device_class())

#------------------------------------------------------------------
#	Always excuted hook method
#------------------------------------------------------------------
	def always_executed_hook(self):
		print "In ", self.get_name(), "::always_excuted_hook()"

#==================================================================
#
#	TemplateDevServ read/write attribute methods
#
#==================================================================
#------------------------------------------------------------------
#	Read Attribute Hardware
#------------------------------------------------------------------
	def read_attr_hardware(self,data):
		print "In ", self.get_name(), "::read_attr_hardware()"


#==================================================================
#
#	TemplateDevServ command methods
#
#==================================================================

#==================================================================
#
#	TemplateDevServClass class definition
#
#==================================================================
class TemplateDevServClass(PyTango.DeviceClass):

	#	Class Properties
	class_property_list = {
		}


	#	Device Properties
	device_property_list = {
		}


	#	Command definitions
	cmd_list = {
		}


	#	Attribute definitions
	attr_list = {
		}


#------------------------------------------------------------------
#	TemplateDevServClass Constructor
#------------------------------------------------------------------
	def __init__(self, name):
		PyTango.DeviceClass.__init__(self, name)
		self.set_type(name);
		print "In TemplateDevServClass  constructor"

#==================================================================
#
#	TemplateDevServ class main method
#
#==================================================================
if __name__ == '__main__':
	try:
		py = PyTango.Util(sys.argv)
		py.add_TgClass(TemplateDevServClass,TemplateDevServ,'TemplateDevServ')

		U = PyTango.Util.instance()
		U.server_init()
		U.server_run()

	except PyTango.DevFailed,e:
		print '-------> Received a DevFailed exception:',e
	except Exception,e:
		print '-------> An unforeseen exception occured....',e
