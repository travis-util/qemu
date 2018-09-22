# qemu
Using Qemu emulator

[![Build Status](https://travis-ci.org/travis-util/qemu.svg?branch=master)](https://travis-ci.org/travis-util/qemu)

One feature one may like is running in a console shell.

### Warning and error messages
* [Warning: requested NIC (anonymous, model unspecified) was not created (not supported by this machine?)](https://google.com/search?q=Warning%3A+requested+NIC+%28anonymous%2C+model+unspecified%29+was+not+created+%28not+supported+by+this+machine%3F%29)
  * Creating two NICs for OpenWrt on ARM

### TODO
* Update this project to look more like [qemu-demo/alpine-virt](https://gitlab.com/qemu-demo/alpine-virt)@gitlab
* Finnix
  * Put aria2c torrent download test in separate projet for trusty 14.04 LTS and xenial 16.04 LTS
    * https://askubuntu.com/questions/29872/torrent-client-for-the-command-line
    * https://gitlab.com/alpinelinux-packages-demo/aria2
  * Move Finnix in separated project https://gitlab.com/hub-docker-com-demo/finnix or https://gitlab.com/qemu-demo/finnix
  * Debug Finnix part maybe sending arrow special char from python pexpect.
* Try Alpine Linux, it is more Qemu friendly
  * [wiki.alpinelinux.org](https://wiki.alpinelinux.org/) > [*Install Alpine Linux in Qemu*](https://wiki.alpinelinux.org/wiki/Qemu)
  * Compare with other Alpine projects (see "Similar projects" below) and update what needs to.
  * Network configuration
* OpenWrt
  * Compare with other Alpine projects (see "Similar projects" below) and update what needs to.
  * Network configuration
  * OpenWrt prefers two network cards as it is intended for routers.
* [wiki.ubuntu.com](https://wiki.ubuntu.com/) > [Base (Ubuntu Base)](https://wiki.ubuntu.com/Base)

### Similar projects
* [hub-docker-com-demo/alpine](https://gitlab.com/hub-docker-com-demo/alpine)@gitlab
* [hub-docker-com-demo/finnix](https://gitlab.com/hub-docker-com-demo/finnix)@gitlab
* [hub-docker-com-demo/openwrt](https://gitlab.com/hub-docker-com-demo/openwrt)@gitlab
* [hub-docker-com-demo/qemu](https://gitlab.com/hub-docker-com-demo/qemu)@gitlab
* [qemu-demo/alpine-virt](https://gitlab.com/qemu-demo/alpine-virt)@gitlab

### Qemu
* [*QEMU*](https://wiki.archlinux.org/index.php/QEMU#Creating_a_hard_disk_image)
* [*Transfering root filesystem data into QEMU disk images*](http://nairobi-embedded.org/transfering_buildroot_fs_data_into_qemu_disk_images.html)
* [*Making a QEMU disk image bootable with GRUB*](http://nairobi-embedded.org/making_a_qemu_disk_image_bootable_with_grub.html)
* [*System emulation using QEMU*](https://gmplib.org/~tege/qemu.html)
* [*Build and boot a minimal Linux system with qemu*](http://www.kaizou.org/2016/09/boot-minimal-linux-qemu/)
#### Options
* [*QEMU/Options*](https://wiki.gentoo.org/wiki/QEMU/Options)
##### -drive (readonly)
##### egrep '^flags.*(vmx|svm)' /proc/cpuinfo
* true in sudo: false mode
* false in sudo: true mode
* -machine accel=kvm
* -cpu help
* -accel kvm
* 2018-06

## TODO
* Editing a live CD image with bsdtar (see below), using update or appends (create seems as complicated as burning from scratch). This needs to extract a configuration file, to simulate a null update.

## Distributions running in serial console out of the box

Example of Qemu use with OpenWrt
* [*OpenWrt in QEMU*](https://wiki.openwrt.org/doc/howto/qemu)
* https://en.wikipedia.org/wiki/Opkg

Also to consider:
* https://opnsense.org/download/

References
* https://en.wikipedia.org/wiki/List_of_router_firmware_projects
* https://google.com/search?q=open+source+router
* https://www.infoworld.com/article/2615872/networking/networking-review-6-slick-open-source-routers.html

## How to use a live CD with the serial console?
### Kernel parameters
* console=ttyS0

### ANSI escape code
* [ANSI escape code](https://en.wikipedia.org/wiki/ANSI_escape_code)

### Ncurse
qemu -display curses # but
* [*What are the ascii values of up down left right?*](https://stackoverflow.com/questions/2876275/what-are-the-ascii-values-of-up-down-left-right)
* https://www.google.ca/search?q=curses+cursor+keys
* [*NCURSES Programming HOWTO 11. Interfacing with the key board*](http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/keys.html)
* [*The Python Standard Library: 15.11. curses — Terminal handling for character-cell displays*](https://docs.python.org/2/library/curses.html)

### Live image adaptation

## Appending to a live CD with Chorizzo (but is it possible without actually burning to a physical disk?)
## Remastering a live CD with Chorizzo
* [*LiveCDCustomizationFromScratch*](https://help.ubuntu.com/community/LiveCDCustomizationFromScratch)
* [*What is the difference between GRUB and SYSLINUX?*](https://askubuntu.com/questions/651902/what-is-the-difference-between-grub-and-syslinux)
* https://en.wikipedia.org/wiki/El_Torito_(CD-ROM_standard)

### Editing Syslinux configuration
* https://en.wikipedia.org/wiki/SYSLINUX
* [*SYSLINUX*](http://www.syslinux.org/wiki/index.php?title=SYSLINUX)
* [*ISOLINUX*](http://www.syslinux.org/wiki/index.php?title=ISOLINUX)

### Kernel configuration
* http://man7.org/linux/man-pages/man7/bootparam.7.html
* [*Kernel parameters*](https://wiki.archlinux.org/index.php/kernel_parameters)
* https://www.kernel.org/doc/Documentation/admin-guide/kernel-parameters.txt
* [*How does a kernel mount the root partition?*](https://unix.stackexchange.com/questions/9944/how-does-a-kernel-mount-the-root-partition)
* [*How Is The Root File System Found?*](https://kernelnewbies.org/RootFileSystem)

#### Findiso
Findiso is a kernel option proposed by GRML
* [*Working on findiso for Debian Live*](https://www.supergrubdisk.org/2012/04/07/working-on-findiso-for-debian-live/)
* cf. grml-cheatcodes
* [*Debian Bug report logs - #656135 support findiso functionality*](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=656135)

### zRAM
* https://en.wikipedia.org/wiki/Zram
* https://doc.ubuntu-fr.org/zram
* https://wiki.debian.org/ZRam

### Filesystem
#### Root Squashfs
* [*SquashFS+UnionFS as root filesystem?*](https://unix.stackexchange.com/questions/209920/squashfsunionfs-as-root-filesystem)
* https://google.com/search?q=root+squashfs
* [*How to create a bootable system with a squashfs root*](https://askubuntu.com/questions/95392/how-to-create-a-bootable-system-with-a-squashfs-root)
* [*squashfs as root ?*](https://bbs.archlinux.org/viewtopic.php?id=191349)

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
### Appending (does not ork yet, without recreating)
* Would it work?
* tar --create --file new.iso foo1 @old.iso -C/tmp foo2
* tar --create --file new.iso @old.iso
* tar --update --file image.iso foo1
* tar --append --file image.iso foo1
* man bsdtar
* https://github.com/libarchive/libarchive/wiki/ManPageBsdtar1
* tar creates and manipulates streaming archive files. This implementation can extract from tar, pax, cpio, zip, jar, ar, xar, rpm, 7-zip, and ISO 9660 cdrom images and can create tar, pax, cpio, ar, zip, 7-zip, and shar archives.
* https://github.com/libarchive/libarchive/wiki/FormatISO9660
* bsdtar - libarchive 3.1.2, 3.3.2 (bsdtar --help) supports to write on ISO9660
* bsdtar --create --format iso9660 --file new.iso @finnix-111.iso # result is not bootable with 3.1.2
* bsdtar --to-stdout --file finnix-111.iso --extract isolinux.cfg
* --append and --update seems to transform the iso file into an empty POSIX tar archive before to make the requested operation.
* bsdtar -vvw --format iso9660 --file new2.iso --append isolinux.cfg
* bsdtar: Format iso9660 is incompatible with the archive new2.iso.
* bsdtar: Can't read archive f.iso: Unrecognized archive format: Invalid or incomplete multibyte or wide character

### Recreating
* bsdtar -vv --create --format iso9660 --file f3.iso @finnix-111.iso isolinux.cfg
* bsdtar --list -vv --file f3.iso
* Not bootable yet, but this seems to be possible with bsdtar

## Building a live CD image from scratch
* [*Building an hybrid Debian Live ISO with xorriso*](https://www.opengeeks.me/2015/04/build-your-hybrid-debian-distro-with-xorriso/)
* [*How to create a bootable system with a squashfs root*](https://askubuntu.com/questions/95392/how-to-create-a-bootable-system-with-a-squashfs-root)

## Examples of live CD
### Debian Netinstall
* https://google.com/search?q=debian+netinstall+serial
* [*Howto install Debian Jessie (8.2) via the serial console using boot media (USB stick)*](http://pcengines.info/forums/?page=post&id=51C5DE97-2D0E-40E9-BFF7-7F7FE30E18FE)
* (fr) [*Installation Debian via le port série (serial console)*](https://www.debian-fr.xyz/viewtopic.php?f=7&t=720)

### Debian Live CD
* [debian live serial console @ Google](https://google.com/search?q=debian+live+serial+console)
* [*SerialConsoleHowto* (Ubuntu not live CD)](https://help.ubuntu.com/community/SerialConsoleHowto)
* https://en.wikipedia.org/wiki/List_of_live_CDs#Debian-based

### GRML
* https://grml.org/
* http://git.grml.org/?p=grml-live.git;a=blob_plain;f=templates/GRML/grml-cheatcodes.txt;hb=HEAD

### Finnix
* https://finnix.org/
* https://en.wikipedia.org/wiki/Finnix
* [*Serial Console?*](https://lists.finnix.org/pipermail/finnix/2011-July/000151.html) (Works!)
* [*Remastering*](https://www.finnix.org/Remastering)
* [*Making Finnix Use Serial Console*](https://shoup.io/making-finnix-use-serial-console.html)
* Edit /isolinux.cfg
```
serial 0 115200
console 0
...
DEFAULT text
# DISPLAY boot/x86/boot.msg
# PROMPT 0
# TIMEOUT 600
# ONTIMEOUT hd0
...
# MENU BACKGROUND boot/x86/splash.png
...
# KERNEL boot/x86/vesamenu.c32
...
APPEND vga=off console=ttyS0,115200n8 initrd=boot/x86/initrd.xz nomodeset quiet --- console=ttyS0,115200n8
```
* $ xorriso -as mkisofs -r -J -joliet-long -l -cache-inodes -isohybrid-mbr /usr/lib/ISOLINUX/isohdpfx.bin -partition_offset 16 -A "Finnix111" -b isolinux.bin -c boot/x86/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o finnix-111-serial-install.iso finnix
* [*Finnix for VPS providers*](https://www.finnix.org/Finnix_for_VPS_providers)

### Super Grub2 Disk or using Grub
* https://www.supergrubdisk.org/super-grub2-disk/
* ```$ qemu-system-i386 -drive file=super_grub2_disk_hybrid_2.02s9.iso -drive file=finnix-111.iso```

* [*DebianLive MultibootISO*](https://wiki.debian.org/DebianLive/MultibootISO)
