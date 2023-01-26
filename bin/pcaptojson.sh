#!/bin/bash

echo "INICIANDO O PROCESSO PARA PCAP PARA JSON"

sudo ./cfm pcap csv
python3 csvtojson.py

echo "REALIZADO COM SUCESSO"
