# ECE650 : Assignment 0

Replace FIRST_NAME, LAST_NAME, WATIAM, and STUDENT_ID, EMAIL in
`user.yml` by your first and last name, WatIAM id, student number, and
email, respectively. Use plain ASCII characters as much as possible.

Do not change the format of the file. We will parse it
automatically. Only enter the information requested.

Commit your changes and submit on GitLab.

You can pull from this upstream code repo by adding it as a remote
repository to your GitLab Repository. If you are using the git command
line interface, you may wish to use the follow command:

```shell
git remote add <REPO-NAME> "URL-TO-UPSTREAM-ON-GITLAB"
```

Where it is recommended to name <REPO-NAME> as 'upstream'
for consistency. The URL can be obtained from GitLab.
Then the upstream code for each assignment can be obtained through:

```shell
git fetch <REPO-NAME>
```

Or

```shell
git fetch <REPO-NAME> <BRANCH-NAME>
```

Which in this case is the following:

```shell
git pull upstream master
```

Which fetches the code. Then merge the code with your current branch:

```shell
git merge <BRANCH-NAME>
```

Which in this case is:

```shell
git merge upstream/master
```

Once you have made changes, and have added them with a command such
as the following:

```shell
git add <NAME-OF-FILE>
```

A 'commit' will need to be made. Note that a 'commit' contains the changes.

```shell
git commit -m "ENTER A COMMIT MESSAGE HERE. THIS IS FOR YOUR OWN REFERENCE"
```

Note that the message is optional. It is a message for your own clarity.
However, you may find it useful to include meaningful messages
in case you need to refer to previous, older commits.

```shell
git commit
```

Once you have a commit ready, it can be pushed onto the GitLab
Repository through the following

```shell
git push origin master
```

*NOTE* It is ~STRONGLY~ recommended that you go to GitLab and check to
make sure your code is visible on GitLab after pushing.

Note that you can see all of the modified files with:

```shell
git status
```



If you are using git at the command line, it may be useful to configure
git on the command line through the following commands.

```shell
git config --global user.name "FIRSTNAME LASTNAME"
git config --global user.email "USERNAME@uwaterloo.ca"
git config --global push.default simple
git config --global color.ui "true" 
```

If you wish to practice using git, you may try the ["Learn Git Branching"](https://learngitbranching.js.org/) on the [https://try.github.io/](https://try.github.io/) webpage.
