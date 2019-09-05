workflow "Main Workflow" {
  on = "push"
  resolves = ["Pytest"]
}

action "setup-python" {
  uses = "setup-python"
  secrets = ["GITHUB_TOKEN"]
}

action "Install dependencies" {
  uses = "Install-dependencies"
  needs = ["setup-python"]
  secrets = ["GITHUB_TOKEN"]
}

action "Lint" {
  uses = "flake8"
  needs = ["Install dependencies"]
  secrets = ["GITHUB_TOKEN"]
}

action "Pytest" {
  uses = "Pytest"
  needs = ["Lint"]
  secrets = ["GITHUB_TOKEN"]
}
