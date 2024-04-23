 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.4 -p 2004 -u -b 63.470k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 2005 -u -b 71.589k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 2006 -u -b 108.494k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 2007 -u -b 128.444k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 2010 -u -b 6.585k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 2011 -u -b 105.787k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 2012 -u -b 154.158k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 2014 -u -b 130.088k -w 256k -t 50000 -i 0 &
sleep 0.4