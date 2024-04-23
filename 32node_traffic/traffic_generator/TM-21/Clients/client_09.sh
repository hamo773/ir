 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 9001 -u -b 4939.958k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.4 -p 9004 -u -b 2851.974k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 9005 -u -b 3216.778k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 9006 -u -b 4875.064k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.8 -p 9008 -u -b 4751.365k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.10 -p 9010 -u -b 295.897k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.12 -p 9012 -u -b 6926.950k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 9013 -u -b 5845.201k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 9014 -u -b 5845.361k -w 256k -t 50000 -i 0 &
sleep 0.4