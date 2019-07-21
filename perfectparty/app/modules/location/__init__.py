def init_api(api):
    base_url = '/location'

    from . import resources
    api.add_resource(resources.LocationResource, f'{base_url}')
