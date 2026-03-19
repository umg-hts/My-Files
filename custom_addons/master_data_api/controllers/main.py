from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):

    @http.route('/api/test', type='json', auth='public', methods=['POST'], csrf=False)
    def test_api(self, **kwargs):
        return {
            "status": "success",
            "message": "API is working!"
        }