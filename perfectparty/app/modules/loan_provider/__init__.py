def init_api(api):
    base_url = '/loan_provider'

    from . import resources
    api.add_resource(resources.LPResource, f'{base_url}')
