import vtk

#-----data Source---------------
planeSource = vtk.vtkPlaneSource()
planeSource.SetCenter(1.0, 0.0, 0.0)
planeSource.SetNormal(1.0, 0.0, 1.0)
planeSource.Update()

#--------Mapper----------
planeMapper = vtk.vtkPolyDataMapper()
planeMapper.SetInputData(planeSource.GetOutput())

#---------Actor---------------
planeActor = vtk.vtkActor()
planeActor.SetMapper(planeMapper)
planeActor.GetProperty().SetColor(1, 0, 0)

#------------renderer & renderer window--------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(planeActor)

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.SetSize(500, 500)
rendererWindow.AddRenderer(renderer)
rendererWindow.Render()

#--------rendererWindowInteractor--------------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(rendererWindow)
iren.Start()