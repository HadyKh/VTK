import vtk

InputFilename = 'fileName'
colors = vtk.vtkNamedColors()

#--------------data Source----------
reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName(InputFilename)
reader.Update()

#------------Mapper----------------
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

#------------Actor----------------
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(colors.GetColor3d("MistyRose"))

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