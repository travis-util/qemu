# qemu
Using Qemu emulator

One feature one may like is running in a console shell.

### Qemu
* [*QEMU*](https://wiki.archlinux.org/index.php/QEMU#Creating_a_hard_disk_image)
* [*Transfering root filesystem data into QEMU disk images*](http://nairobi-embedded.org/transfering_buildroot_fs_data_into_qemu_disk_images.html)
* [*Making a QEMU disk image bootable with GRUB*](http://nairobi-embedded.org/making_a_qemu_disk_image_bootable_with_grub.html)
* [*System emulation using QEMU*](https://gmplib.org/~tege/qemu.html)
* [*Build and boot a minimal Linux system with qemu*](http://www.kaizou.org/2016/09/boot-minimal-linux-qemu/)
#### Options
* [*QEMU/Options*](https://wiki.gentoo.org/wiki/QEMU/Options)
##### -drive (readonly)

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
### Ncurse
qemu -display curses # but
* [*What are the ascii values of up down left right?*](https://stackoverflow.com/questions/2876275/what-are-the-ascii-values-of-up-down-left-right)
* https://www.google.ca/search?q=curses+cursor+keys
* [*NCURSES Programming HOWTO 11. Interfacing with the key board*](http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/keys.html)
* [*The Python Standard Library: 15.11. curses — Terminal handling for character-cell displays*](https://docs.python.org/2/library/curses.html)

### Live image adaptation

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
* Would it work?
* tar --create --file new.iso foo1 @old.iso -C/tmp foo2
* tar --create --file new.iso @old.iso
* tar --update --file image.iso foo1
* tar --append --file image.iso foo1
* man bsdtar
* https://github.com/libarchive/libarchive/wiki/ManPageBsdtar1
* tar creates and manipulates streaming archive files. This implementation can extract from tar, pax, cpio, zip, jar, ar, xar, rpm, 7-zip, and ISO 9660 cdrom images and can create tar, pax, cpio, ar, zip, 7-zip, and shar archives.
* https://github.com/libarchive/libarchive/wiki/FormatISO9660
* bsdtar 3.1.2 - libarchive 3.1.2 (bsdtar --help) supports to write on ISO9660
* bsdtar --create --format iso9660 --file new.iso @finnix-111.iso # result is not bootable with 3.1.2

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
