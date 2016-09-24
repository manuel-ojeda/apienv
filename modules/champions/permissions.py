from rest_framework import permissions

class ApiUserPermissions(permissions.BasePermission):
	SELECTED_GROUP = "Los chilos"

	def has_permissions(self, request, view):
		if request.user.groups.filter(
			name=self.SELECTED_GROUP
			) and request.method == 'GET':
			return True
		return False