# changer_empty_notify

I'm sure I'll come up with a better name, but until then, this is what it is.

This is a program to load onto an ESP32 which is tied into the "need service" light for american changers. It will scan the wifi networks it can see, connect to one if it's in a pre-determined list, and send a notification through ntfy.sh saying where the changer is empty.

