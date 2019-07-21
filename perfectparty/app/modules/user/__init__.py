def init_api(api):
    base_url = '/supply'

    from . import resources
    api.add_resource(resources.UserResource, f'{base_url}')
