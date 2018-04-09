# Intro to Linux

## Some popular Linux OS
- RedHat: Not free, for enterprises. And get support from RedHat company
- Debian: parent of Ubuntu. It's very stable and reliability. Server built on Debian can up and run for year without rebooting.
- LinuxMint: modified version of Ubuntu for desktop users with media support

## Important directories inside root directory
- `etc`: where configuration files live
- `var`: variable files. Files grows or are changed the size overtime
- `bin`: executable binaries are stored, that are accessible by all users
- `usr`: similar to bin, but not for boot-up or system program 
- `sbin`: directory holds all of the applications you may need as an administrator, but normal users typically won't use.

## Understading the `$PATH`
- As we know, `bin` directory stored binary system programs. Look inside `bin` we can see many familiar files like: ls, cp, rm, ... But why `ls` is still running without the fullpath `\bin\ls`.
- The reason is Linux has a variable to point which directories should look up when executing a program. It's called `$PATH`
