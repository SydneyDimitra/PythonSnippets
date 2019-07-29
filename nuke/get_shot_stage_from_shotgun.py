import os 
text_node = nuke.thisNode()
query_node, stage_prop_node = text_node.dependencies()

show = os.getenv('SHOW')
shot_name = query_node['shot'].value()

from shotgun import _utils
stage = _shot.ShotgunShot(show, shot_name).sg_current_stage["name"]

# Use this to get the knob name for your stage color knob
# stage.replace(' ', '_').replace('-', '_')

knob_name = stage.replace(' ', '_').replace('-', '_')

if not knob_name in stage_prop_node.knobs():
    color_value = stage_prop_node["default_colour"].toScript()
    text_node['color'].fromScript(color_value)
else:
    color_value = stage_prop_node[knob_name].toScript()
    text_node['color'].fromScript(color_value)
    
