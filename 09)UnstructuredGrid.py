import vtk

InputFilename = 'fileName'
colors = vtk.vtkNamedColors()

#--------------data Source----------
reader = vtk.vtkXMLUnstructuredGridReader()
reader.SetFileName(InputFilename)
reader.Update()

#------------Mapper----------------
mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(reader.GetOutput())
mapper.ScalarVisibilityOff()

#------------Actor----------------
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().EdgeVisibilityOn()
actor.GetProperty().SetLineWidth(2.0)
actor.GetProperty().SetColor(colors.GetColor3d("MistyRose"))
backface = vtk.vtkProperty()
backface.SetColor(colors.GetColor3d('Tomato'))
actor.SetBackfaceProperty(backface)

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