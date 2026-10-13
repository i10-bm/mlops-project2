def call() {
    echo "=== Executing Pre-Prod Pipeline ==="
    sh 'python3 scripts/register.py --alias Challenger-pre-test'
    sh 'pytest tests/'
    sh 'python3 scripts/update_alias.py --from Challenger-pre-test --to Challenger-post-test'
}
