from web3 import Web3, HTTPProvider
import json

# Change this only if your contract address changes
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"
RPC_URL = "http://127.0.0.1:7545"

def load_contract():
    web3 = Web3(HTTPProvider(RPC_URL))
    compiled_contract_path = 'Report.json'

    with open(compiled_contract_path) as file:
        contract_data = json.load(file)
        abi = contract_data["abi"]
    
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    return contract

def read_all_data():
    contract = load_contract()

    print("\n--- Hospital Details ---")
    print(contract.functions.getHospital().call())

    print("\n--- Patient Details ---")
    print(contract.functions.getPatient().call())

    print("\n--- Prescription Details ---")
    print(contract.functions.getPrescription().call())

if __name__ == "__main__":
    read_all_data()
