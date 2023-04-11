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

