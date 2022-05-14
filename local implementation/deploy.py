from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)
# install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            },
        },
    },
    solc_version="0.6.0",
)
# print(compiled_sol)


with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi

abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# print(abi)

# connecting to ganache

w3 = Web3(
    Web3.HTTPProvider("https://kovan.infura.io/v3/f6e016a92a82467597ede397598ce0e2")
)
chain_id = 42
my_address = "0xa62d5D83B71419626FE359C2a6b39cC975C9706d"
private_key = os.getenv("PRIVATE_KEY")


# create contract

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)

# get the latest transaction
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)


transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying contract...")
# send signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# wait for receipt
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print("Deployed!...")

# working with contract
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# Call -> making call and getting return value
# Transact -> we make state change

# Initial value of favourite number
print(simple_storage.functions.retrieve().call())
print("Updating Contrect!...")
# print(simple_storage.functions.store(15).call())

store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

send_store_tnx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tnx)
print("Updated!...")
print(simple_storage.functions.retrieve().call())
