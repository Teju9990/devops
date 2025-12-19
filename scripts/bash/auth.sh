#!/bin/bash

echo "$SFDX_AUTH_URL" > auth.txt
sf org login sfdx-url -f auth.txt -a DevOpsPratice
