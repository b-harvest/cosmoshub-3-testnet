# export-migrate-replace script

## configuration(in replace.py)

### environment variables
read_file = "replacement_plan.txt" # containing list of valconspub_old, valconspub_new
original_state_file = "cosmoshub-2-export-at-2140000.json"
new_state_file = "genesis.json"
binary_path = "./" # path where gaiad, gaiacli, gaiadebug is located
version_tobe = "v0.36"
chain_id_tobe = "cosmoshub-3-testnet"
genesis_time_tobe = "2019-10-14T00:00:00Z"
