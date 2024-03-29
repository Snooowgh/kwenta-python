config = {
    'candles': {
        "id": ["id", "String"],
        "synth": ["synth", "String"],
        "open": ["open", "BigInt"],
        "high": ["high", "BigInt"],
        "low": ["low", "BigInt"],
        "close": ["close", "BigInt"],
        "timestamp": ["timestamp", "BigInt"],
        "average": ["average", "BigInt"],
        "period": ["period", "BigInt"],
        "aggregatedPrices": ["aggregated_prices", "BigInt"],
    },
    'trades': {
        "id": ["id", "ID"],
        "timestamp": ["timestamp", "BigInt"],
        "account": ["account", "Address"],
        "abstractAccount": ["abstract_account", "Address"],
        "accountType": ["account_type", "String"],
        "margin": ["margin", "Wei"],
        "size": ["size", "Wei"],
        "marketKey": ["market_key", "Bytes"],
        "asset": ["asset", "String"],
        "price": ["price", "Wei"],
        "positionId": ["position_id", "BigInt"],
        "positionSize": ["position_size", "Wei"],
        "positionClosed": ["position_closed", "Boolean"],
        "pnl": ["pnl", "Wei"],
        "feesPaid": ["fees_paid", "Wei"],
        "keeperFeesPaid": ["keeper_fees_paid", "Wei"],
        "orderType": ["order_type", "String"],
        "trackingCode": ["tracking_code", "String"],
        "fundingAccrued": ["funding_accrued", "Wei"]
    },
    'positions': {
        "id": ["id", "ID"],
        "lastTxHash": ["last_tx_hash", "Address"],
        "openTimestamp": ["open_timestamp", "BigInt"],
        "closeTimestamp": ["close_timestamp", "BigInt"],
        "timestamp": ["timestamp", "BigInt"],
        "market": ["market", "String"],
        "marketKey": ["market_key", "Bytes"],
        "asset": ["asset", "String"],
        "account": ["account", "Address"],
        "abstractAccount": ["abstract_account", "Address"],
        "accountType": ["account_type", "String"],
        "isOpen": ["is_open", "Boolean"],
        "isLiquidated": ["is_liquidated", "Boolean"],
        "trades": ["trades", "BigInt"],
        "totalVolume": ["total_volume", "Wei"],
        "size": ["size", "Wei"],
        "initialMargin": ["initial_margin", "Wei"],
        "margin": ["margin", "Wei"],
        "pnl": ["pnl", "Wei"],
        "feesPaid": ["fees_paid", "Wei"],
        "netFunding": ["net_funding", "Wei"],
        "pnlWithFeesPaid": ["pnl_with_fees_paid", "Wei"],
        "netTransfers": ["net_transfers", "Wei"],
        "totalDeposits": ["total_deposits", "Wei"],
        "fundingIndex": ["funding_index", "BigInt"],
        "entryPrice": ["entry_price", "Wei"],
        "avgEntryPrice": ["avg_entry_price", "Wei"],
        "lastPrice": ["last_price", "Wei"],
        "exitPrice": ["exit_price", "Wei"]
    },
    'funding_rate_history': {
        "id": ["id", "String"],
        "period": ["period", "String"],
        "asset": ["asset", "Bytes"],
        "marketKey": ["market_key", "Bytes"],
        "fundingRate": ["funding_rate", "Wei"],
        "timestamp": ["timestamp", "BigInt"],
    }
}
