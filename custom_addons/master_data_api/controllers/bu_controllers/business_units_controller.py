from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):

    
    @http.route('/api/business_unit/create', type='json', auth='public', methods=['POST'], csrf=False)
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
    
    @http.route('/api/business_unit/list', type='json', auth='public', methods=['POST'], csrf=False)
    def get_business_units(self, **kwargs):
        records = request.env['business.unit'].sudo().search([], limit=10)

        data = []
        for r in records:
            data.append({
                "id": r.id,
                "name": r.name,
                "business_code": r.business_code,
                "business_type": r.business_type
            })

        return data
    
    @http.route('/api/business_unit/update', type='json', auth='public', methods=['POST'], csrf=False)
    def update_business_unit(self, **kwargs):

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