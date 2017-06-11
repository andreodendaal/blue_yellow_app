from pyramid.view import view_config
import blue_yellow_app.utils


@view_config(route_name='home', renderer="templates/index.pt")
def index(_):
    return extend_model({})


@view_config(route_name='box', renderer='templates/box_model.pt')
def box_model(_):
    return extend_model({})

@view_config(route_name='layout', renderer='templates/layout.pt')
def layout(_):
    return extend_model({})


def extend_model(model_dict):
    model_dict['build_cache_id'] = blue_yellow_app.utils.build_cache_id
    return model_dict



