import vtk

InputFilename, nodal_var = 'fileName', ''
colors = vtk.vtkNamedColors()

#--------------data Source----------
reader = vtk.vtkExodusIIReader()
reader.SetFileName(InputFilename)
reader.UpdateInformation()
reader.SetTimeStep(10)
reader.SetAllArrayStatus(vtk.vtkExodusIIReader.NODAL, 1)  # enables all NODAL variables
reader.Update()

#------------Create Geometry------------
geometry = vtk.vtkCompositeDataGeometryFilter()
geometry.SetInputConnection(0, reader.GetOutputPort(0))
geometry.Update()

#------------Mapper----------------
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(geometry.GetOutputPort())
mapper.SelectColorArray(nodal_var)
mapper.SetScalarModeToUsePointFieldData()
mapper.InterpolateScalarsBeforeMappingOn()

#------------Actor----------------
actor = vtk.vtkActor()
actor.SetMapper(mapper)


#-----------Renderer & rendering window---------------
renderer = vtk.vtkRenderer()
renderer.AddViewProp(actor)
renderer.SetBackground(colors.GetColor3d('DimGray'))

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(600, 600)
renderWindow.SetWindowName('ReadExodusData')
renderWindow.Render()

#------------Interactor--------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renderWindow)
iren.Start()