RocketTestStand
2007-07-03
rocket@watzlavick.com

This program is a control program for a small rocket test
stand.  It is written in LabVIEW 7.1 and has the following
dependencies:

Software
Windows 2000 or greater
LabVIEW 7.1 or greater
NI-DAQmx 7.2 or greater
NI-DAQ 7.2 Traditional or greater
NI-Sync 1.1.0 or greater

Hardware
NI PXI-1042 or equivalent PXI Chassis
NI PXI-6030E (Analog I/O)
NI PXI-6527 (Digital I/O)
NI PXI-6651 (Timing and synchronization)
NI PXI-8335 (MXI-3 bus extender)
NI PCI-8335 (MXI-3 bus extender)
NI SCXI-1000 or equivalent chassis
NI SCXI-1520 Signal conditioner
NI SCXI-1314 Terminal block for SCXI-1520
NI SCXI-1125 Signal conditioner
NI SCXI-1320 Terminal block for SCXI-1125
Datum/Bancomm bc635 PCI card (IRIG/GPS timing)

There is also a dependency on a custom hardware failsafe
and relay box.  Details on this can be found at:
http://www.watzlavick.com/robert/rocket


General Notes

The main program is called RocketTestStand<ver>.vi.  

It uses several loops to provide a responsive user
interface while acquiring and displaying the data in the 
background.  LabVIEW queues are used to pass around data and
commands between the loops.  The acquisition and control program 
runs reasonably well on a Pentium III-450 MHz machine with 
256 MB of RAM but the viewer program uses lots of RAM and works
better on a faster machine.

When I first wrote the program, the 6527 was not yet supported
in NI-DAQmx so I had to use NI-DAQ Traditional.  I believe
recent versions of NI-DAQmx support this card but I haven't had
the chance to convert the code over to the new API.

There are two versions of the post-test data viewer:
RocketData-replayer-regenTests-2007.vi
RocketData-replayerGraph-regenTest-2007.vi
The first one is much simpler and uses less RAM but it doesn't
provide individual cursor control.  The second one allows you
to drag cursors across the data and see values for all 
parameters at the same time.

