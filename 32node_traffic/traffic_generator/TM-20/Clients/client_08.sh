 #!/bin/bash 
echo Generating traffic...
        
iperf3 -c 10.0.0.1 -p 8001 -u -b 4020.242k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.2 -p 8002 -u -b 103.614k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.5 -p 8005 -u -b 2617.882k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.6 -p 8006 -u -b 3967.430k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.7 -p 8007 -u -b 4696.990k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.9 -p 8009 -u -b 4911.778k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.11 -p 8011 -u -b 3868.458k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.13 -p 8013 -u -b 4756.947k -w 256k -t 50000 -i 0 &
sleep 0.4
iperf3 -c 10.0.0.14 -p 8014 -u -b 4757.078k -w 256k -t 50000 -i 0 &
sleep 0.4