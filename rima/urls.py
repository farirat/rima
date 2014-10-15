from importlib import import_module

def import_view(view_path):
	module_name, view_class = view_path.rspilt(".", 1)
	import_module()

urls_map = []