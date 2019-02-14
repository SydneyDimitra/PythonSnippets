import maya.cmds as cmds

# -------UI--------#
result = cmds.promptDialog(
        title='Basic UI',
        message='Insert NameSpace',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')
# -------------------#

if result == 'OK':
    nSpace = cmds.promptDialog(query=True, text=True)
    build_layers(nSpace + ':')
