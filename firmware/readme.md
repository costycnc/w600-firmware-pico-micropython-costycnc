w600-pico

I modified the original firmware http://www.winnermicro.com/upload/1/editor/1568709203932.zip with notepad++ 

I insert these lines 

                        import easyw600
                        easyw600.createap(ssid="w600")
                        import w600
                        w600.run_ftpserver(port=21,username="user",password="user")
                        print("w600 ")

in wm_w600.fls

In notepad++ i installed hex plugin

![w600-pico](https://github.com/costycnc/w600-firmware-pico-micropython-costycnc/blob/main/img/plugin.jpg)

Hex plugin is a plugin that permit to modify any binary file... i used hex plugin many times to modify divers binary files without need to have a compiler ... but shure not need to touch the code ... only ascii characters same in this example.

So i open original firmware w600.fls in notepad++ and in hex mode i search for boot.py

I find many boot.py ... at this for address 

The original boot.py contain:


          # boot.py -- run on boot-up
          # can run arbitrary Python, but best to keep it minimal
          print("")
          print("    WinnerMicro W600")
          print("")
          

![w600-pico](https://github.com/costycnc/w600-firmware-pico-micropython-costycnc/blob/main/img/btpy.jpg?raw=true)

Seem that any file content begin after 0 ... so change any character from 0 to 0 in hex mode ... because need to keep exactly number of bytes ... if you edit directly in any text editor ... the file will be compromise ... so keep more attention if want modify another custom file ... is a primitive mode ... but in same cases is more efficient that have the compiler installed ...

So i put :

                        import easyw600
                        easyw600.createap(ssid="w600")
                        import w600
                        w600.run_ftpserver(port=21,username="user",password="user")
                        print("w600 ")

Need to make attention with new line character that is 0d and 0a


![w600-pico](https://github.com/costycnc/w600-firmware-pico-micropython-costycnc/blob/main/img/btpy1.jpg)

So... now the firmware have boot.py populated with few lines that create an access point and a ftp server ... son can transfer files over wifi (ap w600 connect without password) and ftp with https://filezilla-project.org/download.php

When make refirmware with this firmware the lines is ready ... not need insert manually any time when need to reinstall firmware.

In my case ... i need to reinstall firmware from time a time because when make some test module is blocking ... so need to reinstall firmware to unblocking!

Happy coding!



