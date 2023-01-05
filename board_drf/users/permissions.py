from rest_framework import permissions

# get은 누구나, put,patch는 해당 유저만 
class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  #데이터에 영향을 안미치는 메소드 
            return True #트루 반환 
        return obj.user == request.user #데이터에 영향을 미치는 메소드 => 비교를 통해 반환처리
         
