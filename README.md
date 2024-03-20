# Overture 65E

Reverse engineering / recovery notes around this old piece of networking hardware.
Mostly as I cant find much online.

The devices boot using redboot before booting into their main OS.
The front console port is cisco console cable compatible.
Default baud rate is 115200.
In redboot you can raise it to 460800 at the least with it working.

## Default login

The default login appears to be superuser/superuser.

## Saving settings

It _appears_ to save your settings you need to return to the earlier menu and copy running-settings to flash:startup-settings
