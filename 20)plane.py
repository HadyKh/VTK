import vtk

plane = vtk.vtkPlaneSource()
plane.SetNormal(1,1,1)
plane.SetCenter(0,0,0)
plane.Update()

planeMapper = vtk.vtkPolyDataMapper()
planeMapper.SetInputData(plane.GetOutput())

planeActor = vtk.vtkActor()
planeActor.SetMapper(planeMapper)

renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(planeActor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer)
renderWindow.Render()

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()
