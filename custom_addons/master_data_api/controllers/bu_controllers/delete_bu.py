from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):

    @http.route('/api/business_unit/delete', type='json', auth='public', methods=['POST'], csrf=False)
    def delete_business_unit(self, **kwargs):

        data = request.jsonrequest or {}

        if 'params' in data:
            data = data['params']

        business_code = data.get("business_code")

        # ❌ Must provide business_code
        if not business_code:
            return {
                "status": "error",
                "message": "business_code is required"
            }

        # 🔍 Find record
        record = request.env['business.unit'].sudo().search([
            ('business_code', '=', business_code)
        ], limit=1)

        # ❌ Not found
        if not record:
            return {
                "status": "error",
                "message": f"No Business Unit found with code '{business_code}'"
            }

        # ✅ Delete
        record.unlink()

        return {
            "status": "success",
            "message": f"Business Unit '{business_code}' deleted successfully"
        }