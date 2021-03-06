import pexpect, sys
# child = pexpect.spawn('qemu-system-arm -M realview-eb-mpcore -kernel openwrt-realview-vmlinux-initramfs.elf -nographic') # Obsolete
child = pexpect.spawn('qemu-system-arm -net nic,vlan=0 -net nic,vlan=1 -net user,vlan=1 -nographic -M virt -m 64 -kernel openwrt-armvirt-32-zImage-initramfs')
child = pexpect.spawn('qemu-system-arm -nographic -M virt -m 64 -kernel openwrt-armvirt-32-zImage-initramfs')
child.logfile = sys.stdout
child.expect('Please press Enter to activate this console.')
child.sendline('')
# child.expect('root@(none):/#')
child.expect('root@')
child.sendline('uname -a')
child.expect('root@')
child.sendline('cat /proc/cmdline')
child.expect('root@')
child.sendline('opkg')
child.expect('root@')
child.sendline('opkg update') # Internet connection not working! should work now...
child.expect('root@')
child.sendline('halt')
child.expect('root@')
# child.expect(pexpect.EOF)
print child.before;
