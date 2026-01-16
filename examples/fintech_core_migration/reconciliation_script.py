import pandas as pd

def reconcile_ledgers(legacy_csv, new_db_export):
    """
    Compares the Legacy Ledger against the New Microservice Ledger.
    """
    legacy = pd.read_csv(legacy_csv)
    new_sys = pd.read_csv(new_db_export)

    diff = legacy['balance'] - new_sys['balance']
    if diff.sum() != 0:
        raise CriticalError("MONEY HAS VANISHED!")

    print("Reconciliation Complete. Variance: $0.00")
