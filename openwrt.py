import pexpect, sys
child = pexpect.spawn('qemu-system-arm -M realview-eb-mpcore -kernel openwrt-realview-vmlinux-initramfs.elf -nographic')
child.logfile = sys.stdout
child.expect('Please press Enter to activate this console.')
child.sendline('')
# child.expect('root@(none):/#')
child.expect('root')
child.sendline('uname -a')
child.expect('root')
child.sendline('opkg')
child.expect('root')
child.sendline('opkg update')
# child.sendline('halt')
child.expect(pexpect.EOF)
print child.before;
