def init_api(api):
    base_url = '/flowers'

    from . import resources
    api.add_resource(resources.FlowerResource, f'{base_url}')
