# Linux security

## What will we learn?
- Managing users
- Packages or software installed on the server
- Authenticating users
- How Linux manages files permissions
- Configure a firewall

## Concepts

#### Super user

#### Package source lists
`/etc/apt/sources.list`

List software of Linux

`sudo apt-get update`: check all softwares in the sources list and aware if changes

`sudo apt-get upgrade`: update all the changes

#### /etc/passwd
`vagrant:x:1000:1000:vagrant,,,:/home/vagrant:/bin/bash`
- vagrant: name of the user
- x: encrypted password in early days. But now, this field is often filled with an `x` means None
- 1000:1000: user id, group id

#### Creating new user
```shell
sudo adduser <studentname>
```

