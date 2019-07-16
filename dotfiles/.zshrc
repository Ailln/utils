## 别名

# 系统
alias ll="ls -l"
alias la="ls -a"

# git
alias gs="git status"
alias ga="git add -a ."
alias gc="git commit"
alias gb="git branch"
alias gd="git diff"
alias gco="git checkout"
alias gp="git push"
alias gl="git pull"
alias gt="git tag"
alias gm="git merge"
alias gg="git log --graph --pretty=format:"%c(bold red)%h%creset -%c(bold yellow)%d%creset %s %c(bold green)(%cr) %c(bold blue)<%an>%creset" --abbrev-commit"
alias gcp="git cherry-pick"
alias gbg="git bisect good"
alias gbb="git bisect bad"

# ssh 自动续连
alias ssh="ssh -o serveraliveinterval=30"
alias scpr="rsync -p --rsh=ssh"