 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 10001 -u -b 231.533k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 10003 -u -b 3.408k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 10004 -u -b 133.670k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 10006 -u -b 228.491k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 10007 -u -b 270.508k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 10008 -u -b 222.693k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 10011 -u -b 222.791k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 10013 -u -b 273.961k -w 256k -t 50000 -i 0 &
sleep 0.4