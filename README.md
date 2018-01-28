# qemu
Using Qemu emulator

One feature one may like is running in a console shell.

## Distributions running in serial console out of the box

Example of Qemu use with OpenWrt
* https://wiki.openwrt.org/doc/howto/qemu

Also to consider:
* https://opnsense.org/download/

References
* https://en.wikipedia.org/wiki/List_of_router_firmware_projects
* https://google.com/search?q=open+source+router
* https://www.infoworld.com/article/2615872/networking/networking-review-6-slick-open-source-routers.html

## How to use a live CD with the serial console?

### Kernel parameter
### Ncurse
### Live image adaptation

## Remastering a live CD with Chorizzo
### Editing Syslinux configuration
* [*SYSLINUX*](http://www.syslinux.org/wiki/index.php?title=SYSLINUX)

### Files needed
#### Packages
* https://tracker.debian.org/pkg/syslinux
* https://packages.debian.org/en/isolinux
#### isohdpfx.bin
* https://packages.debian.org/search?searchon=contents&keywords=isohdpfx.bin&mode=exactfilename
#### isolinux.bin
* Often already on existing CD image
* https://packages.debian.org/search?searchon=contents&keywords=isolinux.bin&mode=exactfilename

## Editing a live CD image with bsdtar
* Would it work?

## Building a live CD image from scratch
* [*Building an hybrid Debian Live ISO with xorriso*](https://www.opengeeks.me/2015/04/build-your-hybrid-debian-distro-with-xorriso/)

## Examples of live CD
### Debian Netinstall
* https://google.com/search?q=debian+netinstall+serial
* [*Howto install Debian Jessie (8.2) via the serial console using boot media (USB stick)*](http://pcengines.info/forums/?page=post&id=51C5DE97-2D0E-40E9-BFF7-7F7FE30E18FE)
* (fr) [*Installation Debian via le port série (serial console)*](https://www.debian-fr.xyz/viewtopic.php?f=7&t=720)

### Debian Live CD
* [debian live serial console @ Google](https://google.com/search?q=debian+live+serial+console)
* [*SerialConsoleHowto* (Ubuntu not live CD)](https://help.ubuntu.com/community/SerialConsoleHowto)

### GRML
* http://git.grml.org/?p=grml-live.git;a=blob_plain;f=templates/GRML/grml-cheatcodes.txt;hb=HEAD
