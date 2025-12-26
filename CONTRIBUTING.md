# Contributing to DING

Welcome to **DING**!
Before starting, make sure to read the following rules carefully!

---

## Before You Start

- Go through the `README.md` to understand the project.
- Check the **Issues** section and claim an issue by commenting on it.
- **WAIT** until a maintainer has assigned you to the issue (If issue is labelled as `open-for-all`, you may skip this and directly start working)
- If something is unclear or no contribution guide exists for a specific feature, **clarify with the mentors on the OpenCode Discord.**

---

## Steps to Contribute

### Step 1: Fork the Repository

- Fork the _DING_ repository to your GitHub account.
- Clone your fork locally:

  ```bash
  git clone https://github.com/<your-username>/DING.git
  ```

- Navigate to the project directory:

  ```bash
  cd DING
  ```

---

### Step 2: Make Your Changes

- Write clean, readable, and _well-documented_ code.
- Ensure your changes solve _only the issue you’re working on_.
- ALWAYS Test your changes **locally** before you push.

**NOTE** : Some issues may require working on a separate branch.
For this, do the following:

```bash
git switch <branch-name>
```

> Follow the branch naming convention if mentioned in the issue. Without them, the PR will NOT be accepted.

To switch back to the main branch:

```bash
git switch main
```

---

### Step 3: Commit Your Changes

After adding all your changed files, commit them as follows:

```bash
git commit -m "<short description of change>"
```

---

### Step 4: Open a Pull Requestt

Once you've solved the issue:

- Push your changes to your fork:
- Open a PR from your fork to the **main DING repository** (`opencodeiiita/echo`).

#### Step 4.5 : PR etiquette

Failure to follow these **WILL result in points not being awarded**, even if the PR is merged.

- Before submittnig a PR, ensure there are **no merge conflicts!** Always test locally and make sure everything works!.
- PR title must be **clear and relevant**.
- **PR SUBMISSION FORMAT:**:

  ```
  Issue : #<issue_number>

  FIX: <description_of_fix>

  ```

  (The `#` is mandatory, otherwise the PR will NOT be tagged to an issue!)

---

- If your PR follows the template correctly, you’ll receive a **“Valid PR”** message from our GitHub bot.
- If the PR is **invalid**, the bot will warn you and request changes.
- Modify the **same PR** to fix issues (i.e, make commits to the project without opening a new pr) — **do NOT close and open a new PR** unless a mentor asks you to.

---

### Making Changes After Review

- If a mentor requests changes:
  - Update your code in the **same PR**.
  - Push additional commits to that PR.
- DO NOT open multiple PRs for the same issue.

- Once all criteria are satisfied and your PR is approved, it will be merged!
- A successful merge earns you points on the [Leaderboard!](https://events.geekhaven.in/)

---

## Stuck?

- Reach out to mentors on Discord **if you have any confusion or queries**.
- Be respectful and patient during reviews and merges.

---

Happy contributing!
