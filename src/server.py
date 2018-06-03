from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
from urllib.parse import urlparse
from urllib.parse import parse_qs
import re
import simplejson
from db_mock import *
from controllers.users_controller import *
from controllers.rents_controller import *


db = DbMock()
user_controller = UsersController(db)
rent_controller = RentsController(db)


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # get users
            if None != re.search('/api/v1/users$', self.path):
                self._render_response(user_controller.index(), 200)

            # get user
            elif None != re.search('/api/v1/users/\-?\d+$', self.path):
                self._render_response(
                    user_controller.show(int(self._id())), 200)

            # get user rents
            elif None != re.search('/api/v1/users/\-?\d+/rents$', self.path):
                self._render_response(
                    rent_controller.get_user_rents(int(self._id())), 200)

            # get user rent
            elif None != re.search('/api/v1/users/\-?\d+/rents/\-?\d+$', self.path):
                self._render_response(
                    rent_controller.get_user_rent(int(self._ids()[0]), int(self._ids()[1])), 200)

            else:
                self._render_invalid_route_response()
        except NameError as e:
            self._render_not_found_response(e)
        except Exception as e:
            self._render_bad_request_response(e)
        return

    def do_POST(self):
        try:
            # create user rent
            if None != re.search('/api/v1/users/\-?\d+/rents$', self.path):
                rent_controller.user_rent_a_bike(self._id(), self._params())
                self._render_empty_response()

            # close user rent
            elif None != re.search('/api/v1/users/\-?\d+/rents/\-?\d+$', self.path):
                rent_controller.close_user_rent(
                    int(self._ids()[0]), int(self._ids()[1]))
                self._render_empty_response()

            else:
                self._render_invalid_route_response()

        except NameError as e:
            self._render_not_found_response(e)
        except Exception as e:
            self._render_bad_request_response(e)
        return

    ### PARSER ###
    def _id(self):
        return int(self._ids()[0])

    def _ids(self):
        return re.findall(r'\b\d+\b', self.path)

    def _params(self):
        content_length = int(self.headers['Content-Length'])
        return simplejson.loads(self.rfile.read(content_length))

    def _url_params(self):
        return urlparse(self.path)

    ### RENDERS ###
    def _render_response(self, hash, status):
        return self.wfile.write(self._render({'response': hash}, status))

    def _render_bad_request_response(self, exception):
        hash = {'error': 'bad_request',
                'message': str(exception)}
        return self._render_response(hash, 400)

    def _render_not_found_response(self, exception):
        hash = {'error': 'not_found',
                'message': str(exception)}
        return self._render_response(hash, 404)

    def _render_invalid_route_response(self):
        hash = {'error': 'invalid_route',
                'message': 'The route does not exist'}
        return self._render_response(hash, 403)

    def _render_empty_response(self):
        hash = {'status': 'successfull'}
        return self._render_response(hash, 200)

    def _render(self, hash, status):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = BytesIO()
        response.write(
            bytes(str(simplejson.dumps(hash, sort_keys=True, indent=4 * ' ')), "utf-8"))
        return response.getvalue()
