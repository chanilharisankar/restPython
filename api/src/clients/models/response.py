import json
from marshest.marshmodels import MarshModel

class ListUsersResponse(MarshModel):

    def __init__(self, page,per_page,total,total_pages,data):
        self.page=page
        self.per_page=per_page
        self.total=total
        self.total_pages=total_pages
        self.data=data

    @classmethod
    def _json_to_object(cls, serialized_str):
        response = None
        try:
            json_dict = json.loads(serialized_str.decode("utf-8"))
        except Exception as e:
            return (serialized_str)


class Data(MarshModel):
    def __init__(self,id,first_name,last_name,avatar):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.avatar=avatar


    @classmethod
    def _json_to_object(cls, serialized_str):
        if type(serialized_str) is dict:
            json_dict = serialized_str
        else:
            json_dict = json.loads(serialized_str.decode("utf-8"))
        try:
            response= Data(id=json_dict.get('id'),
                           first_name=json_dict.get('first_name'),
                           last_name=json_dict.get('last_name'),
                           avatar=json_dict.get('avatar'))
        except:
            return response

        return response

    @classmethod
    def _list_to_object(cls, dict_list):
        items = []
        for item in dict_list:
            item_obj = cls._json_to_object(item)
            items.append(item_obj)
        return items


















        



