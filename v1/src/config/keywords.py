"""
IRC News Bot - A bot that monitors crypto-related news from IRC channels and forwards them to Telegram
Copyright (C) 2024  GaloisField

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

CRYPTO_KEYWORDS = [
    # Cryptocurrencies
    "bitcoin", "btc", "ethereum", "eth", "dogecoin",
    
    # Crypto-specific terms
    "crypto", "cryptocurrency", "blockchain", "defi", "nft",
    "polymarket", "web3", "crypto mining", "altcoin", "microstrategy", "Michael Saylor"
    
    # Exchanges and platforms
    "binance", "coinbase", "dex", "decentralized exchange", "centralized exchange",
    
    # Technical terms
    "asic miner", "cold storage", "cryptography", "dao",
    "erc20", "crypto escrow", "fomo", "fud", "kyc",
    "multisignature wallet", "privacy coin", "blockchain p2p", "sha-256",
    "hardware wallet", "block reward", "software wallet",
    "double-spend attack", "blockchain node", "wallet address",
    
    # Market and trading terms
    "crypto market", "crypto trading", "crypto exchange",
    "bull market crypto", "bear market crypto", "crypto halving", "blockchain fork",
    "hash rate", "gas fee", "crypto market cap", "crypto volatility", "crypto liquidity",
    "crypto whale", "to the moon", "crypto pump",
    
    # DeFi and Smart Contracts
    "smart contract", "proof-of-work", "proof-of-stake", "stablecoin",
    "yield farming", "liquidity pool", "defi protocol", "blockchain oracle",
    "mining difficulty", "blockchain network", "crypto wallet",
    
    # Crypto culture and community
    "hodl", "satoshi nakamoto", "crypto adoption", "institutional crypto",
    "crypto whitepaper", "51% attack", "crypto airdrop",
    "blockchain governance", "crypto staking", "layer 2",
    "crypto scalability", "blockchain interoperability",
    
    # Memes and slang
    "memecoin", "shitcoin", "diamond hands", "paper hands", "bag holder",
    "crypto shill", "rugpull", "crypto fud", "crypto fomo",
    
    # Prediction markets
    "prediction market", "event contracts", "crypto gambling",
    "crypto derivatives", "virtual automated market makers", "vamm",
    
    # Social and community
    "crypto influencer", "crypto twitter", "crypto reddit", "crypto youtube",
    
    # Market behavior
    "crypto manipulation", "pump and dump crypto", "crypto scam",
    
    # Regulatory
    "crypto aml", "crypto regulatory", "crypto compliance"
] 