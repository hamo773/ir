 #!/bin/bash 
echo Initializing server listening...
        
iperf3 -s -p 2023 -1 &
sleep 0.3
iperf3 -s -p 3023 -1 &
sleep 0.3
iperf3 -s -p 8023 -1 &
sleep 0.3
iperf3 -s -p 13023 -1 &
sleep 0.3
iperf3 -s -p 14023 -1 &
sleep 0.3
iperf3 -s -p 15023 -1 &
sleep 0.3
iperf3 -s -p 19023 -1 &
sleep 0.3
iperf3 -s -p 20023 -1 &
sleep 0.3
iperf3 -s -p 22023 -1 &
sleep 0.3
iperf3 -s -p 24023 -1 &
sleep 0.3
iperf3 -s -p 25023 -1 &
sleep 0.3
iperf3 -s -p 26023 -1 &
sleep 0.3
iperf3 -s -p 27023 -1 &
sleep 0.3
iperf3 -s -p 28023 -1 &
sleep 0.3
iperf3 -s -p 30023 -1 &
sleep 0.3
iperf3 -s -p 31023 -1 &
sleep 0.3
iperf3 -s -p 32023 -1 &
sleep 0.3