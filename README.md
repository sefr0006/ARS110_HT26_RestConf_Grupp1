# todo:

## r1:
* no shut på serial

* ~~kolla om ip summary-address eigrp 1 192.168.48.0 255.255.254.0 går att fixa annars försök fixa genom cli om det är ok~~ 

yang cisco ios xe som 16.12.08 använder

https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16121/Cisco-IOS-XE-interfaces.yang

ip summary address är deprecated och hänvisar till:

https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16121/Cisco-IOS-XE-eigrp.yang

inga seriella

summering endast går att göra i named mode?? ej classic?

* ~~kolla om det är ok att rätta ovanstående med en show run~~ | i ip summary-address 


## r2:
* ~~no shut på serial~~ ok

## r3:
* ~~testa allting~~ ok

* [![tls connect error](tls_connect_error_r3.png)] !! :( jätteledsen

## skilla.py

* ~~ta bort allt onödigt (oanvända interfaces behövs inte vara med)~~
ok?

## rätta.py

* använd allt onödigt (oanvända interfaces ska vara oanvända)
