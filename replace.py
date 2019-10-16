import subprocess
import json
import time

# environment variables
read_file = "replacement_plan.txt" # containing list of valconspub_old, valconspub_new
original_state_file = "cosmoshub-2-export-at-2140000.json"
new_state_file = "genesis.json"
binary_path = "./" # path where gaiad, gaiacli, gaiadebug is located
version_tobe = "v0.36"
chain_id_tobe = "cosmoshub-3.1-testnet"
genesis_time_tobe = "2019-10-14T00:00:00Z"


# print shasum 
print("original state file shasum")
cmd = "jq -S -c -M '' " + original_state_file + " | shasum -a 256"
print(subprocess.check_output(cmd,shell=True).decode("utf8"))
time.sleep(1)


# migration
print("migrate...")
cmd = binary_path + "gaiad migrate " + version_tobe + " " + original_state_file + " --chain-id " + chain_id_tobe + " --genesis-time " + genesis_time_tobe + " > " + new_state_file
print(subprocess.call(cmd,shell=True))
print("migration complete!\n")
time.sleep(1)


# print shasum 
print("new state file shasum before replacement")
cmd = "jq -S -c -M '' " + new_state_file + " | shasum -a 256"
print(subprocess.check_output(cmd,shell=True).decode("utf8"))
time.sleep(1)


# run replacement script
print("running replacement script...")
lines = open(read_file,"r").read().split("\n")
result_string = []

for line in lines:

    valconspub_old = line.split(",")[0]
    valconspub_new = line.split(",")[1]

    cmd = binary_path + "gaiadebug pubkey " + valconspub_old
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    address_old = result.split("\n")[0].split(": ")[1]

    cmd = binary_path + "gaiakeyutil " + str(address_old)
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    valcons_old = result.split("\n")[7].split("- ")[1]

    cmd = binary_path + "gaiacli keys parse " + valconspub_old
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    bytes_old = result.split("\n")[1].split(" ")[1][10:]

    cmd = binary_path + "gaiadebug pubkey " + str(bytes_old)
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    pubkey_old = json.loads(result.split("\n")[2].split(": ")[1])["value"]

    cmd = binary_path + "gaiadebug pubkey " + str(pubkey_old)
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    address_old = result.split("\n")[0].split(": ")[1]
    

    
    cmd = binary_path + "gaiadebug pubkey " + valconspub_new
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    address_new = result.split("\n")[0].split(": ")[1]

    cmd = binary_path + "gaiakeyutil " + str(address_new)
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    valcons_new = result.split("\n")[7].split("- ")[1]

    cmd = binary_path + "gaiacli keys parse " + valconspub_new
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    bytes_new = result.split("\n")[1].split(" ")[1][10:]
    
    cmd = binary_path + "gaiadebug pubkey " + str(bytes_new)
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    pubkey_new = json.loads(result.split("\n")[2].split(": ")[1])["value"]

    cmd = binary_path + "gaiadebug pubkey " + str(pubkey_new)
    result = subprocess.check_output(cmd,shell=True).decode("utf8")
    address_new = result.split("\n")[0].split(": ")[1]

    cmd = "sed -i 's%" + valconspub_old + "%" + valconspub_new + "%g' " + new_state_file
    print("replace " + valconspub_old + " to " + valconspub_new)
    subprocess.call(cmd,shell=True)
    cmd = "sed -i 's%" + pubkey_old + "%" + pubkey_new + "%g' " + new_state_file
    print("replace " + pubkey_old + " to " + pubkey_new)
    subprocess.call(cmd,shell=True)
    cmd = "sed -i 's%" + address_old + "%" + address_new + "%g' " + new_state_file
    print("replace " + address_old + " to " + address_new)
    subprocess.call(cmd,shell=True)
    cmd = "sed -i 's%" + valcons_old + "%" + valcons_new + "%g' " + new_state_file
    print("replace " + valcons_old + " to " + valcons_new)
    subprocess.call(cmd,shell=True)

time.sleep(1)
print("\nreplacement script complete!\n")

# print shasum 
print("new state file shasum after replacement")
cmd = "jq -S -c -M '' " + new_state_file + " | shasum -a 256"
print(subprocess.check_output(cmd,shell=True).decode("utf8"))
time.sleep(1)
