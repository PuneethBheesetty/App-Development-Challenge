import bpy;

Class option_Panel(bpy.types.Panel):
	bl_label = "Main option panel";
	bl_idname = "ID_optionpanel";
	bl_space_type = 'VIEW_3D';
	bl_region_type = 'UI';
	bl_category = "Options";
	
def draw(self, context):
	layout = self.layout;
	row = layout.row();
	row.label(text = "Filter by color", icon = "THERMOMETER");
	row.operator(filter_color); # make filter_color
	
if __name__ == "__main__":
	bpy.utils.register_class(option_panel);
	
