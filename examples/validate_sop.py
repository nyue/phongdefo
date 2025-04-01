import hou

# env HOUDINI_DSO_PATH="`pwd`/build/ubuntu-h200-debug;@/dso_^;@/dso" hython examples/validate_sop.py
obj = hou.node("/obj")
geo = obj.createNode("geo", run_init_scripts=False)
sphere = geo.createNode("sphere")
deformer = geo.createNode("tet_embedded_deform")
hou.hipFile.save(file_name='demo.hip')
