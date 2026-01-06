#!/usr/bin/env python3
"""
Delete all connected accounts from your Stripe platform.

Usage:
    python delete_connected_accounts.py [--dry-run]

Options:
    --dry-run    List accounts without deleting them
"""

import os
import sys
import stripe
from dotenv import load_dotenv

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

# Initialize Stripe
stripe_api_key = os.getenv('STRIPE_SECRET_KEY')
if not stripe_api_key:
    print("Error: STRIPE_SECRET_KEY not found in environment variables.")
    print("Please check your .env file.")
    sys.exit(1)

stripe.api_key = stripe_api_key


def safe_delete_account(account_id: str, dry_run: bool = False) -> bool:
    """Safely delete a connected account, handling errors gracefully."""
    try:
        if dry_run:
            print(f"  [DRY RUN] Would delete: {account_id}")
            return True
        
        stripe.Account.delete(account_id)
        print(f"  ✓ Deleted: {account_id}")
        return True
    except stripe.InvalidRequestError as e:
        if "No such" in str(e):
            print(f"  ✗ Not found: {account_id}")
        else:
            print(f"  ✗ Error deleting {account_id}: {e}")
        return False
    except Exception as e:
        print(f"  ✗ Error deleting {account_id}: {e}")
        return False


def list_connected_accounts():
    """List all connected accounts."""
    accounts = []
    starting_after: str | None = None
    
    while True:
        if starting_after:
            response = stripe.Account.list(limit=100, starting_after=starting_after)
        else:
            response = stripe.Account.list(limit=100)
        accounts.extend(response.data)
        
        if not response.has_more:
            break
        
        starting_after = response.data[-1].id
    
    return accounts


def main():
    dry_run = "--dry-run" in sys.argv
    
    # Verify connection
    try:
        platform_account = stripe.Account.retrieve()
        print(f"Connected to Stripe account: {platform_account.id}")
        display_name = (
            platform_account.settings.dashboard.display_name
            if platform_account.settings and platform_account.settings.dashboard
            else None
        )
        print(f"Business name: {display_name or 'Not set'}")
    except stripe.AuthenticationError:
        print("Error: Invalid Stripe API key.")
        sys.exit(1)
    
    print()
    print("=" * 50)
    if dry_run:
        print("DRY RUN: Listing Connected Accounts")
    else:
        print("Deleting All Connected Accounts")
    print("=" * 50)
    
    # Get all connected accounts
    print("\nFetching connected accounts...")
    accounts = list_connected_accounts()
    
    if not accounts:
        print("No connected accounts found.")
        return
    
    print(f"Found {len(accounts)} connected account(s):\n")
    
    # Show account details
    for account in accounts:
        email = account.email or "No email"
        business_name = (
            account.business_profile.name
            if account.business_profile and account.business_profile.name
            else "No name"
        )
        print(f"  • {account.id} - {business_name} ({email})")
    
    print()
    
    if not dry_run:
        # Confirm deletion
        response = input(f"Delete all {len(accounts)} account(s)? [y/N]: ")
        if response.lower() != "y":
            print("Aborted.")
            return
        print()
    
    # Delete accounts
    deleted_count = 0
    failed_count = 0
    
    for account in accounts:
        if safe_delete_account(account.id, dry_run):
            deleted_count += 1
        else:
            failed_count += 1
    
    print()
    print("=" * 50)
    if dry_run:
        print(f"DRY RUN complete. {deleted_count} account(s) would be deleted.")
    else:
        print(f"Deleted {deleted_count} account(s), {failed_count} failed.")
    print("=" * 50)


if __name__ == "__main__":
    main()
