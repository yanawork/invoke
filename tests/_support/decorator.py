from invoke.task import task


@task(aliases=('bar',))
def foo():
    pass

@task(default=True)
def biz():
    pass

@task(positional=('pos',))
def one_positional(pos, nonpos):
    pass

@task(positional=('pos1', 'pos2'))
def two_positionals(pos1, pos2, nonpos):
    pass

@task(positional=('second', 'first'))
def swapped_order_positionals(first, second, nonpos):
    pass
