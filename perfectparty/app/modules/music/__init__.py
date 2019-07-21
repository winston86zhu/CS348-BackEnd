def init_api(api):
    base_url = '/musics'

    from . import resources
    api.add_resource(resources.MusicResource, f'{base_url}')
