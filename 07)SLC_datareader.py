import vtk

InputFilename, iso_value = 'fileName', 72.0
colors = vtk.vtkNamedColors()

#--------------data Source----------
# vtkSLCReader to read.
reader = vtk.vtkSLCReader()
reader.SetFileName(InputFilename)
reader.Update()

#------------Contour----------------

# Implementing Marching Cubes Algorithm to create the surface using vtkContourFilter object.
contourFilter = vtk.vtkContourFilter()
contourFilter.SetInputConnection(reader.GetOutputPort())
# Change the range(2nd and 3rd Paramater) based on your
# requirement. recomended value for 1st parameter is above 1
# contourFilter.GenerateValues(5, 80.0, 100.0)
contourFilter.SetValue(0, iso_value)

outliner = vtk.vtkOutlineFilter()
outliner.SetInputConnection(reader.GetOutputPort())
outliner.Update()

#------------Mapper----------------
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(contourFilter.GetOutputPort())
mapper.SetScalarVisibility(0)

#------------Actor----------------
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetDiffuse(0.8)
actor.GetProperty().SetDiffuseColor(colors.GetColor3d('Ivory'))
actor.GetProperty().SetSpecular(0.8)
actor.GetProperty().SetSpecularPower(120.0)

#-----------Renderer & rendering window---------------
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(colors.GetColor3d('SlateGray'))

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(500, 500)

#------------Interactor--------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()

