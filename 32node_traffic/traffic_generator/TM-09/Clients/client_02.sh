 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.4 -p 2004 -u -b 69.200k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 2005 -u -b 78.051k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 2006 -u -b 118.288k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 2007 -u -b 140.040k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 2010 -u -b 7.180k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 2011 -u -b 115.337k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 2012 -u -b 168.075k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 2014 -u -b 141.831k -w 256k -t 50000 -i 0 &
sleep 0.4