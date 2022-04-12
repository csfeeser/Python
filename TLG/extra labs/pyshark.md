# Python for Network Captures and Wireshark

<video class="slide" controls="" controlslist="nodownload" data-autoplay="" poster="https://labs.alta3.com/courses/pyna/vid/pynaposter.png"><source type="video/mp4" src="https://labs.alta3.com/courses/pyna/vid/python_for_network_captures_and_wireshark.mp4" data-lazy-loaded=""></video>

### Lab Objective

The objective of this lab is to explore using Python to create, and parse, `*.pcap` files.

Wireshark is the de facto tool when needing to create network captures. Wireshark is GUI rich, which won't work at the CLI, and is a poor choice for scripting. Instead, we'll use tshark. The application `tshark` is a GUI-less version of Wireshark.

Start by reading about `pyshark` here: https://github.com/KimiNewt/pyshark

### Procedure

1. First, install `pyshark` with `pip` using `sudo`.

    `student@bchd:~/mycode` `sudo python3 -m pip install pyshark`

0. The `pyshark` leverages `tshark`. So we also need to ensure `tshark` is installed.

    `student@bchd:~/mycode` `sudo apt install tshark`

0. Start the python3 interpreter. Unfortunately, we need to run with `sudo` as `tshark` is not setup for capturing with non-sudo users.

    `student@bchd:~/mycode` `sudo python3`

0. Issue the following command to import `pyshark`

    `student@bchd:~/mycode` `>>>` `import pyshark`

0. Setup a capture object that includes capturing on interface `ens3` and direct packets to be saved to `pythoncapture.pcap`

    `>>>` `capture = pyshark.LiveCapture(interface='ens3', output_file='pythoncapture.pcap')`

0. Begin a capture for 50 seconds.

    `>>>` `capture.sniff(timeout=50)`

0. The `capture` object will display how many packets were captured.

    `>>>` `capture`

0. Determine what the second packet captured was.

    `>>>` `capture[1]`

0. Retrieve a list of interfaces used to create the capture

    `>>>` `capture.interfaces`

0. Exit the Python interpreter

    `>>>` `exit()`

0. Ensure the capture file was created.

    `student@bchd:~/mycode` `ls *.pcap`

0. Great, now create a python script to create a capture.

    `student@bchd:~/mycode` `vim readingshark.py`

0. Our goal is to create a Python script that can open an interact with the `*.pcap` we just downloaded.

    ```python
    #!/usr/bin/python3
    """
    Open a pcap file.
    """

    import pyshark

    def main():

        # open the pcap file pythoncapture.pcap
        cap = pyshark.FileCapture("pythoncapture.pcap")

        # what protocol should we scan the pcap for?
        scanfor = input("What protocol should we scan the PCAP for (DNS, ICMP, TCP, etc.)? ")
        # loop across the entire capture (packet by packet)
        packetmatch = 0
        for packet in cap:
            # print each packet
            # print(packet)
            # print the PROTOCOL associated with each packet
            if packet.highest_layer == scanfor.upper():
                print(packet)
                packetmatch += 1 # packet matches on protocol

        if packetmatch > 0:
            print(f"A total of {packetmatch} packets match the {scanfor} protocol")
        else:
            print(f"Sorry, we were not able to find any packets matching the {scanfor} protocol")


    if __name__ == "__main__":
        main()        
    ```

0. Save and exit with `:wq`

0. Run your script.

    `student@bchd:~/mycode` `python3 readingshark.py`

0. **CODE CHALLENGE 01 -** Allow the user to search for more than a single protocol.

0. **CODE CHALLENGE 02 -** Allow the user the option to save out a new `*.pcap` containing the matches on their search results.

0. That's it for this lab. Many other libraries are available that allow Python to interact with network packets. If you find yourself finishing early, do some Googling on other libraries that are available. Share with the class any you might find.
