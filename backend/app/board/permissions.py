from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

# class IsClubLeaderOrReadOnly(permissions.BasePermission):
#     def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # leader = obj.meeting.leader
#         # return request.user == leader
#         return request.user == getattr(obj, "meeting.leader", None)


class IsWriterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Any) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        # return request.user == obj.writer
        return request.user == getattr(obj, "writer", None)
