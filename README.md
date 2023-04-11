# w600-pico-costycnc

![w600-pico](https://github.com/costycnc/w600-firmware-pico-micropython-costycnc/blob/main/img/w600-pico.jpg)

I find micropython source code here https://github.com/robert-hh/Micropython-Editor and from same use here https://github.com/robert-hh/Shared-Stuff the firmware wm_w600_lfs.fls

![w600-pico](https://github.com/costycnc/w600-firmware-pico-micropython-costycnc/blob/main/img/w600.jpg)

Also can download micropython firmware from w600-pico from this page https://www.wemos.cc/en/latest/tutorials/w600/get_started_with_micropython_w600.html and here is direct link http://www.winnermicro.com/upload/1/editor/1568709203932.zip

You can buy w600-pico from official store https://www.wemos.cc/en/latest/w600/index.html or from my site https://www.costycnc.com/store/product/w600-pico-costycnc where can send with preinstalled main.py if you want , wth a little pay more!

For upload firmware need to install ch341 driver ( https://www.wemos.cc/en/latest/w600/index.html)

You can use this terminal for write(comunicate) with w600-pico https://bipes.net.br/aroca/web-serial-terminal/ or use this another terminal https://ttssh2.osdn.jp/ terminal for receive or send data to/from w600-pico or this another terminal https://www.settorezero.com/wordpress/software/zeroterm/ 

The terminal is not necessary ... only for see errors when run main.py file. I make this tutorial https://github.com/costycnc/w600-pico-micropython-official/tree/main/w600-pico%20upload%20file%20over%20ftp%20windows for first contact with w600-pico

Windows tool https://github.com/vshymanskyy/w600tool/releases/tag/0.1 

After install firmware you can see an access point wifi named "w600" 

Connect it (user="user" password="user" ) with ftp client  https://filezilla-project.org/  or use windows dos ftp command to put or read file to/from w600

The ip will be 192.168.43.1 same as risponse 
