def RLcalc(gc_accounts, mfa_accounts):
    gc_rate = 0.06666666666666667
    mfa_rate = 0.1

    combined_reqs = (gc_rate * gc_accounts) + (mfa_rate * mfa_accounts)
    return combined_reqs
while True:
    print("\n+--==--+ Rate Limit Calculator by: B1ueflame +--==--+")
    print()
    gc_accounts = int(input("Enter number of Giftcard (no name set yet) accounts: "))
    mfa_accounts = int(input("Enter number of MFA (name already set) accounts: "))

    total_requests = RLcalc(gc_accounts, mfa_accounts)
    print(f"The requests per second you can send is: {total_requests}")