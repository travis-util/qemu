import pexpect, sys
child = pexpect.spawn('qemu-system-x86_64 -kernel finnix/boot/x86/linux64 -append 'initrd=boot/x86/initrd.xz console=ttyS0' -cdrom finnix-111.iso -nographic')
child.logfile = sys.stdout
# child.expect('Please press Enter to activate this console.')
# child.sendline('')
# child.expect('root@(none):/#')
# child.sendline('uname -a')
# child.sendline('dpkg')
# child.sendline('dpkg update')
# child.sendline('halt')
# child.expect(pexpect.EOF)
# print child.before;
