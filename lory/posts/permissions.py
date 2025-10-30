from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    오브젝트를 작성한 사람만 수정/삭제 가능.
    읽기(GET)는 모두 허용.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS 같은 읽기 요청은 누구나 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 작성자만 수정/삭제 가능
        return obj.creator.id == request.user.id
