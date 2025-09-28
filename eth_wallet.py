from web3 import Web3
import secrets

# Connect to Ethereum Sepolia testnet (replace with your Infura/Alchemy URL)
INFURA_URL = "https://sepolia.infura.io/v3/YOUR_API_KEY"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Generate a new ETH wallet
priv = secrets.token_hex(32)
private_key = "0x" + priv
acct = w3.eth.account.from_key(private_key)

print("Address:", acct.address)
print("Private Key (keep safe):", private_key)
