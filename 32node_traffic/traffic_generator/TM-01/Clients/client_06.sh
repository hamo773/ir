 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.2 -p 6002 -u -b 98.700k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 6003 -u -b 56.375k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 6004 -u -b 2210.922k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 6007 -u -b 4474.234k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 6009 -u -b 4678.835k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 6012 -u -b 5369.946k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 6013 -u -b 4531.347k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 6014 -u -b 4531.471k -w 256k -t 50000 -i 0 &
sleep 0.4