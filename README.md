# Intro
The CICFlowMeter is an open source tool that generates Biflows from pcap files, and extracts features from these flows.

CICFlowMeter is a network traffic flow generator available from here . It can be used to generate bidirectional flows, where the first packet determines the forward (source to destination) and backward (destination to source) directions, hence the statistical time-related features can be calculated separately in the forward and backward directions. Additional functionalities include, selecting features from the list of existing features, adding new features, and controlling the duration of flow timeout.

NOTE: 
1. TCP flows are usually terminated upon connection teardown (by FIN packet) while UDP flows are terminated by a flow timeout. The flow timeout value can be assigned arbitrarily by the individual scheme e.g., 600 seconds for both TCP and UDP.
2. In this project it's just to convert the .pcap files to csv using CICFlowmeter and then convert to .json files.

----------------------------------------

# Installation and executing:

Download https://github.com/ahlashkari/CICFlowMeter

Download CICFlowMeter: https://drive.google.com/drive/folders/1WiE_3PJjZOu9KHooYP3tgCdeLc18Rk8W

Extract CICFlowMeterV-4.0

Copy everything to the same folder

___Note: The only prerequisite is that "libpcap" library or WinPcap on windows systems, be pre-installed___


For Linux

> $ sudo apt-get install libpcap-dev
> Go to the jnetpcap folder inside CICFlowMeter/jnetpcap/linux/jnetpcap-1.4.r1425
> Copy libjnetpcap.so and libjnetpcap-pcap100.so in /usr/lib/ (as sudo).

For windows
> download [winpcap](<https://www.winpcap.org/install/default.htm>)
> Go to the jnetpcap folder inside CICFlowMeter/jnetpcap/win/jnetpcap-1.4.r1425
> Copy libjnetpcap.dll and libjnetpcap-pcap100.dll in /usr/lib/ (as sudo).

## executing
Go to the extracted directory,enter the 'bin' folder

### linux
Open a terminal and run this command
```
//For GUI:
sudo ./CICFlowMeter

//For Command line:
./cfm "inputFolder" "outputFolder"
```
### windows
Lanunch the Comand Prompt and run this command
```
//for GUI:
CICFlowMeter.bat

//for Commond line:
cfm.bat "inputFolder" "outputFolder"
```

## Get started
for offline
```
1.Select the folder that include your PCAP files
2.Select the folder that you would like to save you CSV files
3.Click OK button
```

for realtime
```
1 CLick Load button to find the list of network interfaces
2 Select the interface you would like to monitor
3 Click start button and wait for a while
4 Click stop button to stop the process and save the csv in same applcation folder/data/daily
```

--------------------------------------------------------------

source: https://github.com/ahlashkari/CICFlowMeter
