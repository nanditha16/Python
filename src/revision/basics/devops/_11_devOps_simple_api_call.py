"""
Use Case: Integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.
-------------------------------------------------------
DevOps engineers often monitor database replication to ensure data consistency.
This script uses a while loop to:
1. Authentication support via GitHub token
2. Error handling and rate limit awareness
3. Modular structure for reusability
4. Optional CLI arguments for flexibility
5. Clean output formatting

# Basic usage
python _11_devOps_simple_api_call.py

# Filter PRs created after July 1, 2025
python _11_devOps_simple_api_call.py 2025-07-01

"""

import requests
import os
import sys
from dotenv import load_dotenv

from collections import defaultdict
from utility.devops_library import setup_safe_logging

import csv
from datetime import datetime
from typing import Dict, List, Optional

# ---------------- Load Environment ----------------
# Load environment variables from .env file (local setup)
load_dotenv()

# ---------------- Logging Setup ----------------

# Set up logging
log_path = setup_safe_logging("application.log")

# ---------------- Configuration ----------------
# Constants
# URL to fetch pull requests from the GitHub API
GITHUB_API_URL = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
DEFAULT_HEADERS = {
    "Accept": "application/vnd.github.v3+json"
}
PER_PAGE = 100  # Max allowed by GitHub

# ---------------- Core Logic ----------------

def get_github_token() -> str:
    """Retrieve GitHub token from environment variable."""
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        print("GitHub token not found. Set GITHUB_TOKEN as an environment variable.")
        sys.exit(1)
    return GITHUB_TOKEN


# Make a GET request to fetch pull requests data from the GitHub API
def fetch_all_pull_requests(headers: Dict[str, str], since: Optional[str] = None) -> List[dict]:
    """Fetch all pull requests using pagination."""
    pulls = []
    page = 1
    while True:
        params = {"state": "open", "per_page": PER_PAGE, "page": page}
        response = requests.get(GITHUB_API_URL, headers=headers, params=params)
        if response.status_code != 200:
            print(f"❌ Failed to fetch page {page}. Status code: {response.status_code}")
            sys.exit(1)
        page_data = response.json()
        if not page_data:
            break
        if since:
            page_data = filter_by_date(page_data, since)
        pulls.extend(page_data)
        page += 1
    return pulls

def filter_by_date(pulls: List[dict], since: str) -> List[dict]:
    """Filter PRs created after a specific date."""
    try:
        cutoff = datetime.strptime(since, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        sys.exit(1)

    filtered = []
    for pr in pulls:
        created_at = pr.get("created_at")
        if created_at:
            pr_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
            if pr_date >= cutoff:
                filtered.append(pr)
    return filtered

def extract_pr_creators(pulls: list) -> Dict[str, int]:
    """Extract PR creators and count their contributions."""
    pr_creators = defaultdict(int)
    for pull in pulls:
        creator = pull.get("user", {}).get("login")
        if creator:
            pr_creators[creator] += 1
    return pr_creators

def display_pr_stats(pr_creators: Dict[str, int]) -> None:
    """Display PR creator statistics."""
    print("\nActive Pull Request Creators on Kubernetes Repo:")
    for creator, count in sorted(pr_creators.items(), key=lambda x: x[1], reverse=True):
        print(f"🔹 {creator}: {count} PR(s)")

def export_to_csv(pr_creators: Dict[str, int], filename: str = "pr_creators.csv") -> None:
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "PR Count"])
            for creator, count in pr_creators.items():
                writer.writerow([creator, count])
        print(f"\nData exported to {filename}")
    except IOError as e:
        print(f"Failed to write CSV: {e}")

def main():
    print("Fetching active pull request data from Kubernetes GitHub repo...")
    token = get_github_token()
    headers = {**DEFAULT_HEADERS, "Authorization": f"Bearer {token}"}

    # Optional: pass a date filter via command-line argument
    since_date = sys.argv[1] if len(sys.argv) > 1 else None

    pulls = fetch_all_pull_requests(headers, since=since_date)
    pr_creators = extract_pr_creators(pulls)
    display_pr_stats(pr_creators)
    export_to_csv(pr_creators)

# ---------------- Execution ----------------
if __name__ == "__main__":
    main()