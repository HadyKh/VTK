import vtk

InputFilename = 'fileName'
colors = vtk.vtkNamedColors()

#--------------data Source----------
reader = vtk.vtkSTLReader()
reader.SetFileName(InputFilename)
reader.Update()

#------------Mapper----------------
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())
mapper.SetScalarVisibility(0)

#------------Actor----------------
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetDiffuse(0.8)
actor.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))
actor.GetProperty().SetSpecular(0.3)
actor.GetProperty().SetSpecularPower(60.0)

#-----------Renderer & rendering window---------------
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(colors.GetColor3d('SlateGray'))

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(500, 500)
renderWindow.Render()

#------------Interactor--------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()
