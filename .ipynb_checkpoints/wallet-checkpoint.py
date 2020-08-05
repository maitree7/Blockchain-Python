{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import libraries\n",
    "import subprocess\n",
    "import json\n",
    "import os\n",
    "from constants import *\n",
    "from dotenv import load_dotenv\n",
    "from bipwallet import wallet\n",
    "from web3 import Web3\n",
    "from eth_account import Account\n",
    "from bit import PrivateKeyTestnet\n",
    "from bit.network import NetworkAPI\n",
    "from web3.middleware import geth_poa_middleware\n",
    "from web3.gas_strategies.time_based import medium_gas_price_strategy\n",
    "\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "cannon chronic machine excess hope blanket giraffe cancel behave hello absurd input\n"
     ]
    }
   ],
   "source": [
    "# import mnemonic from env\n",
    "filepath=\"env.bat\"\n",
    "p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)\n",
    "\n",
    "stdout, stderr = p.communicate()\n",
    "print (p.returncode) # is 0 if success\n",
    "mnemonic = os.getenv('MNEMONIC')\n",
    "print(mnemonic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "# connect to local ETH/ geth\n",
    "w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))\n",
    "w3.middleware_onion.inject(geth_poa_middleware, layer=0)\n",
    "w3.eth.setGasPriceStrategy(medium_gas_price_strategy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define function to derive wallet\n",
    "def derive_wallets(mnemonic, coin, numderive):\n",
    "    \"\"\"Use the subprocess library to call the php file script from Python\"\"\"\n",
    "    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic=\"{mnemonic}\" --numderive=\"{numderive}\" --coin=\"{coin}\" --format=json' \n",
    "    \n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)\n",
    "    (output, err) = p.communicate()\n",
    "   \n",
    "    keys = json.loads(output)\n",
    "    return  keys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'path': \"m/44'/0'/0'/0/0\",\n",
       "  'address': '16TbGXrr2gjCAkSnxb1dseACLUEgb1FUYQ',\n",
       "  'xprv': 'xprvA3xaAvWDJc2B8mPFyEMzQotCRDLah4vn7T5toQ7LiFSEAjqjvUt3gQ5ztaDcrNfeXuSoRjdfQufghFgjHJWtXxDbpQZqFWrRWhyjHfM3SsU',\n",
       "  'xpub': 'xpub6GwvaS378yaUMFTj5FtzmwpvyFB56XedUg1VbnWxGayD3YAtU2CJECQUjsnMTcgfmy7GmSxhU3rRUp3cmMkzdx9dmjkeVHphVrhLqTSp1iq',\n",
       "  'privkey': 'KyM3bVtH4Kg1Q4CitFNJSf4rvtqhdZAkyTuALBjyZaioZw3t9W7g',\n",
       "  'pubkey': '038d285ea71e7c2dd48b0d93bca5db5b40cc05eede41afe894c5e29415fb6d6fc6',\n",
       "  'pubkeyhash': '3be00c9af3c214fcf0acf871a59733ca8bd9b636',\n",
       "  'index': 0},\n",
       " {'path': \"m/44'/0'/0'/0/1\",\n",
       "  'address': '1LNvZPxNiW3xymMg8mMzVbiEaRCN68KvB5',\n",
       "  'xprv': 'xprvA3xaAvWDJc2BAgXZC947voTrRGp6gVtEt7KXEVqWs7XGsAeSugMjKp4PHmMn2PSe4Boc1mRFnvRyHWcunjt7E86Pa4FG8hHpVfqG3M38zfD',\n",
       "  'xpub': 'xpub6GwvaS378yaUPAc2JAb8HwQayJeb5xc6FLF82tF8RT4FjxybTDfyscNs92K86SZ2nNKZPFQcbC7uQ864SurCaMWbix17C7MHRcxKCaqK1v5',\n",
       "  'privkey': 'KyN3SXH8dHgqTSu1UJ2uLVBCkTG63JBSE5XoN7GozsYR4vYTv94i',\n",
       "  'pubkey': '0235eca9c4d08c9fc3424b753e8be6822f12746d3d680723a5ba078c47e0a99901',\n",
       "  'pubkeyhash': 'd48fd561249fd17d601468876b41071276b6cb08',\n",
       "  'index': 1},\n",
       " {'path': \"m/44'/0'/0'/0/2\",\n",
       "  'address': '1KY6VYJDZhSTFysai12WqAtEr1mdmMZACg',\n",
       "  'xprv': 'xprvA3xaAvWDJc2BE68wnGJoue99DjvZ9uNfr4mqftsUpFdBLenPWwZjx1M7gpn37jRPLSSRxQJzMFdbhdN8FF6R1wR6JLfJCcBC9hjtqkS5tb9',\n",
       "  'xpub': 'xpub6GwvaS378yaUSaDQtHqpGn5smmm3ZN6XDHhSUHH6NbAADT7Y4UszVofbY5PA6NT3raGFsxs448Jn37jcUKhPPxg6SgJH5EjBCMPPhmGxBZv',\n",
       "  'privkey': 'L2FnjNzAZAm9zfULwvZPuHDU4NjkGiSeF2Qn6ZPNQa7Ae5e3YogZ',\n",
       "  'pubkey': '025e4b66228a2a24fa13c64bc2aa282382cb1fd6214af2e35a833c3e159dd47ff5',\n",
       "  'pubkeyhash': 'cb53be53c9e4629ccead0fba9a1ee0b87a5cf883',\n",
       "  'index': 2}]"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Test the function derive_wallets\n",
    "derive_wallets(mnemonic, 'BTC', 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Setting dictionary of coins to be used in the wallet\n",
    "coins = {\"eth\", \"btc-test\", \"btc\"}\n",
    "numderive = 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "# \n",
    "keys = {}\n",
    "for coin in coins:\n",
    "    keys[coin]= derive_wallets(mnemonic, coin, numderive=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"0x30c2577db89760baa9ba4058b1033b9e103f287e5de1689e35833ee8e7a7c857\"\n",
      "\"cNYVznjLVmB5XANVr4SJ6choENNntn1t96jPQbn51rGUjTrpsnV7\"\n"
     ]
    }
   ],
   "source": [
    "\n",
    "eth_PrivateKey = keys[\"eth\"][0]['privkey']\n",
    "btc_PrivateKey = keys['btc-test'][0]['privkey']\n",
    "\n",
    "print(json.dumps(eth_PrivateKey, indent=4, sort_keys=True))\n",
    "print(json.dumps(btc_PrivateKey, indent=4, sort_keys=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create a function that convert the privkey string in a child key to an account object.\n",
    "def priv_key_to_account(coin,priv_key):\n",
    "    print(coin)\n",
    "    print(priv_key)\n",
    "    if coin == ETH:\n",
    "        return Account.privateKeyToAccount(priv_key)\n",
    "    elif coin == BTCTEST:\n",
    "        return PrivateKeyTestnet(priv_key)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_tx(coin,account, recipient, amount):\n",
    "    if coin == ETH: \n",
    "        gasEstimate = w3.eth.estimateGas(\n",
    "            {\"from\":eth_acc.address, \"to\":recipient, \"value\": amount}\n",
    "        )\n",
    "        return { \n",
    "            \"from\": eth_acc.address,\n",
    "            \"to\": recipient,\n",
    "            \"value\": amount,\n",
    "            \"gasPrice\": w3.eth.gasPrice,\n",
    "            \"gas\": gasEstimate,\n",
    "            \"nonce\": w3.eth.getTransactionCount(eth_acc.address)\n",
    "        }\n",
    "    \n",
    "    elif coin == BTCTEST:\n",
    "        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eth\n",
      "0x30c2577db89760baa9ba4058b1033b9e103f287e5de1689e35833ee8e7a7c857\n"
     ]
    }
   ],
   "source": [
    "# create a function to hold Ethereum \n",
    "eth_acc = priv_key_to_account(ETH, derive_wallets(mnemonic, ETH,5)[0]['privkey'])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create a function to send txn\n",
    "def send_txn(coin,account,recipient, amount):\n",
    "    txn = create_tx(coin, account, recipient, amount)\n",
    "    if coin == ETH:\n",
    "        signed_txn = eth_acc.sign_transaction(txn)\n",
    "        result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)\n",
    "        return result.hex()\n",
    "    elif coin == BTCTEST:\n",
    "        signed_txn = account.sign_transaction(txn)\n",
    "        return NetworkAPI.broadcast_tx_testnet(signed_txn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0x4f8b0c162957811ddb7deb1b297fa707e41a81e65def03d89659fb6ad0a2184f'"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#use the send_txn function to send transactions \n",
    "send_txn(ETH,eth_acc,'0x46BbdBf56ff911A93AdaF0164d0709F78B52765E',1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## BTC-TEST Transactions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "btc-test\n",
      "cNYVznjLVmB5XANVr4SJ6choENNntn1t96jPQbn51rGUjTrpsnV7\n"
     ]
    }
   ],
   "source": [
    "btc_acc = priv_key_to_account(BTCTEST,btc_PrivateKey)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"unspents\":[{\"amount\":49808912,\"confirmations\":-1781555,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"62989ab0fa72c9ed0a2de95e878d94391522a036a448ad4bbeeaa2949fed2b8e\",\"txindex\":14,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":100000,\"confirmations\":-1781480,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"f509aa70dd53d1d1938d6c3916906e1c49183a01e199fafc07fa20bce31f57f7\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":23000,\"confirmations\":-1781480,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"d5c99494f1dabcc740edd4126430e9baa09fdd09a30400830f3906245dfd45ff\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":10969,\"confirmations\":-1781479,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"d117e459d8ce4eec6ff607fd7002790372f0a7c6288ae1ebfffbb3a1133ddff0\",\"txindex\":1,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false}],\"outputs\":[[\"mtK73sNPY9CKuzVvpv4W1969AD1UmGGfsX\",10000000],[\"n3D8vVvLyD7pPQmWoQgMMERZrDjmBheBpU\",39798161]]}'"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create BTC transaction\n",
    "create_tx(BTCTEST,btc_acc,\"mtK73sNPY9CKuzVvpv4W1969AD1UmGGfsX\", 0.1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"unspents\":[{\"amount\":49808912,\"confirmations\":-1781555,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"62989ab0fa72c9ed0a2de95e878d94391522a036a448ad4bbeeaa2949fed2b8e\",\"txindex\":14,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":100000,\"confirmations\":-1781480,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"f509aa70dd53d1d1938d6c3916906e1c49183a01e199fafc07fa20bce31f57f7\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":23000,\"confirmations\":-1781480,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"d5c99494f1dabcc740edd4126430e9baa09fdd09a30400830f3906245dfd45ff\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false},{\"amount\":10969,\"confirmations\":-1781479,\"script\":\"76a914edf426ec881075b8ad83bd43951d86ab79007d3988ac\",\"txid\":\"d117e459d8ce4eec6ff607fd7002790372f0a7c6288ae1ebfffbb3a1133ddff0\",\"txindex\":1,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false}],\"outputs\":[[\"mtK73sNPY9CKuzVvpv4W1969AD1UmGGfsX\",10000000],[\"n3D8vVvLyD7pPQmWoQgMMERZrDjmBheBpU\",39798161]]}'"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Send BTC transaction\n",
    "create_tx(BTCTEST,btc_acc,\"mtK73sNPY9CKuzVvpv4W1969AD1UmGGfsX\", 0.1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## ETH Transactions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "You can't add the same un-named instance twice",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-147-576601230a47>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mw3\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmiddleware_onion\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minject\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mgeth_poa_middleware\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mlayer\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\web3\\datastructures.py\u001b[0m in \u001b[0;36minject\u001b[1;34m(self, element, name, layer)\u001b[0m\n\u001b[0;32m    167\u001b[0m             )\n\u001b[0;32m    168\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 169\u001b[1;33m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0madd\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0melement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    170\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    171\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mlayer\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\web3\\datastructures.py\u001b[0m in \u001b[0;36madd\u001b[1;34m(self, element, name)\u001b[0m\n\u001b[0;32m    140\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mname\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_queue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    141\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mname\u001b[0m \u001b[1;32mis\u001b[0m \u001b[0melement\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 142\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"You can't add the same un-named instance twice\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    143\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    144\u001b[0m                 \u001b[1;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"You can't add the same name again, use replace instead\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: You can't add the same un-named instance twice"
     ]
    }
   ],
   "source": [
    "w3.middleware_onion.inject(geth_poa_middleware, layer=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
