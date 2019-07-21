MODULES = ['user', 'auth', 'supplier', 'planner', 'music', 'food', 'flower']


def init_api(api):
    from importlib import import_module

    for module_name in MODULES:
        import_module('.{}'.format(module_name), package=__name__).init_api(api)
