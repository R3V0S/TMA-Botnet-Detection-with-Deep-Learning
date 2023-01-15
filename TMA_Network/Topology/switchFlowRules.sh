#!/bin/bash
echo -e '********** Flow rules added in the Switch 1 ********** \n'
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
echo -e '\n\n ********** Flow rules added in the Switch 2 ********** \n'
sudo ovs-ofctl -O OpenFlow13 dump-flows s2
echo -e '\n\n ********** Flow rules added in the Switch 3 ********** \n'
sudo ovs-ofctl -O OpenFlow13 dump-flows s3
