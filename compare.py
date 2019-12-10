### purpose of this script is to double check the consistency of accounts and delegations 
### in migrated genesis file for hub-3 compared to exported state file from hub-2

import json

export_file = "cosmoshub-2-export-at-2140000.json"
genesis_file = "genesis.json"

with open(export_file, "r") as f:
    export = json.loads(f.read())

with open(genesis_file, "r") as f:
    genesis = json.loads(f.read())

export_accounts = export["app_state"]["accounts"]
genesis_accounts = genesis["app_state"]["accounts"]

export_delegations = export["app_state"]["staking"]["delegations"]
genesis_delegations = genesis["app_state"]["staking"]["delegations"]

export_accounts = sorted(export_accounts, key = lambda i: i['address']) 
genesis_accounts = sorted(genesis_accounts, key = lambda i: i['address']) 

export_delegations = sorted(export_delegations, key = lambda i: i['validator_address']) 
genesis_delegations = sorted(genesis_delegations, key = lambda i: i['validator_address']) 

export_delegations = sorted(export_delegations, key = lambda i: i['delegator_address']) 
genesis_delegations = sorted(genesis_delegations, key = lambda i: i['delegator_address']) 

if export_delegations == genesis_delegations:
    print("delegations are identical!")
else:
    print("delegations mismatch! need further investigation!")
print("\n")

matched_accounts = []

print("---------- new accounts in genesis_accounts ----------")
new_accounts = []
for acc in genesis_accounts:
    match_flag = False
    for export_acc in export_accounts:
        if export_acc["address"] == acc["address"]: 
            match_flag = True
            matched_accounts.append({"export":export_acc, "genesis":acc})
            break
    if match_flag == False:
        print(acc)
        new_accounts.append(acc)
print("---------- total new accounts : " + str(len(new_accounts)) + "----------")
print("\n")

print("---------- removed accounts from export_accounts ----------")
removed_accounts = []
for acc in export_accounts:
    match_flag = False
    for genesis_acc in genesis_accounts:
        if genesis_acc["address"] == acc["address"]: 
            match_flag = True
            break
    if match_flag == False:
        print(acc)
        removed_accounts.append(acc)
print("---------- total removed accounts : " + str(len(removed_accounts)) + "----------")
print("\n")
     

print("number of accounts in export file : " + str(len(export_accounts)))
print("number of accounts in genesis file : " + str(len(genesis_accounts)))
print("number of matched accounts : " + str(len(matched_accounts)))
print("\n")

print("match checking for keys : address, coins, delegated_free, delegated_vesting, original_vesting")
mismatch_cnt = 0
match_cnt = 0
for acc in matched_accounts:
    match_flag = True
    mismatch_list = []
    check_keys = ["address","coins","delegated_free","delegated_vesting","original_vesting"]
    for key in check_keys:
        if acc["export"][key] == None: acc["export"][key] = []
        if acc["export"][key] != acc["genesis"][key]:
            match_flag = False
            mismatch_list.append(key)
            print(acc["export"])
            print(acc["genesis"])
    if match_flag == True:
        # print(str(acc["export"]["address"]) + " match!")
        match_cnt += 1
    else:
        print(str(acc["export"]["address"]) + str(mismatch_list) + " mismatch!")
        mismatch_cnt += 1

print("total match count : " + str(match_cnt))
print("total mismatch count : " + str(mismatch_cnt))


    
