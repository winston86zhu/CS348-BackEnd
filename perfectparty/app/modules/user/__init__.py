def init_api(api):
    base_url = '/user'

    from . import resources
    api.add_resource(resources.User, f'{base_url}')
