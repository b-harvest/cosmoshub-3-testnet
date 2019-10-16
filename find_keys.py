import subprocess
import json
import time

# environment variables
read_file = "replacement_plan.txt" # containing list of valconspub_old, valconspub_new
write_file = "replace_script.sh"
binary_path = "./"
new_state_file = "genesis.json"


# run replacement script
print("finding keys...")
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
    print(cmd)
    result_string.append(cmd)
    cmd = "sed -i 's%" + pubkey_old + "%" + pubkey_new + "%g' " + new_state_file
    print(cmd)
    result_string.append(cmd)
    cmd = "sed -i 's%" + address_old + "%" + address_new + "%g' " + new_state_file
    print(cmd)
    result_string.append(cmd)
    cmd = "sed -i 's%" + valcons_old + "%" + valcons_new + "%g' " + new_state_file
    print(cmd)
    result_string.append(cmd)

with open(write_file,"w+") as f:
    for line in result_string:
        f.write(line + "\n")


