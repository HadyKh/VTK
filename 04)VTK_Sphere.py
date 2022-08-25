import vtk

#-----data Source---------------
sphere = vtk.vtkSphereSource()

#--------Mapper----------
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphere.GetOutputPort())

#---------Actor---------------
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)
sphereActor.GetProperty().SetColor(1, 0, 0)


#------------renderer & renderer window--------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(sphereActor)

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.SetSize(500, 500)
rendererWindow.AddRenderer(renderer)
rendererWindow.Render()

#--------rendererWindowInteractor--------------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(rendererWindow)
iren.Start()