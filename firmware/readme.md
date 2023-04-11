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

So i open original firmware w600.fls in notepad++ and in hex mode i search for main.py

I find many main.py ... but this for address 

