 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.4 -p 2004 -u -b 57.515k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 2005 -u -b 64.872k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 2006 -u -b 98.314k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 2007 -u -b 116.393k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 2010 -u -b 5.967k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 2011 -u -b 95.862k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 2012 -u -b 139.694k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 2014 -u -b 117.882k -w 256k -t 50000 -i 0 &
sleep 0.4