from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py")
@task
def test(ctx):
    ctx.run("python3 -m pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")