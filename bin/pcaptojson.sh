#!/bin/bash

echo "STARTING THE PROCESS FOR PCAP TO JSON"

sudo ./cfm pcap csv
python3 csvtojson.py

echo "SUCCSSESFULLY DONE"
