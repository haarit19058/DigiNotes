
# Managing Arch

To clean storage and efficiently manage packages on your Arch Linux system, follow these steps:

### 1. **Identify Large and Unnecessary Packages**

- Check installed packages sorted by size:
    
    ```bash
    pacman -Qi | awk '/^Name/{n=$3}/^Installed Size/{print $4 " " $5 " " n}' | sort -h
    ```
    
- Remove unwanted or unused packages:
    
    ```bash
    sudo pacman -Rns package_name
    ```
    
    Use `-Rns` to remove the package along with its dependencies that are not required by other packages.

### 2. **Clean the Package Cache**

- Arch Linux keeps a cache of downloaded packages. Over time, this can take up significant space. To clean it:
    - Remove cached packages not installed anymore:
        
        ```bash
        sudo pacman -Sc
        ```
        
    - To remove all cached packages:
        
        ```bash
        sudo pacman -Scc
        ```
        
    - Use `paccache` (from `pacman-contrib`) to retain the last three versions of each package:
        
        ```bash
        sudo paccache -r
        ```
        

### 3. **Remove Orphaned Packages**

- Orphaned packages are no longer required as dependencies. Remove them using:
    
    ```bash
    sudo pacman -Qtdq | sudo pacman -Rns -
    ```
    

### 4. **List and Remove Unused Configuration Files**

- Over time, configuration files from uninstalled packages may remain:
    
    ```bash
    sudo find /etc -name "*.pacsave" -o -name "*.pacnew"
    ```
    
    Review and remove files that are no longer needed.

### 5. **Identify Large Files and Directories**

- Find the largest directories:
    
    ```bash
    sudo du -h / --max-depth=1 | sort -h
    ```
    
- Use `ncdu` for an interactive view:
    
    ```bash
    sudo pacman -S ncdu
    ncdu /
    ```
    

### 6. **Enable System Maintenance**

- Use a package manager wrapper like `paru` or `yay` for better package management:
    
    ```bash
    sudo pacman -S paru
    ```
    
- Periodically check for redundant dependencies and outdated packages:
    
    ```bash
    paru -Qdt
    paru -Syu
    ```
    

### 7. **Automate Regular Maintenance**

- Add maintenance commands to a script or `cron` job:
    
    ```bash
    crontab -e
    ```
    
    Example:
    
    ```bash
    @weekly sudo paccache -r && sudo pacman -Qtdq | sudo pacman -Rns -
    ```
    

### 8. **Consider Using Tools for System Information**

- Install `bleachbit` for GUI-based cleanup:
    
    ```bash
    sudo pacman -S bleachbit
    ```
    
- Use `btop` or `htop` for real-time resource monitoring:
    
    ```bash
    sudo pacman -S btop htop
    ```
    

### 9. **Document Your Installed Packages**

- Save a list of explicitly installed packages:
    
    ```bash
    pacman -Qqe > package_list.txt
    ```
    
- Restore packages later:
    
    ```bash
    sudo pacman -S - < package_list.txt
    ```
    

If the system still feels messy, consider a **fresh installation** and follow best practices for maintaining a clean Arch Linux setup.


# The linux handbook or the arch wiki might be helpful to learn concepts that you dont know
# Notes

- Your UEFI will check all devices in your boot order, it will try to find a partition with the EFI label and reads and executes the one highest in the boot order. This partition will contain EFI binaries, they are little programs your UEFI can run, your bootloader will be one of these binaries.Your bootloader will now start running, it only has access to all the stuff in your boot partition for now. It will load the initramfs and kernel, once they are loaded the kernel will mount the root partition as defined in its kernel parameters, afterwards it will start executing binaries such as init and mount. This still leaves out a lot, Linux may for example be an EFI binary meaning you do not need a bootloader, if you use GRUB your initramfs and kernel may also be stored on the root partition since GRUB is capable of reading Ext4, tools such as system-gpt-auto can on their own infer mount points of the partitions without an fstab. There is a lot of "IF" surrounding this whole topic.




## Check for internet connection

- ip addr show
	- shows all types of connection
- For using wifi
		iwctl 
		iwd shell for connecting the wifi
		device list    to list all the wireless   interface available on the device



scan the local area and find all the wifi points
- station wlan0 scan
- station wlan0 get-networks  to see all the available networks around you
- staiton wlan0 connect "wifinametoconnect"   to connect to the wifi router
- exit from iwd prompt

ip addr --- check if the wifi is connected or not

ping -c 5 8.8.8.8    ping the google server to check internet connection



## Disk partition

### for non uefi

- fdisk -l   lists all the disks available
- fdisk /dev/sda  -- to move to the required harddisk
- o   --press enter   it will give new partition on the harddisk
- n   to cerate new partition
- it will give one partion
- t   -- allows to set the type of the partition
- 8e ---for lvm
- a   -- automatically select the partition one
- w  -- to finalise the changes
- fdisk -l to see the partiotion again
- pvcreate --dataalignment 1m /dev/sda1  to create a new physical partition on our partiion
- vgcreate volgroup0 /dev/sda1   //volume group is a container for disks

We will create two logical volumes
- lvcreate -L 30 GB volgroup0 -n lv_root   //cretes the logical partition
- lvcreate -l 100%FREE volgroup0 -n lv_home
- modprobe dm_mod   //to load a kernel module into memory
-  vgscan  //scan the system for volume group
- vgchange -ay  //activate the volume group


- Formatting 
- mkfs.ext4 /dev/volgroup0/lv_root //  farmat the partion now it can be mounted
- mount /dev/volgroup0/lv_root /mnt    //to mount the partition at mnt
- mkfs.ext4 /dev/volgroup0/lv_home
- mkdir /mnt/home
- mount /dev/volgroup0/lv_root /mnt/home
- mkdir /mnt/etc
- genstab -U -p /mnt >>/mnt/etc/fstab
- cat /mnt/etc/fstab


### With uefi

- fdisk -l
- fdisk /dev/sda    gives the shell
- p  //print all teh partitions on the disk
- g to create a new gpt partition table
- n   to create the one partition
- +fdisk
- 500M  to give 500 mb for the efi partition
- t  //enter type for the partition
- 1   // for efi partition
- n   // for creating new parttion
- enter twice to seelect the remaining part
- t
- 30 //enter fo rlinux lvm type
- # LVM video on hsi yt channel
- w // to write the changes
- mkfs.fat -F32 /dev/sda1 //for the fat file system  used in efi
- pvcreate --dataalignment 1m /dev/sda/2 //creates a physical volume for lvm disk /partition   to prepare the partiton to work with lvm+
- vgcreate volgroup0 /dev/sda2    //to create a volume group
- lvcreate -L 30GB volgroup0 -n lv_root  //to create the logical volume 
- lvcreate -l 100%FREE volgroup0 -n lv_home  
- modprobe dm_mod   //adds kernel module
- vgscan 
- vgchange -ay
- mkfs.ext4 /dev/volgroup0/lv_root
- mount /dev/volgroup0/lv_root /mnt
- mkfs.ext4 /dev/volgroup0/lv_home
- mkdir /mnt/home
- mount /dev.volgroup0/lv_home/mnt/home
- mkdir /mnt/etc
- genstab -U -p /mnt >> /mnt/etc/fstab
- cat /mnt/etc/fstab
- # what is this new command


### UEFI with encryption

- fdisk -l
- fdisk /dev/sda
- p  //see all existing partion
- g // work with brand new gpt partion layout
- n //new
- +500M  //for efi
- t  1 // to create the partition type
- n
- +500 M for another 500mb partition

- n 
- enter
- enter
- final partition
- t 30   for LVM
- p // see all the partition
-  w //save the changes
- fdisk -l
- mkfs.fat -F32 /dev/sda1
- mkfs.ext4 /dev/sda2
- Encrypting the third partition
- cryptsetup luksFormat /dev/sda3
- Passphrase : hrc1905
- cryptsetup open --type luks /dev/sda3 lvm
- type in the passphrase

- setting up the third part
- pvcreate --dataalignment 1m /dev/mapper/lvm
- vgcreate volgroup0 /dev/mapper/lvm
- lvcreate -L 30GB volgroup0 -n lv_root
- lvcreate -l 100%FREE volgroup0 -n lv_home
- modprobe dm_mod //kernel module load inthe memeory
- vgscan 
- vgchange -ay 
- mkfs.ext4 /dev/volgroup0/lv_root
- mount /dev/volgroup0/lv_root /mnt
- mkdir /mnt/boot/mount /dev/sda2 /mnt/boot

- mkfs.ext4 /dev/volgroup0/lv_home
- mkdir /mnt/home
- mount /dev/volgroup0/lv_home /mnt/home
- mkdir /mnt/etc
- # fstab is the file that the arch will red when it boots up
- genstab -U -p /mnt >> /mnt/etc/fstab
- cat /mnt/etc/fstab


## Installing arch

### installing the base packages 

- pacstrap -i /mnt base
- arch-chroot /mnt  // gives us acces to the arch linux installation
- pacman -S linux  linux-headers//default linux kernel standard one
- or
- pacman -S linux  linux-lts-headers

- pacman -S linux  linux-headers linux-lts-headers
- pacman -S nano   or vim
- pacman -S base-devel openssh  //base-devel is the basic development packages  and openssh gives remote installation accesss
- systemctl enable sshd  // in case if you want to use openssh

- to manipulate the network
- pacman -S networkmanager wpa_supplicant wireless_tools netctl
- paccman -S dialog //it gives us the ability to use something like wifi menu in cmd in case the gui doesn't work
- systemctl enable NetwokManager //to start the network manager to start automatically on boot
- pacman -S lvm2
- nano /etc/mkinitcpio.conf
- change the hooks line
- add encrypt lvm2 between block and file system // encrpt for thsoe who used disk encryption
- mkinitcpio -p linux 
- mkinitcpio -p linux-lts
- nano /etc/locale.gen
- find the locale country code and uncomment that
- locale-gen
- passwd hrc1905   // set the password for the root user
- useradd -m -g users -G wheel jay
- passwd jay //hrc1905
- pacman -S sudo 
- which sudo 
- EDITOR=nano visudo 
- uncomment wheel = all all all
- // our user will be able to use sudo commant to access root


## Installing Grub
### for non uefi system
- pacman -S grub dosfstools os-prober mtools
### for uefi
- pacman -S grub efibootmgr dosfstools os-prober mtools
### for uefi with encryption
- same as above


In the virtual Box continue the process from here
pacma
## movin on
- mkdir /boot /EFI
- mount /dev/sda1 /boot/EFI
- non uefi
	- grub install --target=i386-pc --recheck /dev/sda
	- no partition letter at the endefi
- efi
	- grub-install --target=x86_64-efi --bootloader-id =grub\_ uefi  --recheck 


- ls -l /boot /grub 
- if locale is not in this 
- mkdir /boot/grub/locale
- cp /usr/share/locale/en\\@quot/LC_MESSAGES/grub.mo /boot/grub/locale/en.mo


- for encrption
- basically telling grub to unlock the lock at boot
	- nano /etc/default/grub
	- uncomment grub_enable_cryptodisk=y
	- add new option in---> grub cmdline linux default=""cryptdevice=/dev/sda3:volgroup0:allow-discards"
-

- genrating the grub config file
- grub-mkconfig -o /boot/grub/grub.cfg


- exit 
- unmount -a
- reboot
# Now reboot is ready. 


# Post-install tweaks

- creating swap file and not the swap partition.
- su 
- password
- cd /root 
- dd if=/dev/zero of=/swapfile bs=1M count=2048 status=progress
- swap file created of 2gb

- chmod 600 /swapfile
- mkswap /swapfile //to make a true swap file
- cp /etc/fstab /etc/fstab.bak
- echo '/swapfile none swap sw 0 0' |tee -a /etc/fstab  // this will be the line in the fstab
- cat  /etc/fstab
- free -m 
- mount -a 
- free -m
- swapon -a
- free -m


- setting the timezone
- timedatectl list-timezones //to get all the timezones
- q //to quit out of that

- timedatectl set-timezone America/Detroit
- systemctl enable systemd-timesyncd //to activate the syncronization


- setting the hsot name of the system
- hostnamectl set-hostname myarch
- cat /etc/hostname
- nano /etc/hosts
- add a new line 
	- 127.0.0.1 localhost
	- 127.0.1.1 myarch


- Microcode for the cpu
- pacman -S intel-ucode

## Adding gui

### adding graphics driver
- pacman -S xorg-server //to manage we have the relevant packages
- pacman -S mesa // for intel gpu

- for virtual box
- pacman -S virtualbox-guest-utils xf86-video-vmware //for virtualbox
- systemctl enable vboxservice 



### gnome
- pacman -S gnome
- pacman -S gnome-tweaks

- enabling the display manager
- systemctl enable gdm //enabling the login screen
- now you should see a login screen on start

- set the language in gmone otherwise the apps wont startup
### plasma
- pacman -S plasma-meta kde-applications
- systemctl enable sddm

### xfce
- pacman -S xfce4 xfce4-goodies
- pacman -S lightdm lightdm-gtk-greeter
- systemctl enable lightdm
- reboot

### mate
- pacman -S mate mate-extra
- pacman -S lightdm lightdm-gtk-greeter
- systemctl enable lightdm
- reboot



# resising partitions after booting 
[seehere](https://www.rootusers.com/lvm-resize-how-to-decrease-an-lvm-partition/)

[thendothis](https://www.rootusers.com/lvm-resize-how-to-decrease-an-lvm-partition/)

# What after installing arch??
- Update your system
	- sudo pacman -Syu


s



