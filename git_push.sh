
#!/bin/bash

set -e

# =====================================
# BASIC NETWORK SNIFFER - GIT PUSH
# =====================================

PROJECT_NAME="Basic-Network-Sniffer"
BRANCH="main"
COMMIT_MESSAGE="${1:-Initial commit: Basic Network Sniffer}"

echo ""
echo "=========================================="
echo "       BASIC NETWORK SNIFFER"
echo "          GITHUB UPLOADER"
echo "=========================================="

# Check Git installation
if ! command -v git >/dev/null 2>&1; then
    echo "[!] Git is not installed."
    exit 1
fi

# Move to project directory
cd "$(dirname "$0")"

echo "[+] Project directory: $(pwd)"

# Check required project file
if [ ! -f "simple_scanner.py" ]; then
    echo "[!] simple_scanner.py not found!"
    exit 1
fi

# Create .gitignore if missing
if [ ! -f ".gitignore" ]; then
    cat > .gitignore <<'EOF'
venv/
__pycache__/
*.pyc
reports/*.csv
reports/*.txt
!reports/.gitkeep
.env
.vscode/
.idea/
EOF
    echo "[+] Created .gitignore"
fi

# Preserve reports directory
mkdir -p reports
touch reports/.gitkeep

# Initialize Git if required
if [ ! -d ".git" ]; then
    git init
    echo "[+] Git repository initialized"
fi

# Configure branch
git branch -M "$BRANCH"

# Stage project files
git add -A

# Show staged files
echo ""
echo "Files ready for upload:"
git status --short

# Commit changes if required
if ! git diff --cached --quiet; then

    git commit -m "$COMMIT_MESSAGE"

else

    echo "[+] No new changes to commit."

fi

# Check remote
if ! git remote get-url origin >/dev/null 2>&1; then

    echo ""
    read -rp "Enter your GitHub repository URL:https://github.com/vedanta-16/Network-Sniffer.git " REPO_URL

    if [ -z "https://github.com/vedanta-16/Network-Sniffer.git" ]; then
        echo "[!] Repository URL is required."
        exit 1
    fi

    git remote add origin "https://github.com/vedanta-16/Network-Sniffer.git"

fi

# Push to GitHub
echo ""
echo "[+] Pushing project to GitHub..."

git push -u origin "$BRANCH"

echo ""
echo "=========================================="
echo "       PROJECT PUSH SUCCESSFUL!"
echo "=========================================="
echo "Project: Network-Sniffer"
echo "Branch : $BRANCH"
echo "=========================================="
