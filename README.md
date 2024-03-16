# HackRF-Minimodem-ImGui
Half-Duplex chatting using HackRF with GUI dearpygui.

![image](https://github.com/YD1RUH/HackRF-Minimodem-ImGui/blob/main/HackRF%20ImGUI%20minimodem.png)

## Requirement
- Linux Operating System (64-bit)
- python3 : `apt install python3`
- minimodem : `sudo apt install minimodem`
- xterm : `sudo apt install xterm`
- DearPyGUI : `pip3 install dearpygui`
- HackRF library : `sudo apt-get install hackrf libhackrf-dev`
- GNURadio3.8 : [Installation guide](https://wiki.gnuradio.org/index.php/LinuxInstall)
- SoapySDR : [Installation guide](https://github.com/pothosware/SoapySDR/wiki/BuildGuide#unix-instructions)
- SoapySDR HackRF : [Installation guide](https://github.com/pothosware/SoapyHackRF/wiki#building-soapy-hack-rf)

## How To Use
- clone the source using `git clone https://github.com/YD1RUH/HackRF-Minimodem-ImGui`
- go into the directory `cd HackRF-Minimodem-ImGui`
- make all file executable `chmod +x *`
- Open terminal, then run `./Minimodem-ImGUI`

## Next TODO
- adding sending file support (only txt file)
