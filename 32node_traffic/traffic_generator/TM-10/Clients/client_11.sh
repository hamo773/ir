 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 11001 -u -b 4132.742k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.3 -p 11003 -u -b 60.837k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 11005 -u -b 2691.139k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 11006 -u -b 4078.453k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 11007 -u -b 4828.429k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 11008 -u -b 3974.967k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 11013 -u -b 4890.064k -w 256k -t 50000 -i 0 &
sleep 0.4