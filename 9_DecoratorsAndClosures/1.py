# From Fluent Python Chapter 9

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()
print(target)
