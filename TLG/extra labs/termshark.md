# Termshark Guide

<video class="slide" controls="" controlslist="nodownload" data-autoplay="" poster="https://labs.alta3.com/courses/pyna/vid/pynaposter.png"><source type="video/mp4" src="https://labs.alta3.com/courses/pyna/vid/examining_network_capture_pcaps_files_with_termshark.mp4" data-lazy-loaded=""></video>

*Note: Since the recording of this video, installing termshark has become more streamlined. See the lab notes for the easiest installation method.*

### Lab Objective

**The objective of this lab is to learn to use termshark to examine** `*.pcap` **files.** The tool termshark allows for Wireshark-like analysis in a TTY screen.  The behavior of termshark is close to Wireshark, but the operation is different. This lab will guide you through a practical usage scenario so that you can effectively use this tool anytime you're attempting to troubleshoot at the command line.

### Procedure

1. Start in your home directory.

    `student@bchd:~$` `cd`

0. Now install termshark.

    `student@bchd:~$` `sudo apt install termshark -y`

0. When prompted if `non-superusers be able to capture packets` select `YES`.

0. Let's start termshark. This will start a termshark capture on the lo (loopback) interface.

    `student@bchd:~$` `sudo termshark -i lo`

    ```
    (The termshark UI will start when packets are detected...)
    Packets read from lo have been saved in /root/.cache/termshark/pcaps/lo--2021-09-01--12-09-07.pcap
    ```

0. Let termshark run for a few seconds.  You will notice the striped bar on the top right of your screen.

0. Let's stop the capture, using the ctrl-c command.

    `ctrl-c`

0. Termshark is now displaying the content it just captured. So let's see if we can adjust the display layout. Repeatedly press the `|` key. Notice the layout changing with each iteration.

    `first |` `2x1 display`  

    `second |` `1 over 2`

    `third |` `Back to the first layout`

0. You can also expand the size of a termshark pane. Let's make the second pane larger. Click on the second pane, and repeatedly press the `+` button.  Notice the pane extends downward.

0. Let's make the second pane smaller.  Click on the second pane, and repeatedly press the `-` button.  Notice the pane shrinks.

0. WAIT A MINUTE! Did we just click on a linux ncurses pane and it obeyed our mouse!?! That is cool, so how far does this go. Can you click on the first pane and repeat the above two steps. (FYI, the answer is yes, try it!)

0. To quit termshark simply press `ctrl-c`, then click the OK button on the pop up.

0. Let's download a PCAP file from the **Alta3 Research 5G** course, and use termshark to analyze it.

    `student@bchd:~$` `wget https://labs.alta3.com/courses/5g/pcaps/5greg.pcap`

0. Now that we have the file downloaded, let's look at it using termshark.

    `student@bchd:~$` `sudo termshark -r 5greg.pcap`  

0. Hmmm, that file looks wrong. We should be looking at HTTP2, but termshark appears to not understand the capture. Let's fix that. Type `ctrl-c` to quit termshark.

0. Now, lets start termshark with a more powerful command, telling termshark exactly how to decode HTTP2.

    `student@bchd:~$` `sudo termshark -r 5greg.pcap  -d=tcp.port==8000,http2`

0. OK, that looks better, now let's quit termshark and try to apply a display filter to the above command.

    `ctrl-c`

0. Let's try that again, this time with a `Y` display filter:

    `student@bchd:~$` `sudo termshark -r 5greg.pcap  -d=tcp.port==8000,http2 -Y="((((http2) && !(http2.type == 8)) && !(http2.type == 7)) && !(http2.type == 4)) && !(http2.type == 3)"`

0. OK, that is great!  We are ready to use termshark to perform analysis!  Quit termshark.

    `ctrl-c`  

0. **CHALLENGE 01** - Use the library `pyshark` [https://github.com/KimiNewt/pyshark](https://github.com/KimiNewt/pyshark) to make a capture (i.e. write a Python script that makes a network capture), then examine that capture with termshark.


<br><br><div align="center">

![Alta3 Logo](https://static.alta3.com/images/Alta3-logo_large.png)

</div>
