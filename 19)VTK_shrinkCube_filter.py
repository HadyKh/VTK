import vtk

colors = vtk.vtkNamedColors()

#-------Data source--------
cube = vtk.vtkCubeSource()

#-----Adding filter-------------
shrink = vtk.vtkShrinkFilter()
shrink.SetInputConnection(cube.GetOutputPort())
shrink.SetShrinkFactor(0.9)

#-----------mapper---------------
cubeMapper = vtk.vtkDataSetMapper()
cubeMapper.SetInputConnection(shrink.GetOutputPort())



#---------------actor---------------
cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.GetProperty().SetColor(1, 0, 0)
cubeActor.GetProperty().EdgeVisibilityOn()

back = vtk.vtkProperty()
back.SetColor(colors.GetColor3d('Tomato'))

cubeActor.SetBackfaceProperty(back)

#---------------rendering window & renderer---------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(cubeActor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.SetSize(500, 500)
renderWindow.AddRenderer(renderer)
renderWindow.Render()

#---------------render Window Interactor---------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()
