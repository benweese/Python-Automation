workflow "Push" {
  resolves = ["Setup Python"]
  on = "push"
}

action "Checkout" {
  uses = "actions/checkout@v1"
}

action "Setup Python" {
  uses = "actions/setup-python@v1"
  needs = ["Checkout"]
}
