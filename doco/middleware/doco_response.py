from rest_framework.renderers import JSONRenderer


class DocoJsonResponse(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        _data = {
           'message': '',
           'success': False,
           'status': renderer_context['response'].status_code,
           'code': '',
           'errors': [],
        }

        if not renderer_context['response'].exception:
            _data['message'] = 'success'
            _data['code'] = 'success'
            _data['success'] = True
            _data['data'] = data
        else:
            _data['message'] = 'failure'
            _data['code'] = 'failure'
            _data['errors'] = data if isinstance(data, list) else [data]

        return super(DocoJsonResponse, self).render(_data, accepted_media_type, renderer_context)
