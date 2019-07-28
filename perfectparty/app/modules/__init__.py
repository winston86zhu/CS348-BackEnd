
MODULES = ['user', 'auth', 'event', 'order', 'location', 'loan_provider', 'supply']

def init_api(api):
    from importlib import import_module

    for module_name in MODULES:
        print(f'adding {module_name} to api')
        import_module('.{}'.format(module_name), package=__name__).init_api(api)
