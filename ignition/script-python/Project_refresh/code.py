def project_refresh(self):
	import system
	import system.project
	import time
	logger = system.util.getLogger("Logger")
	logger.info("Script Triggered")
	self.getSibling("Status").props.text= "Project Directory Scanning" 
	time.sleep(2)
	system.project.requestScan()
	logger.info("Script Worked Succesfully")
	time.sleep(2)
	self.getSibling("Status").props.text= "Project Directory Scan Complete" #comment