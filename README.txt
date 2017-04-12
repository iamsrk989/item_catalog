
Instructions to run on Ubuntu linux.

1. Please unzip the package and cd into the catalog folder.
2. Then run 'python database_setup.py' command in the terminal window.
3. Then run 'python dummydata.py' command in the terminal window if you want to populate the database with test data.
4. Then run 'python project.py' command in the terminal window. This will start the server.
5. Open your browser and go to localhost:5000 to access the website.
6. You can view the Categories and Products already present in the database.
7. Please click "Click Here to Log in" link on the top right corner.
8. You can use google or facebook account to sign in.
9. Once Signed in you can add, edit and delete , Categories and Products to the Website.
10. To access JSON files for categories visit http://localhost:5000/category/JSON 
11. For products JSON visit http://localhost:5000/category/"Category id"/product/JSON -  Example "http://localhost:5000/category/2/product/JSON"


The instructions to install and run all the neccessary software is given below. These instructions are taken from "Installing the Virtual Machine" page of the Intro to relational Database class.

--------------------------------------------------------------------------------------------------------------->
Installing the Virtual Machine
We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

Use a terminal
You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from git-scm.com.

Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from virtualbox.org, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
_If Vagrant is successfully installed, you will be able to run `vagrant --version` in your terminal to see the version number._  
_The shell prompt in your terminal may differ. Here, the `$` sign is the shell prompt._
If Vagrant is successfully installed, you will be able to run vagrant --version in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.
Download the VM configuration
The virtual machine configuration is in this file: FSND-Virtual-Machine.zip - "https://d17h27t6h515a5.cloudfront.net/topher/2016/December/58488015_fsnd-virtual-machine/fsnd-virtual-machine.zip"

Download this file to your computer and unzip it. This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:
_Navigating to the FSND-Virtual-Machine directory and listing the files in it._  
_This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows._
Navigating to the FSND-Virtual-Machine directory and listing the files in it.
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
_Starting the Ubuntu Linux installation with `vagrant up`._  

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

If you reboot your computer, you will need to run vagrant up to restart the VM.
------------------------------------------------------------------------------------------------------------------->