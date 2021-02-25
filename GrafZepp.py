#!/usr/bin/env python

from scapy.all import *
from scapy.layers.inet import IP, ICMP

#welcome msg
def msg():
    print("\n ::::::::  :::::::::      :::     ::::::::::  ::::::::: :::::::::: :::::::::  :::::::::  :::::::::: :::        ::::::::::: ::::    ::: \n:+:    :+: :+:    :+:   :+: :+:   :+:              :+:  :+:        :+:    :+: :+:    :+: :+:        :+:            :+:     :+:+:   :+: \n+:+        +:+    +:+  +:+   +:+  +:+             +:+   +:+        +:+    +:+ +:+    +:+ +:+        +:+            +:+     :+:+:+  +:+ \n:#:        +#++:++#:  +#++:++#++: :#::+::#       +#+    +#++:++#   +#++:++#+  +#++:++#+  +#++:++#   +#+            +#+     +#+ +:+ +#+ \n+#+   +#+# +#+    +#+ +#+     +#+ +#+           +#+     +#+        +#+        +#+        +#+        +#+            +#+     +#+  +#+#+# \n#+#    #+# #+#    #+# #+#     #+# #+#          #+#      #+#        #+#        #+#        #+#        #+#            #+#     #+#   #+#+# \n ########  ###    ### ###     ### ###         ######### ########## ###        ###        ########## ########## ########### ###    #### ")#presentation and user input
    print("                                                                                                     made by a Very Horny Oni\n\n\n")
    print("Your orders, commander... \n\n")

#ip scan function
def ip_scan():
    ip = raw_input("[o]- Insert IP range: ")
    print("Sending Fi-167 planes (packets) to port: {} \n".format(ip))
    #send ARP packets to IP range
    rangeIP = ARP(pdst = ip)
    broadcast = Ether(dst = "ff:ff:ff:ff:ff:ff")
    final_packet = broadcast/rangeIP
    #access the response[0] - answered IP
    response = srp(final_packet, timeout = 2, verbose = False)[0]

    for n in response:
        #print("{} \n".format(n))
        print("[+] HOST {} FOUNDED :::::::::: MAC - {}".format(n[1].psrc, n[1].hwsrc))


#main funct to call ip scan funct
def main():
    msg()
    ip_scan()
    pass


if __name__ == "__main__":
    main()
