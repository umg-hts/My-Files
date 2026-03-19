from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):

    @http.route('/api/partners', type='json', auth='public', methods=['POST'], csrf=False)
    def get_partners(self, **kwargs):
        partners = request.env['res.partner'].sudo().search([], limit=5)
        
        data = []
        for p in partners:
            data.append({
                "id": p.id,
                "name": p.name
            })
        
        return data