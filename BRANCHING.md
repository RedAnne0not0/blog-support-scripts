# 🪴 Git Branching Policy for Blog Projects

## 📁 Repository Structure
- Local working directory is `~/Projects/coding/blog-support-scripts`.
- GitHub is used as the remote for backup, collaboration, and long-term version control.
- Remote GitHub repo is https://github.com/RedAnne0not0/blog-support-scripts
- Following a *main branch + feature branches* workflow.

---

## 🔁 Branching Strategy

### 🧵 `main`
- Always contains **stable**, working code.
- Only merge **fully tested features** into `main`.
- Avoid direct edits on `main`.

### 🌿 Feature Branches
- Create a new branch for **every feature, fix, or experiment**:
  ```bash
  git checkout -b feature-name
  ```
- Name branches clearly, e.g.:
  - `robust-front-matter`
  - `verbose-flag`
  - `copy-to-hugo`
  - `cli-args-support`

### 🧪 Testing & Iteration
- Keep commits small and meaningful: `WIP`, `Fix`, `Add`, etc.
- Use `git status` and `git diff` often.
- Test feature functionality *before* merging.

---

## 🔀 Merging Guidelines

### ✅ Before Merging into `main`:
1. **Ensure the feature is complete and tested.**
2. **Commit all changes**:
   ```bash
   git add .
   git commit -m "Add robust front matter detection"
   ```
3. **Switch to `main`**:
   ```bash
   git checkout main
   ```
4. **Merge the feature branch**:
   ```bash
   git merge feature-name
   ```

### 🧼 After Merging
- If done with the branch, **delete it**:
  ```bash
  git branch -d feature-name           # Local
  git push origin --delete feature-name  # Remote (optional)
  ```

---

## ✍️ Commit Message Style
- Use clear, imperative-style commits:
  - `Add CLI argument for verbosity`
  - `Fix broken front matter detection`
  - `Refactor main loop for clarity`
- Use `WIP:` for temporary in-progress commits.

---

## 📤 Pushing to GitHub
Only push when:
- A feature is complete
- You want off-device backup
- You want to share or archive progress

```bash
git push origin main
```

---

## 📌 Optional Conventions
- Use `README.md` to document the script’s purpose, usage, and flags.
- Maintain a `TODO.md` or Logseq-linked page for tracking planned features.
- Tag releases with:
  ```bash
  git tag -a v0.1 -m "First working draft of export script"
  git push origin --tags
  ```
