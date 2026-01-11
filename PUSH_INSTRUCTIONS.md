Git push / Publish guide

If you want to publish this repository to GitHub, here are the steps.

1) Create a new repo on GitHub (your account). Example name: `sh-myver`.

2) On your machine (project root), run:

```powershell
git remote remove origin 2>$null
git remote add origin https://github.com/<your-username>/sh-myver.git
git branch -M main
git push -u origin main
```

Notes
- If you prefer SSH, use the SSH URL instead: `git@github.com:<your-username>/sh-myver.git`.
- If push fails with a permission error, either push from an account with access or add the pushing account as a collaborator on the target repository.
- I can attempt to push from this environment, but the process will fail unless the environment is authenticated with an account that has push rights.
