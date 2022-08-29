# Server for Keysight Multichanell Multimeter

## Targets

This is the simple server for Keysight data acquisition unit.

## Getting Started

#### Software

To start the program you need Python version 3.10

## Operation

Programme starts a local server at PORT 9008 (you can change it's value in cls_SocketServer.py line 13).

To get setup identification: <br/>*query string "Idn".*<br/>

To scan first 10 multimeter channels (you can change this value in *cls_instrument.py* line 63)*
and get data:<br/>
*query string "Meas".*<br/>

To get a list of setup Errors: <br/>
*query string "Errors".*
