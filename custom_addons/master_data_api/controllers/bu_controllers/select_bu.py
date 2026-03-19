from odoo import http
from odoo.http import request
import json

class MyAPI(http.Controller):

    # @http.route('/api/business_unit/search', type='json', auth='public', methods=['POST'], csrf=False)
    # def search_business_unit(self, **kwargs):

    #     data = request.jsonrequest or {}

    #     if 'params' in data:
    #         data = data['params']

    #     keyword = data.get("business_code")

    #     if not keyword:
    #         return {
    #             "status": "error",
    #             "message": "business_code is required"
    #         }

    #     # 🔍 SEARCH with ilike
    #     records = request.env['business.unit'].sudo().search([
    #         ('business_code', 'ilike', keyword)
    #     ])

    #     # ❌ No result
    #     if not records:
    #         return {
    #             "status": "error",
    #             "message": f"No records found matching '{keyword}'"
    #         }

    #     # ✅ Return list
    #     result = []
    #     for r in records:
    #         result.append({
    #             "id": r.id,
    #             "name": r.name,
    #             "business_code": r.business_code
    #         })

    #     return {
    #         "status": "success",
    #         "count": len(result),
    #         "data": result
    #     }

    
    @http.route('/api/business_unit/select', type='json', auth='public', methods=['POST'], csrf=False)
    def get_business_unit(self, **kwargs):

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

        # 🔍 Search record
        record = request.env['business.unit'].sudo().search([
            ('business_code',"ilike", business_code)
        ], limit=1)

        # records = request.env['business.unit'].sudo().search([
        #     ('business_code', 'ilike', business_code)
        # ])

        # ❌ Not found
        if not record:
            return {
                "status": "error",
                "message": f"No Business Unit found with code '{business_code}'"
            }

        # ✅ Return data
        return {
            "status": "success",
            "data": {
                "id": record.id,
                "name": record.name,
                "business_code": record.business_code,
                "business_type": record.business_type,
                "company_id": record.company_id.id,
                "location_id": record.bu_br_div_loc.id,
                "warehouse_id": record.holding_business_id.id
            }
        }