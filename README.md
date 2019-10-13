# cosmoshub-3-testnet
decentralized chain upgrade tester group
1. stop gaiad on your spare node(which is using sdk 0.34.7~9) synced to cosmoshub-2

2. export state on height 2,140,000(takes several minutes)

    (sudo) gaiad export --for-zero-height --height 2140000 > cosmoshub-2-export-at-2140000.json

3. check sha256sum of exported file

    jq -S -c -M '' cosmoshub-2-export-at-2140000.json | shasum -a 256
    (result : 633ba29af77848fa5bd6158d89c7c6557c4df32ab1efa9f19b06082a44df2320)

4. install gaia/rc2/v2.0.2 in new server

    # install essential and go-lang(1.13.1)
    sudo apt-get update
    sudo apt-get -y upgrade
    sudo apt-get install build-essential -y
    wget https://dl.google.com/go/go1.13.1.linux-amd64.tar.gz
    tar -xvf go1.13.1.linux-amd64.tar.gz
    
    # go path configuration
    echo 'PATH="$HOME/go/bin:$PATH"' >> ~/.profile
    source ~/.profile
    
    # install gaia
    git clone https://github.com/cosmos/gaia.git
    cd gaia
    git checkout rc2/v2.0.2
    go mod vendor
    make install

5. copy exported file(cosmoshub-2-export-at-2140000.json) to new server

6. migrate the exported file and check sha256sum

    gaiad migrate v0.36 cosmoshub-2-export-at-2140000.json \
    --chain-id cosmoshub-3-testnet --genesis-time=2019-10-14T00:00:00Z > cosmoshub-3-testnet.json
    
    jq -S -c -M '' cosmoshub-3-testnet.json | shasum -a 256
    # result : c0b2e0cdc09ec8414d242732bc25833e82c0bdaa5bdd555192d6eab3b82d778c

7. run valconspub replacement script

(this is to replace top rank validator valconspub to our keys so that we can validate behalf of them)

valconspub replacement plan : [https://docs.google.com/spreadsheets/d/1fIiusivqyPg9JgAbQ2i6yxZuJ6JFCKnY94Lzab2Tcms/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1fIiusivqyPg9JgAbQ2i6yxZuJ6JFCKnY94Lzab2Tcms/edit?usp=sharing)

    sed -i 's,cosmosvalconspub1zcjduepqg6y8magedjwr9p6s2c28zp28jdjtecxhn97ew6tnuzqklg63zgfspp9y3n,cosmosvalconspub1zcjduepq96apq95x43s9zunpm6f37upd6vp22f8evztc6vrv44sl2w3l0kysxpwlm4,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepquhlqdhjw4qp2c2t6qh5z7tfk52qc72623f0etc8f3n7hy8uuh25ql34fvu,cosmosvalconspub1zcjduepqaraq47kraszde9jk8xscev8dgmwh5vn9c7klcxuyrrxjw6rhzmrsxmuytp,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq6fpkt3qn9xd7u44478ypkhrvtx45uhfj3uhdny420hzgsssrvh3qnzwdpe,cosmosvalconspub1zcjduepqqn47r5flesk9064c7wj4x3ww84x7s66zdnm5awta95cd74ysa7sqeu20sk,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqp0j4vum7ryt6nl6zsgq9ar347afmq2c5z6jmzeavv2p2ns6m0dgs5zmg4z,cosmosvalconspub1zcjduepqxevl5mrjtvzzh680rsnppastw6a2znh8kpjlxal4gmt3m3j2rn9sljtwha,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq5kg8xls9l35ftulkm2rt70hexeeyr5cqqkcv4h7936z5uasvvazqla8eck,cosmosvalconspub1zcjduepqwavta5zhpv0jtl5ln7aw86y2dyjle9xenaqwhe0dq7ffmklmx3ls3ymghk,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqwrjpn0slu86e32zfu5xxg8l42uk40guuw6er44vw2yl6s7wc38est6l0ux,cosmosvalconspub1zcjduepqc29ujvmafvpccr40xhnl5n7w52qyeez8gwhdk4lhudjlc0nrzfaq2saljt,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq0dc9apn3pz2x2qyujcnl2heqq4aceput2uaucuvhrjts75q0rv5smjjn7v,cosmosvalconspub1zcjduepqfuqpaxmycpzs7gw5qgkwnpmv278ecuneentpnhl993hak22vktlqvuudx5,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqdgvppnyr5c9pulsrmzr9e9rp7qpgm9jwp5yu8g3aumekgjugxacq8a9p2c,cosmosvalconspub1zcjduepq7k9ncsfjz8zvtag9tpcxh68pxyknw2hp5q3fky7e80pyylltj3esckwpan,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqnltddase4lqjcfhup8ymg0qex3srakg54ppv06pstvwdjxkm6tmq08znvs,cosmosvalconspub1zcjduepqj525fwk8vsrd64lft6cj6xf00ckwe2h7gc0sky455c0mjxm0drzsmgmel7,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqmfxl36td7rcdzszzrk6c7kzp5l3jlw4lnxz8zms3py7qcsa9xlns7zxfd6,cosmosvalconspub1zcjduepqt5f2fjjj63h73lpdhxnm3jpewpzj2m6pzzwnl0n2xsspa7t7njjqrsttkh,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqfahazsjeru5wqulfuzklmkh272ggss2ru6fk00zq2fmlfzcq773sqlqe42,cosmosvalconspub1zcjduepqu2tueyjhhy754zxcjr5k64cvuu3csnyk0arsp5n56vym2dqx0d7sjmpm36,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqjc07nu2ya8tyzl8m385rnc382pkulwt2gh8yary73f3a96jak7pqsf63xf,cosmosvalconspub1zcjduepqgta6se8tczzxnvftkw85l8yeu3nkk3f94ywvwg6rmq588q6wml7q6s0au5,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqteacnywz7urnac46wtrcy34myyj82j250ny7866yffypdgavae5s0lf4a0,cosmosvalconspub1zcjduepqcssjskt4hvp8menz4vk4wwsugaxg2h0yjalytdc4d4m6lac8jegqffjzx6,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqjnnwe2jsywv0kfc97pz04zkm7tc9k2437cde2my3y5js9t7cw9mstfg3sa,cosmosvalconspub1zcjduepqnxh3dgn4tu570s7yf0d7rhckgmw45gklljkr6r3cm7zkvpjhtuwqz2myye,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqjg26g27dtvjqstyqktmp4jsn98473vfz0mek2eyklfp0yqapav5szdrvpd,cosmosvalconspub1zcjduepq6wtpv8stjhx2exsp4akvf240cpukhlyq5gepsmesqy7ckn9yadtq37djy3,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq7jsrkl9fgqk0wj3ahmfr8pgxj6vakj2wzn656s8pehh0zhv2w5as5gd80a,cosmosvalconspub1zcjduepqmxfl83u58jvtdd3dtls3720jjc6m5g2pgvekfmfevlgx8xqj405q05eauw,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqtj2urav4g9wex3hku588au0x4sucrc9lpky46zp5u8w4mvd584sqmcxxhs,cosmosvalconspub1zcjduepq0kf8suuyme92vgafnq6xnes8x0tztvm237yje8v7nghaytr7w6ks4tlwj5,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqvc5xdrpvduse3fc084s56n4a6dhzudyzjmywjx25fkgw2fhsj70searwgy,cosmosvalconspub1zcjduepqj5nvp9eufd2ualq2239q7qdq9s6qp6cx2dh5575tavl5cx3ge6zq7mpqzw,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqhm6gjjkwecqyfrgey96s5up7drnspnl4t3rdr79grklkg9ff6zaqnfl2dg,cosmosvalconspub1zcjduepq3a4ymdddr3ytdrsrnjjaaaxrftcf8ul9yclpscp8dnyk4ce90tdq4qene0,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq9xu9z6ky3nz3k544ar4zhupjehkxdlpmt2l90kekxkrvuu7hxfgslcdqwy,cosmosvalconspub1zcjduepq5qhc3ml6cg6tx5kjslxdk5kut8d3vpqld0grvfrhrpfga69yf89qv5phvm,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq8hu49qdl5594rzxmdsww3hleu8phxrajjfsseqjere9mjrrrv9tq35mll4,cosmosvalconspub1zcjduepqcfncjlkvjzfwmq27k6n542qx3wwh2a0sxd8pagapgy20ufjeznzqhwurn0,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqe93asg05nlnj30ej2pe3r8rkeryyuflhtfw3clqjphxn4j3u27msrr63nk,cosmosvalconspub1zcjduepqsv5gm20rq0p36cknhy3ur6tc4h36cwzst40t8vm9aev0cnmsl0lqfhzey5,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepq8y846wm58fmmuctxp7csqmaz3594xnykcean0lp722ntf6u5ycaqss4prd,cosmosvalconspub1zcjduepqwzsyfpc80mn3f4zc0juzk3rqcrtlu9y3fd6zzcrwu854dx9xtg9qvajt5r,g' cosmoshub-3-testnet.json
    sed -i 's,cosmosvalconspub1zcjduepqsszd2gzte82dzt0xpa3w0ky8lxhjs6zpd5ft8akmkscwujpftymsnt83qc,cosmosvalconspub1zcjduepql4l34spcvcg5ffhdd9tcaxauuy0k7mkr0fpf5f2kedj8zyrmkfyqapu8r0,g' cosmoshub-3-testnet.json
    

8. check sha256sum again with cosmoshub-3-testnet.json

    jq -S -c -M '' cosmoshub-3-testnet.json | shasum -a 256
    # result : 6e2352e07fa6ed9f72d48d77a90f38885e24888f7bdc3a9a53e1b81d544fd476

9. run validator pub_key(ed25519) replacement script

    sed -i 's%Roh99RlsnDKHUFYUcQVHk2S84NeZfZdpc+CBb6NREhM=%LroQFoasYFFyYd6TH3At0wKlJPlgl40wbK1h9To/fYk=%g' cosmoshub-3-testnet.json
    sed -i 's%5f4G3k6oAqwpegXoLy02ooGPK0qKX5Xg6Yz9ch+cuqg=%6PoK+sPsBNyWVjmhjLDtRt16MmXHrfwbhBjNJ2h3Fsc=%g' cosmoshub-3-testnet.json
    sed -i 's%0kNlxBMpm+5WtfHIG1xsWatOXTKPLtmSqn3EiEIDZeI=%BOvh0T/MLFfquPOlU0XOPU3oa0Js9065fS0w31SQ76A=%g' cosmoshub-3-testnet.json
    sed -i 's%C+VWc34ZF6n/QoIAXo4191OwKxQWpbFnrGKCqcNbe1E=%Nln6bHJbBCvo7xwmEPYLdrqhTuewZfN39UbXHcZKHMs=%g' cosmoshub-3-testnet.json
    sed -i 's%pZBzfgX8aJXz9tqGvz75NnJB0wAFsMrfxY6FTnYMZ0Q=%d1i+0FcLHyX+n5+64+iKaSX8lNmfQOvl7QeSndv7NH8=%g' cosmoshub-3-testnet.json
    sed -i 's%cOQZvh/h9ZioSeUMZB/1Vy1Xo5x2sjrVjlE/qHnYifM=%wovJM31LA4wOrzXn+k/OooBM5EdDrttX9+Nl/D5jEno=%g' cosmoshub-3-testnet.json
    sed -i 's%e3BehnEIlGUAnJYn9V8gBXuMh4tXO8xxlxyXD1APGyk=%TwAem2TARQ8h1AIs6YdsV4+ccnnM1hnf5Sxv2ylMsv4=%g' cosmoshub-3-testnet.json
    sed -i 's%ahgQzIOmCh5+A9iGXJRh8AKNlk4NCcOiPebzZEuIN3A=%9Ys8QTIRxMX1BVhwa+jhMS03KuGgIpsT2TvCQn/rlHM=%g' cosmoshub-3-testnet.json
    sed -i 's%n9bW9hmvwSwm/AnJtDwZNGA+2RSoQsfoMFsc2Rrb0vY=%lRVEusdkBt1X6V6xLRkvfizsqv5GHwsStKYfuRtvaMU=%g' cosmoshub-3-testnet.json
    sed -i 's%2k346W3w8NFAQh21j1hBp+Mvur+ZhHFuEQk8DEOlN+c=%XRKkylLUb+j8LbmnuMg5cEUlb0EQnT++ajQgHvl+nKQ=%g' cosmoshub-3-testnet.json
    sed -i 's%T2/RQlkfKOBz6eCt/drq8pCIQUPmk2e8QFJ39IsA96M=%4pfMkle5PUqI2JDpbVcM5yOITJZ/RwDSdNMJtTQGe30=%g' cosmoshub-3-testnet.json
    sed -i 's%lh/p8UTp1kF8+4noOeInUG3PuWpFzk6Mnopj0updt4I=%QvuoZOvAhGmxK7OPT5yZ5GdrRSWpHMcjQ9goc4NO3/w=%g' cosmoshub-3-testnet.json
    sed -i 's%XnuJkcL3Bz7iunLHgka7ISR1SVR8yePrREpIFqOs7mk=%xCEoWXW7An3mYqstVzocR0yFXeSXfkW3FW13r/cHllA=%g' cosmoshub-3-testnet.json
    sed -i 's%lObsqlAjmPsnBfBE+orb8vBbKrH2G5VskSUlAq/YcXc=%ma8WonVfKefDxEvb4d8WRt1aIt/8rD0OON+FZgZXXxw=%g' cosmoshub-3-testnet.json
    sed -i 's%khWkK81bJAgsgLL2GsoTKevosSJ+82VklvpC8gOh6yk=%05YWHguVzKyaAa9sxKqvwHlr/ICiMhhvMAE9i0yk61Y=%g' cosmoshub-3-testnet.json
    sed -i 's%9KA7fKlALPdKPb7SM4UGlpnbSU4U9U1A4c3u8V2KdTs=%2ZPzx5Q8mLa2LV/hHynyljW6IUFDM2TtOWfQY5gSq+g=%g' cosmoshub-3-testnet.json
    sed -i 's%XJXB9ZVBXZNG9uUOfvHmrDmB4L8NiV0INOHdXbG0PWA=%fZJ4c4TeSqYjqZg0aeYHM9Yls2qPiSydnpov0ix+dq0=%g' cosmoshub-3-testnet.json
    sed -i 's%ZihmjCxvIZinDz1hTU69024uNIKWyOkZVE2Q5Sbwl58=%lSbAlzxLVc78ClRKDwGgLDQA6wZTb0p6i+s/TBoozoQ=%g' cosmoshub-3-testnet.json
    sed -i 's%vvSJSs7OAESNGSF1CnA+aOcAz/VcRtH4qB2/ZBUp0Lo=%j2pNta0cSLaOA5yl3vTDSvCT8+UmPhhgJ2zJauMleto=%g' cosmoshub-3-testnet.json
    sed -i 's%KbhRasSMxRtStejqK/Ayzexm/DtavlfbNjWGznPXMlE=%oC+I7/rCNLNS0ofM21LcWdsWBB9r0DYkdxhSjuikSco=%g' cosmoshub-3-testnet.json
    sed -i 's%PflSgb+lC1GI22wc6N/54cNzD7KSYQyCWR5LuQxjYVY=%wmeJfsyQku2BXranSqgGi511dfAzTh6joUEU/iZZFMQ=%g' cosmoshub-3-testnet.json
    sed -i 's%yWPYIfSf5yi/MlBzEZx2yMhOJ/daXRx8Eg3NOso8V7c=%gyiNqeMDwx1i07kjwel4reOsOFBdXrOzZe5Y/E9w+/4=%g' cosmoshub-3-testnet.json
    sed -i 's%OQ9dO3Q6d75hZg+xAG+ijQtTTJbGezf8PlKmtOuUJjo=%cKBEhwd+5xTUWHy4K0RgwNf+FJFLdCFgbuHpVpimWgo=%g' cosmoshub-3-testnet.json
    sed -i 's%hATVIEvJ1NEt5g9i59iH+a8oaEFtErP227Qw7kgpWTc=%/X8awDhmEUSm7WlXjpu84R9vbsN6QpolVstkcRB7skg=%g' cosmoshub-3-testnet.json
    

10. check sha256sum again with cosmoshub-3-testnet.json

    jq -S -c -M '' cosmoshub-3-testnet.json | shasum -a 256
    # result : 2ff78eee2901838353a46d7fd0b3b8d8c97a1f7d71a14435db580aeb37fa2c18

11. run validator consensus byte address replacement script

    sed -i 's,679B89785973BE94D4FDF8B66F84A929932E91C5,AB3A8F5B706DC0B89218E7CADA39F8B364F7463E,g' cosmoshub-3-testnet.json
    sed -i 's,B1167D0437DB9DF0D533EE2ACDE48107139BDD2E,FB585EAF7A0CD947F0CE9535CA66B1F79FBB6B3C,g' cosmoshub-3-testnet.json
    sed -i 's,AC2D56057CD84765E6FBE318979093E8E44AA18F,D8BEBB7DCA042C9AEF5EDAADEE3830043B604C51,g' cosmoshub-3-testnet.json
    sed -i 's,2199EAE894CA391FA82F01C2C614BFEB103D056C,047E84C1032B214F2C2C5AD518D08D3C40A332B9,g' cosmoshub-3-testnet.json
    sed -i 's,C2356622B495725961B5B201A382DD57CD3305EC,577F36F642B9153DC5AB4DF48B0C2168C6B6E562,g' cosmoshub-3-testnet.json
    sed -i 's,B00A6323737F321EB0B8D59C6FD497A14B60938A,D4749A9783EFA1BC2D737AEAC40D76600A9E72E7,g' cosmoshub-3-testnet.json
    sed -i 's,099E2B09583331AFDE35E5FA96673D2CA7DEA316,443A1B7F053045EE2B7E56A7D4FB383D4C190CF8,g' cosmoshub-3-testnet.json
    sed -i 's,95E060D07713070FE9822F6C50BD76BCCBF9F17A,08F4337969E49BB4F6CD7C9E525485AC0F5F66B5,g' cosmoshub-3-testnet.json
    sed -i 's,D9F8A41B782AA6A66ADC81F953923C7DCE7B6001,9706B0AC61CD48CC832FF98D7FF1723A091291B8,g' cosmoshub-3-testnet.json
    sed -i 's,671460930CCDC9B06C5D055E4D550EB8DAF2291E,4F7FC88AC39C40EDC6BCBA0391D496A273D3D50E,g' cosmoshub-3-testnet.json
    sed -i 's,D540AB022088612AC74B287D076DBFBC4A377A2E,E71E72C5208AB64E28B9BDE5F3605B1F290E9336,g' cosmoshub-3-testnet.json
    sed -i 's,31920F9BC3A39B66876CC7D6D5E589E10393BF0E,CAC5C600255CC939DA6FDEBB5D55F32834BF9B06,g' cosmoshub-3-testnet.json
    sed -i 's,A6935D877B9776C45B96EEAE526959A3B9A5AB1A,A4AAE7F643E9E18A6C2F93611672BF8B07EAFFD8,g' cosmoshub-3-testnet.json
    sed -i 's,EE73A19751D58C5EC044C11E3FB7AE685A10D2C1,C18696991C95BF33BD5ED0C75F157A672D4C4E2A,g' cosmoshub-3-testnet.json
    sed -i 's,75DAB316F4CA1367F532AB71A80B7FA65AB69039,398E6A8B112400A9CFD82042D519194E6F922641,g' cosmoshub-3-testnet.json
    sed -i 's,BAC33F340F3497751F124868F049EC2E8930AC2F,734F358B16E66F23534984E6E31E940AEB0FF98E,g' cosmoshub-3-testnet.json
    sed -i 's,51205659A717DFFB96E054F8BD1108730E17AEA7,62872D6D2DB1AFF54DD37BC89510BAC5426D6AD3,g' cosmoshub-3-testnet.json
    sed -i 's,F4CAB410DE5567DB203BD56C694FB78D482479A1,632836EE4BEA79C03FDCF2AA237575762BF08904,g' cosmoshub-3-testnet.json
    sed -i 's,E800740C68C81B30345C3AE2BA638FA56FF67EEF,12AEBCE49698E925C4B0E8C22C196007D4968BDA,g' cosmoshub-3-testnet.json
    sed -i 's,DA6AAAA959C9EF88A3EB37B1F107CB2667EBBAAB,190989DE83FC629B501D464C778FB51EE6822005,g' cosmoshub-3-testnet.json
    sed -i 's,81965FE8A15FA8078C9202F32E4CFA72F85F2A22,8024ADF09351532D71B86096CBDA32C2BA4464D3,g' cosmoshub-3-testnet.json
    sed -i 's,000AA5ABF590A815EBCBDAE070AFF50BE571EB8B,381F828CD14D61176CC570BCA00D788968B77AB3,g' cosmoshub-3-testnet.json
    sed -i 's,57713BB7421C7FEB381B863FC87DED5E829AA961,827641F618E2C9D0C7A4CC6F4512998DAF954E52,g' cosmoshub-3-testnet.json
    sed -i 's,9EE94DBB86F72337192BF291B0E767FD2729F00A,4A59EFB3E65D1AC2A4FAE590E7625A23B54F7178,g' cosmoshub-3-testnet.json
    

12. check sha256sum again with cosmoshub-3-testnet.json

    jq -S -c -M '' cosmoshub-3-testnet.json | shasum -a 256
    # result : b89b7c0e6a173c7fa0c2998ac9d478992d7240f1075975a3b8552876c4cee019

13. copy cosmoshub-3-testnet.json as genesis.json in your config folder and run your validator(s) with submitted consensus keys

14. please share your peer info in telegram chat
