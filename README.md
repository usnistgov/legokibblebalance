# NIST Open-Source Software Repository Template

Use of GitHub by NIST employees for government work is subject to
the [Rules of Behavior for GitHub][gh-rob]. This is the
recommended template for NIST employees, since it contains
required files with approved text. For details, please consult
the Office of Data & Informatics' [Quickstart Guide to GitHub at
NIST][gh-odi].

Please click on the green **Use this template** button above to
create a new repository under the [usnistgov][gh-nst]
organization for your own open-source work. Please do not "fork"
the repository directly, and do not create the templated
repository under your individual account.

The key files contained in this repository -- which will also
appear in templated copies -- are listed below, with some things
to know about each.

---

## README


PI: Stephan Schlamminger, NIST PML, Division 684, Fundamental Electric Measurements Group
Contact: Stephan.schlamminger@nist.gov





# Installation

### clone conda environment first:

conda create --name lego --clone base

conda activate lego

### NOIDAQmx

Download NIDAQmx
https://www.ni.com/en-us/support/downloads/drivers/download.ni-daq-mx.html#48087973.html

Install PyDaqmx 


conda install -c fallen pydaqmx

or

download from https://github.com/clade/PyDAQmx

run in Anaconda prompt:

python setup.py install


### install pyqtgraph

conda install -c anaconda pyqtgraph 


# Things to do

### Prior to Beta realease
* Coil slection should change automatically on weighing mode (i.e. you set the "measuremnt coil" in settings -  this way is when you measure BL it controls with the "Auxilliary coil")
* Calibrate postition window (this list inlude minor with major poinrs on this window):
	+ Fit values have way too many digits.
	+ Fit tool alows me a higher order fit a higher polynomial order than is posible to fit. Warning is never passed to user (unless python console is open.


* Import old config

*create installer / binary file




### Sometime
* Ui: deactivate UI Elements when functions are not needed.
* Check that opening cfgPID does not interfere with current Target
* cfg Pos %stable and variables to change eps for being in range, % progress %eps
* check every situation with volt mm conversion
* offset changed indicator in measure BL
* Better instructions (for example cfgSS)
* Textbox focus in cfg Pos
* Check naming (esp inputs), make it more readable
* unique file / gui / w name pos&position
* do graph time in: last x seconds
* mBL: right Error in % (Standard Derivation?)
* mBL: blcoil update when switching coil while window is open
* better stability on cfgPos and cfgSS: create Graph
* add Detection for disconnected LWB
* check why config is saved everytime ( maybe cuz devchanger )
* better weighmass, taking mean voltage/current of a timerperiod instead of 1 sample 
* Path Choice, diffrent configs for diffrent balances



### Not Important
* Window Icon
* Window UI Redesign (Max Size, draggable)
* Error catching @ create Plot window
* better use of 'basic Window'
* Comment every file & rewrite clunky parts
* establish 3 modes (static/velo/manual) instead of doPID & static/velo (better performance!)

### Additional Features
* Draggable Line for Offset in cfgSS
* Better mean sine Value for velo PID
* Saving variable history
* Saving window position
* saving last input for textboxes
* Toggle filter in PW, BTN in coilPos to display target
* Configure Data filtering
* Write PID as P*(1+I+D) instead of P + I + D
* Popup dialog when exiting window without saving pid variables
* error graph
* multithreading
* raw inputs and additional graphs in debugging window
* configurable amount of periods per bl fit
* customizeable stability requirements / waiting time in weighmass / cfgSS
* measure h window
* cfgPos: stepBack, updating graph with every point

##Julians Alpha Test:

### Major
* Coil slection should change automatically on weighing mode (i.e. you set the "measuremnt coil" in settings -  this way is when you measure BL it controls with the "Auxilliary coil")
* Calibrate postition window (this list inlude minor with major poinrs on this window):
	+ Fit values have way too many digits.
	+ Fit tool alows me a higher order fit a higher polynomial order than is posible to fit. Warning is never passed to user (unless python console is open.

### Minor

* If I click on a graph I accidentally move it and without knowing to click the A the autoscale is now messed up. This feature is best turned off. The right click menu can always be used to turn it on again.
* Velocities are in m/s which gives numbers in scietific e notation. For kids it is probably better to just go for mm/s so the numbers are less confusing.
* PID window. Change Epsilon to "Position error" for clarity. (Units might be nice on this panel in general)
* PID outputs update so fast that they are impossible to read. Also a fix number of digits outputs would make it a bit easier.
* Data aquisition settings: Can you add mesages on hover wich explain the options more clearly? I am not quite sure what I would be changing.
* Weigh mass gives far too many digits for the mass.
* Show PID outputs as a graph. This is useful for debugging.

### Tiny

* Watt balance shouldn't be one word on main window
* Zero postion is two words not one. (As is max position)
* A lot of the python style startLowerThenCamelCase seems to have worked it's way into the UI and looks strange.
* The instructions are a bit too! fond! of! exclamation! marks! I feel I am being shouted at a lot.
* No graph have x and y labels. Even when this is "obvious there should be some labels."