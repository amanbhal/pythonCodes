#this is a setup file for pygame_example13.py which helps to convert it into exe file
import cx_Freeze

executables = [cx_Freeze.Executable("pygame_example13.py")]

#define the setup which will include all the functions to setup
cx_Freeze.setup(
	name = "APPLE HUNT",	#name of application
	options = {"build_exe":{"packages":["[pygame]"],"include_files":["icon.jpg","snakehead.png","apple.jpg"]}},
	description = "APPLE HUNT snake game",
	executables = executables
	)