 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.2 -p 6002 -u -b 118.288k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 6003 -u -b 67.563k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 6004 -u -b 2649.704k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 6007 -u -b 5362.195k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 6009 -u -b 5607.402k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 6012 -u -b 6435.672k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 6013 -u -b 5430.643k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 6014 -u -b 5430.792k -w 256k -t 50000 -i 0 &
sleep 0.4