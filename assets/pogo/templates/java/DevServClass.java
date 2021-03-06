//+======================================================================
// $Source$
//
// Project:   	Tango Device Server
//
// Description:	java source code for the TemplateDevServ class .
//              This class is a singleton class and implements everything
//              which exists only once for all the  TemplateDevServ object
//              It inherits from the DeviceClass class.
//
// $Author: pascal_verdier $
//
// $Revision: 9951 $
//
// $Log$
// Revision 3.1  2004/09/06 09:29:17  pascal_verdier
// *** empty log message ***
//
//
// copyleft :    European Synchrotron Radiation Facility
//               BP 220, Grenoble 38043
//               FRANCE
//
//-======================================================================
//
//  		This file is generated by POGO
//	(Program Obviously used to Generate tango Object)
//
//         (c) - Software Engineering Group - ESRF
//=============================================================================

package TemplateDevServ;

import java.util.*;
import org.omg.CORBA.*;
import fr.esrf.Tango.*;
import fr.esrf.TangoDs.*;
import fr.esrf.TangoApi.*;

public class TemplateDevServClass extends DeviceClass implements TangoConst
{
	/**
	 *	TemplateDevServClass class instance (it is a singleton).
	 */
	private static TemplateDevServClass	_instance = null;

	/**
	 *	Class properties array.
	 */
	private DbDatum[]	cl_prop = null;

	//--------- Start of properties data members ----------

	//--------- End of properties data members ----------


//===================================================================			
//
// method : 		instance()
// 
// description : 	static method to retrieve the TemplateDevServClass object 
//					once it has been initialised
//
//===================================================================			
	public static TemplateDevServClass instance()
	{
		if (_instance == null)
		{
			System.err.println("TemplateDevServClass is not initialised !!!");
			System.err.println("Exiting");
			System.exit(-1);
		}
		return _instance;
	}

//===================================================================			
//
// method : 		Init()
// 
// description : 	static method to create/retrieve the TemplateDevServClass
//					object. This method is the only one which enables a 
//					user to create the object
//
// in :			- class_name : The class name
//
//===================================================================			
	public static TemplateDevServClass init(String class_name) throws DevFailed
	{
		if (_instance == null)
		{
			_instance = new TemplateDevServClass(class_name);
		}
		return _instance;
	}
	
//===================================================================			
//
// method : 		TemplateDevServClass()
// 
// description : 	constructor for the TemplateDevServClass class
//
// argument : in : 	- name : The class name
//
//===================================================================			
	protected TemplateDevServClass(String name) throws DevFailed
	{
		super(name);

		Util.out2.println("Entering TemplateDevServClass constructor");
	
		Util.out2.println("Leaving TemplateDevServClass constructor");
	}
	
//===================================================================			
//
// method : 		command_factory()
// 
// description : 	Create the command object(s) and store them in the
//					command list
//===================================================================			
	public void command_factory()
	{
		Util.out2.println("Entering TemplateDevServClass command_factory");
		command_list.addElement(new   DevReadTimeCmd(new String("DevReadTime"),
						 	    		Tango_ARGIN_TYPE,  Tango_ARGOUT_TYPE));
	}


//===================================================================			
//
// method : 		device_factory()
// 
// description : 	Create the device object(s) and store them in the 
//					device list
//
// argument : in : 	String[] devlist : The device name list
//
//===================================================================			
	public void device_factory(String[] devlist) throws DevFailed
	{
	
		for (int i=0 ; i<devlist.length ; i++)
		{
			Util.out4.println("Device name : " + devlist[i]);
						
			// Create device and add it into the device list
			//----------------------------------------------
			device_list.addElement(new TemplateDevServ(this, devlist[i]));

			// Export device to the outside world
			//----------------------------------------------
			if (Util._UseDb == true)
				export_device(((DeviceImpl)(device_list.elementAt(i))));
			else
				export_device(((DeviceImpl)(device_list.elementAt(i))), devlist[i]);
		}
	}

