from run_expr import run_expr

namelist = [('news20.scale', 20, 62060), ('aloi.scale', 1000, 128), ('sector.scale', 105, 55197)]

for args in namelist:
    run_expr(*args, 150)
