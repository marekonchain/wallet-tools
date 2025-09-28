```python
from solana.keypair import Keypair
from solana.rpc.api import Client

# Generate new Solana wallet
kp = Keypair()
print("Public Key:", kp.public_key)
print("Private Key (keep safe):", kp.secret_key)

# Connect to Devnet
client = Client("https://api.devnet.solana.com")

# Request airdrop (1 SOL = 1,000,000,000 lamports)
airdrop = client.request_airdrop(kp.public_key, 1_000_000_000)
print("Airdrop Tx:", airdrop)
