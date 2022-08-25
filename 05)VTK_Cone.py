import vtk

#-----data Source---------------
cone = vtk.vtkConeSource()

#--------Mapper----------
coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

#---------Actor---------------
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)
coneActor.GetProperty().SetColor(1, 0, 0)


#------------renderer & renderer window--------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(coneActor)

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.SetSize(500, 500)
rendererWindow.AddRenderer(renderer)
rendererWindow.Render()

#--------rendererWindowInteractor--------------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(rendererWindow)
iren.Start()