# HackRF-Minimodem-ImGui
Half-Duplex chatting using HackRF with GUI dearpygui.

![image](https://github.com/YD1RUH/HackRF-Minimodem-ImGui/blob/support-hamlib/screen.jpg)

## Requirement
- Linux Operating System 
- python3 : `sudo apt install python3`
- minimodem : `sudo apt install minimodem`
- xterm : `sudo apt install xterm`
- DearPyGUI : `pip3 install dearpygui`
- hamlib : [link github source](https://github.com/Hamlib/Hamlib) 

## How To Use
- clone the source using : \
  `git clone https://github.com/YD1RUH/HackRF-Minimodem-ImGui`
- go into the directory : \
  `cd HackRF-Minimodem-ImGui`
- Change branch to support-hamlib : \
  `git checkout support-hamlib`
- make all file executable : \
  `chmod +x *`
- Open terminal, then run : \
  `./MinimodemRig-ImGUI`

## Next TODO
- ~~adding sending file support (only txt file)~~
- ~~loopback audio while transmitting~~
