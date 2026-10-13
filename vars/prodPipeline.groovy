def call() {
    echo "=== Executing Production Pipeline ==="
    sh 'python3 scripts/update_alias.py --from Challenger-post-test --to Champion'
    echo "Model promoted to Champion successfully!"
}
