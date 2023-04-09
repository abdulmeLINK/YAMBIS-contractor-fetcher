## YAMBIS
aka. Yapı Müteahhitliği Bilişim Sistemi is a system that indexes contractors of Turkey. This repository is a to-Json parser for YAMBIS.

## Usage

`python .\save-contractors.py --sessionId ASPNET_SESSION_ID`

use --help to see options

```
usage: save-contractors.py [-h] [-l LENGTH] [-p PCODE] [-s STARTAT] --sessionId SESSIONID

YAMBIS contractor fetcher

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        Length of incoming data
  -p PCODE, --pcode PCODE
                        Province code for example 34 will get only contractors in İstanbul
  -s STARTAT, --startAt STARTAT
                        Fetching start index
  --sessionId SESSIONID
                        ASP.NET_SessionId
```
