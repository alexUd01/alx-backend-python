#!/usr/bin/env bash
# Initialize git repository
echo "# alx-backend-python" >> README.md
git init
git add README.md
git commit -m "Initialized project"
git branch -M master
git remote add origin git@github.com:alexUd01/alx-backend-python.git
git push -u origin master
