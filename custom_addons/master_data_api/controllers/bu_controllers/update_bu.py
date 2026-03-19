from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):

    @http.route('/api/business_unit/update/<string:business_code>', type='json', auth='public', methods=['POST'], csrf=False)
    def update_business_unit(self,business_code, **kwargs):

        data = request.jsonrequest or {}

        if 'params' in data:
            data = data['params']

        # business_code = data.get("business_code")

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

        # ✅ Update only provided fields
        vals = {}

        for field in [
            "name",
            "business_type",
            "company_id",
            "bu_br_div_loc",
            "holding_business_id"
        ]:
            if field in data:
                vals[field] = data[field]

        record.write(vals)

        return {
            "status": "success",
            "message": f"Business Unit '{business_code}' updated successfully"
        }