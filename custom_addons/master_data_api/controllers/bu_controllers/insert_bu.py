from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):
    
    @http.route('/api/business_unit/insert', type='json', auth='public', methods=['POST'], csrf=False)
    def create_business_unit(self, **kwargs):

        data = request.jsonrequest or {}

        if 'params' in data:
            data = data['params']

        business_code = data.get("business_code")

        # 🔍 CHECK DUPLICATE
        existing = request.env['business.unit'].sudo().search([
            ('business_code', '=', business_code)
        ], limit=1)

        if existing:
            return {
                "status": "error",
                "message": f"Business Code '{business_code}' already exists",
                "existing_id": existing.id,
                "existing_name": existing.name
            }

        # ✅ CREATE IF NOT EXISTS
        vals = {
            "name": data.get("name"),
            "business_code": business_code,
            "business_type": data.get("business_type"),
            "company_id": data.get("company_id"),
            "bu_br_div_loc": data.get("bu_br_div_loc"),
            "holding_business_id": data.get("holding_business_id"),
        }

        record = request.env['business.unit'].sudo().create(vals)

        return {
            "status": "success",
            "id": record.id
        }
    