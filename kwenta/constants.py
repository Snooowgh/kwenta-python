DEFAULT_NETWORK_ID = 10
DEFAULT_TRACKING_CODE = (
    "0x6b77656e7461707973646b000000000000000000000000000000000000000000"
)
DEFAULT_SLIPPAGE = 2.0

DEFAULT_GQL_ENDPOINT_PERPS = {
    10: "https://api.thegraph.com/subgraphs/name/kwenta/optimism-perps",
    420: "https://api.thegraph.com/subgraphs/name/kwenta/optimism-goerli-perps",
}

DEFAULT_GQL_ENDPOINT_RATES = {
    10: "https://api.thegraph.com/subgraphs/name/kwenta/optimism-latest-rates",
    420: "https://api.thegraph.com/subgraphs/name/kwenta/optimism-goerli-latest-rates",
}

DEFAULT_PRICE_SERVICE_ENDPOINTS = {
    10: "https://xc-mainnet.pyth.network",
    420: "https://xc-testnet.pyth.network",
}

ACCOUNT_COMMANDS = {
    "ACCOUNT_MODIFY_MARGIN": [0, ["int256"]],
    "ACCOUNT_WITHDRAW_ETH": [1, ["uint256"]],
    "PERPS_V2_MODIFY_MARGIN": [2, ["address", "int256"]],
    "PERPS_V2_WITHDRAW_ALL_MARGIN": [3, ["address"]],
    "PERPS_V2_SUBMIT_ATOMIC_ORDER": [4, ["address", "int256", "uint256"]],
    "PERPS_V2_SUBMIT_DELAYED_ORDER": [5, ["address", "int256", "uint256", "uint256"]],
    "PERPS_V2_SUBMIT_OFFCHAIN_DELAYED_ORDER": [6, ["address", "int256", "uint256"]],
    "PERPS_V2_CLOSE_POSITION": [7, ["address", "uint256"]],
    "PERPS_V2_SUBMIT_CLOSE_DELAYED_ORDER": [8, ["address", "uint256", "uint256"]],
    "PERPS_V2_SUBMIT_CLOSE_OFFCHAIN_DELAYED_ORDER": [9, ["address", "uint256"]],
    "PERPS_V2_CANCEL_DELAYED_ORDER": [10, ["address"]],
    "PERPS_V2_CANCEL_OFFCHAIN_DELAYED_ORDER": [11, ["address"]],
    "GELATO_PLACE_CONDITIONAL_ORDER": [
        12,
        [
            "bytes32",
            "int256",
            "int256",
            "uint256",
            "ConditionalOrderTypes",
            "uint128",
            "bool",
        ],
    ],
    "GELATO_CANCEL_CONDITIONAL_ORDER": [13, ["uint256"]],
}
# https://docs.kwenta.io/developers/deployed-contracts/v2-futures-market-proxy-contracts
TOKEN_MARKET_ADDRESS_MAP = {"BNB": "0x0940B0A96C5e1ba33AEE331a9f950Bb2a6F2Fb25",
                            "AXS": "0x3a52b21816168dfe35bE99b7C5fc209f17a0aDb1",
                            "ETH": "0x2B3bb4c683BFc5239B029131EEf3B1d214478d93",
                            "BTC": "0x59b007E9ea8F89b069c43F8f45834d30853e3699",
                            "LINK": "0x31A1659Ca00F617E86Dc765B6494Afe70a5A9c1A",
                            "SOL": "0x0EA09D97b4084d859328ec4bF8eBCF9ecCA26F1D",
                            "AVAX": "0xc203A12F298CE73E44F7d45A4f59a43DBfFe204D",
                            "AAVE": "0x5374761526175B59f1E583246E20639909E189cE",
                            "UNI": "0x4308427C463CAEAaB50FFf98a9deC569C31E4E87",
                            "MATIC": "0x074B8F19fc91d6B2eb51143E1f186Ca0DDB88042",
                            "APE": "0x5B6BeB79E959Aac2659bEE60fE0D0885468BF886",
                            "DYDX": "0x139F94E4f0e1101c1464a321CBA815c34d58B5D9",
                            "OP": "0x442b69937a0daf9D46439a71567fABE6Cb69FBaf",
                            "DOGE": "0x98cCbC721cc05E28a125943D69039B39BE6A21e9",
                            "XAU": "0x549dbDFfbd47bD5639f9348eBE82E63e2f9F777A",
                            "XAG": "0xdcB8438c979fA030581314e5A5Df42bbFEd744a0",
                            "EUR": "0x87AE62c5720DAB812BDacba66cc24839440048d1",
                            "ATOM": "0xbB16C7B3244DFA1a6BF83Fcce3EE4560837763CD",
                            "FLOW": "0x27665271210aCff4Fab08AD9Bb657E91866471F0",
                            "FTM": "0xC18f85A6DD3Bcd0516a1CA08d3B1f0A4E191A2C4",
                            "NEAR": "0xC8fCd6fB4D15dD7C455373297dEF375a08942eCe",
                            "AUD": "0x9De146b5663b82F44E5052dEDe2aA3Fd4CBcDC99",
                            "GBP": "0x1dAd8808D8aC58a0df912aDC4b215ca3B93D6C49",
                            "ARB": "0x509072A5aE4a87AC89Fc8D64D94aDCb44Bd4b88e",
                            "LDO": "0xaa94C874b91ef16C8B56A1c5B2F34E39366bD484",
                            "LTC": "0xB25529266D9677E9171BEaf333a0deA506c5F99A",
                            "ADA": "0xF9DD29D2Fd9B38Cd90E390C797F1B7E0523f43A9",
                            "FIL": "0x2C5E2148bF3409659967FE3684fd999A76171235",
                            "GMX": "0x33d4613639603c845e61A02cd3D2A78BE7d513dc",
                            "APT": "0x9615B6BfFf240c44D3E33d0cd9A11f563a2e8D8B",
                            "SHIB": "0x69F5F465a46f324Fb7bf3fD7c0D5c00f7165C7Ea",
                            "BCH": "0x96690aAe7CB7c4A9b5Be5695E94d72827DeCC33f",
                            "CRV": "0xD5fBf7136B86021eF9d0BE5d798f948DcE9C0deA",
                            "PEPE": "0x3D3f34416f60f77A0a6cC8e32abe45D32A7497cb",
                            "SUI": "0x09F9d7aaa6Bef9598c3b676c0E19C9786Aa566a8",
                            "BLUR": "0xa1Ace9ce6862e865937939005b1a6c5aC938A11F",
                            "XRP": "0x6110DF298B411a46d6edce72f5CAca9Ad826C1De",
                            "DOT": "0x8B9B5f94aac2316f048025B3cBe442386E85984b",
                            "TRX": "0x031A448F59111000b96F016c37e9c71e57845096",
                            "FLOKI": "0x5ed8D0946b59d015f5A60039922b870537d43689",
                            "INJ": "0x852210F0616aC226A486ad3387DBF990e690116A",
                            "STETH": "0xD91Db82733987513286B81e7115091d96730b62A",
                            "ETHBTC": "0xD5FcCd43205CEF11FbaF9b38dF15ADbe1B186869",
                            "ETC": "0x4bF3C1Af0FaA689e3A808e6Ad7a8d89d07BB9EC7",
                            "COMP": "0xb7059Ed9950f2D9fDc0155fC0D79e63d4441e806",
                            "XMR": "0x2ea06E73083f1b3314Fa090eaE4a5F70eb058F2e",
                            "MKR": "0xf7d9Bd13F877171f6C7f93F71bdf8e380335dc12",
                            "YFI": "0x6940e7C6125a177b052C662189bb27692E88E9Cb",
                            "MAV": "0x572F816F21F56D47e4c4fA577837bd3f58088676",
                            "RPL": "0xfAD0835dAD2985b25ddab17eace356237589E5C7",
                            "WLD": "0x77DA808032dCdd48077FA7c57afbF088713E09aD",
                            "USDT": "0x1681212A0Edaf314496B489AB57cB3a5aD7a833f",
                            "BAL": "0x71f42cA320b3e9A8e4816e26De70c9b69eAf9d24",
                            "FXS": "0x2fD9a39ACF071Aa61f92F3D7A98332c68d6B6602",
                            "KNC": "0x152Da6a8F32F25B56A32ef5559d4A2A96D09148b",
                            "RNDR": "0x91cc4a83d026e5171525aFCAEd020123A653c2C9",
                            "ONE": "0x86BbB4E38Ffa64F263E84A0820138c5d938BA86E",
                            "PERP": "0xaF2E4c337B038eaFA1dE23b44C163D0008e49EaD",
                            "ZIL": "0x01a43786C2279dC417e7901d45B917afa51ceb9a",
                            "RUNE": "0xEAf0191bCa9DD417202cEf2B18B7515ABff1E196",
                            "SUSHI": "0xdcCDa0cFBEE25B33Ff4Ccca64467E89512511bf6",
                            "ZEC": "0xf8aB6B9008f2290965426d3076bC9d2EA835575e",
                            "XTZ": "0xC645A757DD81C69641e010aDD2Da894b4b7Bc921",
                            "UMA": "0xb815Eb8D3a9dA3EdDD926225c0FBD3A566e8C749",
                            "ENJ": "0x88C8316E5CCCCE2E27e5BFcDAC99f1251246196a",
                            "ICP": "0x105f7F2986A2414B4007958b836904100a53d1AD",
                            "XLM": "0xfbbBFA96Af2980aE4014d5D5A2eF14bD79B2a299",
                            "1INCH": "0xd5fAaa459e5B3c118fD85Fc0fD67f56310b1618D",
                            "EOS": "0x50a40d947726ac1373DC438e7aaDEde9b237564d",
                            "CELO": "0x2292865b2b6C837B7406E819200CE61c1c4F8d43",
                            "ALGO": "0x96f2842007021a4C5f06Bcc72961701D66Ff8465",
                            "ZRX": "0x76BB1Edf0C55eC68f4C8C7fb3C076b811b1a9b9f",
                            "SEI": "0x66fc48720f09Ac386608FB65ede53Bb220D0D5Bc",
                            "STETHETH": "0x08388dC122A956887c2F736Aaec4A0Ce6f0536Ce",
                            "TRB": "0xbdb26bfb6A229d7f254FAf1B2c744887ec5F1f31",
                            "TIA": "0x35B0ed8473e7943d31Ee1eeeAd06C8767034Ce39",
                            "IMX": "0xBBd74c2c8c89D45B822e08fCe400F4DDE99e600b",
                            "MEME": "0x48BeadAB5781aF9C4Fec27AC6c8E0F402F2Cc3D6",
                            "FET": "0x4272b356e7E406Eeef15E47692f7f4dE86370634",
                            "GRT": "0x3f957DF3AB99ff502eE09071dd353bf4352BBEfE",
                            "PYTH": "0x296286ae0b5c066CBcFe46cc4Ffb375bCCAFE640",
                            "ANKR": "0x90c9B9D7399323FfFe63819788EeD7Cde1e6A78C",
                            "BONK": "0xB3422e49dB926f7C5F5d7DaF5F1069Abf1b7E894"}
