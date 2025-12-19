#!/bin/bash

sf data query \
  --query "SELECT Id, Name FROM Account LIMIT 20" \
  --result-format csv > accounts.csv
