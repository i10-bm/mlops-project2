def call() {
    echo "=== Executing Dev Pipeline ==="
    sh 'python3 scripts/train.py'
    sh 'python3 scripts/register.py --alias Challenger'
}
