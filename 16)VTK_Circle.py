import vtk

#-----data Source---------------
circle = vtk.vtkRegularPolygonSource()
circle.GeneratePolygonOff()
circle.SetNumberOfSides(50)
circle.SetRadius(5.0)
circle.SetCenter(0.0, 0.0, 0.0)

#--------Mapper----------
circleMapper = vtk.vtkPolyDataMapper()
circleMapper.SetInputConnection(circle.GetOutputPort())

#---------Actor---------------
circleActor = vtk.vtkActor()
circleActor.SetMapper(circleMapper)
circleActor.GetProperty().SetColor(1, 0, 0)

#------------renderer & renderer window--------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(circleActor)

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.SetSize(500, 500)
rendererWindow.AddRenderer(renderer)
rendererWindow.Render()

#--------rendererWindowInteractor--------------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(rendererWindow)
iren.Start()