from pyramid.response import Response
from pyramid.view import view_config
import os
from pyramid.response import FileResponse

from sqlalchemy.exc import DBAPIError

from ..models import MyModel


@view_config(route_name='home')
def my_view(request):
    here = os.path.dirname(__file__)
    index = os.path.join(here, '..', '..', 'dist', 'index.html')
    return FileResponse(index)
