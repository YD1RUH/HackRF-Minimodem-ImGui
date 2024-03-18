# HackRF-Minimodem-ImGui
Half-Duplex chatting using HackRF with GUI dearpygui.

![image](https://github.com/YD1RUH/HackRF-Minimodem-ImGui/blob/main/HackRF%20ImGUI%20minimodem.png)

## Requirement
- Linux Operating System 
- python3 : `sudo apt install python3`
- minimodem : `sudo apt install minimodem`
- xterm : `sudo apt install xterm`
- DearPyGUI : `pip3 install dearpygui`
- HackRF library : `sudo apt-get install hackrf libhackrf-dev`
- GNURadio3.10 : [Installation guide](https://wiki.gnuradio.org/index.php/LinuxInstall)
- SoapySDR : [Installation guide](https://github.com/pothosware/SoapySDR/wiki/BuildGuide#get-the-source-code)
- SoapySDR HackRF : [Installation guide](https://github.com/pothosware/SoapyHackRF/wiki#building-soapy-hack-rf)

## How To Use
- clone the source using `git clone https://github.com/YD1RUH/HackRF-Minimodem-ImGui`
- go into the directory `cd HackRF-Minimodem-ImGui`
- make all file executable `chmod +x *`
- Open terminal, then run `./Minimodem-ImGUI`

## Next TODO
- adding sending file support (only txt file)
