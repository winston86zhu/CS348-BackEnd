def init_api(api):
    base_url = '/auth'

    from . import resources
    api.add_resource(resources.AuthResource, f'{base_url}')
