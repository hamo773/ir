 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 12001 -u -b 7226.910k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 12002 -u -b 186.259k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 12003 -u -b 106.386k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 12007 -u -b 8443.454k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 12008 -u -b 6951.009k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 12009 -u -b 8829.564k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 12010 -u -b 432.882k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 12013 -u -b 8551.235k -w 256k -t 50000 -i 0 &
sleep 0.4