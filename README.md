Yes, you can configure Git so that new files are pushed to GitHub while deleted files in your local directory are **not** removed from your GitHub repository. This can be done by adjusting how you stage and commit changes before pushing. Specifically, you'll need to **add new files** without including deleted files when staging your changes.

Here are the steps to achieve this:

### 1. **Manually Stage New and Modified Files** (Ignore Deleted Files)

When you run the `git add` command, instead of using `git add .` (which stages all changes including deletions), you can stage only new or modified files and **ignore deletions** using the `--ignore-removal` option:

```bash
git add --ignore-removal .
```

This will stage all new and modified files but will **not** stage files that have been deleted. Therefore, the deleted files won't be reflected in your commit or push.

### 2. **Manually Stage Specific Files**

If you want to be more selective, you can manually add only the new files by specifying them directly. For example:

```bash
git add newfile1 newfile2
```

This way, only the specified files will be staged for commit, and deleted files will remain unchanged in the GitHub repository.

### 3. **Configure Git to Automatically Ignore Deleted Files Globally**

You can also configure Git to **always** ignore deletions using a global Git configuration. This means Git will never stage deletions unless you explicitly add them.

Set this option globally using:

```bash
git config --global alias.addnew 'add --ignore-removal .'
```

This creates a `git addnew` alias, which you can use every time you want to add only new or modified files without removing any deleted files:

```bash
git addnew
```

### 4. **Pushing Changes**

After adding the files (without deletions), commit and push as usual:

```bash
git commit -m "Add new files"
git push origin main  # or whatever branch you are pushing to
```

### Example Workflow

Here’s an example of a typical workflow:

```bash
# Stage new and modified files, ignoring deletions
git add --ignore-removal .

# Commit the changes
git commit -m "Add new files and ignore deletions"

# Push to GitHub
git push origin main
```

### Key Points:
- **Deleted files locally won't be removed from the GitHub repository.**
- **Only new or modified files will be added to GitHub.**
- If you ever need to explicitly remove files from GitHub, you can do so by manually staging deletions using `git rm` or by reverting your `--ignore-removal` setting.

This setup gives you control over when files are removed from the GitHub repository and prevents accidental deletion.