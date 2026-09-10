import pandas as pd

provider = pd.read_csv('provider_transactions.csv')

internal = pd.read_csv('internal_transactions.csv')
print("Here are the providers transactions:")

#print(provider)

print("\n Internal transactions:")
print(internal)

#DATA VALIDATION
required_columns = [
    "transaction_id",
    "transaction_date",
    "phone_number",
    "amount",
    "fee",
    "status"
]
for column in required_columns:
    if column not in provider.columns:
        print(f"Missing column in provider file:{column}")
        print(provider.isnull().sum())

provider_duplicates = provider[
    provider.duplicated(
        subset=['transaction_id'],
        keep=False
    )
]
internal_duplicates = internal[
    internal.duplicated(
        subset=['transaction_id'],
        keep=False
    )
]
print("Here are duplicate transactions form provider")
print(provider_duplicates)
#print("Here are duplicate transactions form provider\n")
#print(internal_duplicates)

#Merging the 2 data from the provider and the internal data from the platform

reconciliation = provider.merge(
    internal, on="transaction_id",
    how="outer",
    suffixes=("_provider","_internal"),
    indicator=True
)
print("Data from provider merge with internal data from the platform\n")
#print(reconciliation)

missing_internal = reconciliation[
    reconciliation["_merge"] == "left_only"
]
missing_provider = reconciliation[
    reconciliation["_merge"] == "left_only"
]
print(missing_provider)