import vtk

#-----data Source--------------- Create the lines
linespolydata = vtk.vtkPolyData()

#----Create a vtkPoints container and store the points in it
origin = [0.0, 0.0, 0.0]
p0 = [1.0, 0.0, 0.0]
p1 = [0.0, 1.0, 0.0]
pts = vtk.vtkPoints()
pts.InsertNextPoint(origin)
pts.InsertNextPoint(p0)
pts.InsertNextPoint(p1)

linespolydata.SetPoints(pts) #add the points to the line container

#----Create the first line (between Origin and P0)
line0 = vtk.vtkLine() 
line0.GetPointIds().SetId(0, 0)  # the second 0 is the index of the Origin in linesPolyData's points
line0.GetPointIds().SetId(1, 1)  # the second 1 is the index of P0 in linesPolyData's points
#---Create the second line (between Origin and P1)
line1 = vtk.vtkLine()
line1.GetPointIds().SetId(0, 0)  # the second 0 is the index of the Origin in linesPolyData's points
line1.GetPointIds().SetId(1, 2)  # 2 is the index of P1 in linesPolyData's points

#------Store the lines in a cell array container
lines = vtk.vtkCellArray()
lines.InsertNextCell(line0)
lines.InsertNextCell(line1)
#-----Add the lines to the lines container
linespolydata.SetLines(lines)

#------Coloring the lines
namedColors = vtk.vtkNamedColors()
colors = vtk.vtkUnsignedCharArray()
colors.SetNumberOfComponents(3)
try:
    colors.InsertNextTupleValue(namedColors.GetColor3ub("Tomato"))
    colors.InsertNextTupleValue(namedColors.GetColor3ub("Mint"))
except AttributeError:
    # For compatibility with new VTK generic data arrays.
    colors.InsertNextTypedTuple(namedColors.GetColor3ub("Tomato"))
    colors.InsertNextTypedTuple(namedColors.GetColor3ub("Mint"))
linespolydata.GetCellData().SetScalars(colors)

#--------Mapper----------
linesMapper = vtk.vtkPolyDataMapper()
linesMapper.SetInputData(linespolydata)

#---------Actor---------------
linesActor = vtk.vtkActor()
linesActor.SetMapper(linesMapper)
linesActor.GetProperty().SetColor(1, 0, 0)


#------------renderer & renderer window--------------
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.5, 0.5, 0.5)
renderer.AddActor(linesActor)

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.SetSize(500, 500)
rendererWindow.AddRenderer(renderer)
rendererWindow.Render()

#--------rendererWindowInteractor--------------------
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(rendererWindow)
iren.Start()
