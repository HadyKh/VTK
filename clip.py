import vtk


def clip(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()
    main_polydata =  reader.GetOutput()

    lens_clip  = vtk.vtkClipDataSet()
    lens_clip .SetInputData(main_polydata)
    lens_clip .SetValue(1)
    lens_clip .GenerateClipScalarsOff()
    lens_clip .Update()

    polydata_points = lens_clip .GetOutput()

    geometry = vtk.vtkGeometryFilter()
    geometry.SetInputData(polydata_points)
    geometry.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(lens_clip.GetOutputPort())
    mapper.SetScalarRange(lens_clip.GetOutput().GetScalarRange())

    #---------------actor---------------
    actor2 = vtk.vtkActor()
    actor2.SetMapper(mapper)
    actor2.GetProperty().SetColor(1, 0, 0)

    #---------------rendering window & renderer---------------
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(0.5, 0.5, 0.5)
    renderer.AddActor(actor2)

    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetSize(500, 500)
    renderWindow.AddRenderer(renderer)
    renderWindow.Render()

    #---------------render Window Interactor---------------
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renderWindow)
    iren.Start()
