import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkRenderingCore import (vtkActor, vtkPolyDataMapper, vtkRenderWindow, vtkRenderWindowInteractor, vtkRenderer)


# colors = vtkNamedColors()
# Set the background color.
# bkg = map(lambda x: x / 255.0, [26, 51, 102, 255])
# colors.SetColor("BkgColor", *bkg)

# ---------data source-----------------
# This creates a polygonal cylinder model with eight circumferential
# facets.
cylinder = vtkCylinderSource()
# cylinder.SetResolution(8)

#------------Mapper--------------------
# The mapper is responsible for pushing the geometry into the graphics
# library. It may also do color mapping, if scalars or other
# attributes are defined.
cylinderMapper = vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())

#------------------Actor---------------
# The actor is a grouping mechanism: besides the geometry (mapper), it
# also has a property, transformation matrix, and/or texture map.
# Here we set its color and rotate it -22.5 degrees.
cylinderActor = vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(1, 0, 0)#colors.GetColor3d("Tomato"))
# cylinderActor.RotateX(30.0)
# cylinderActor.RotateY(-45.0)


#--------------Renderer---------------------
# Create the graphics structure. The renderer renders into the render
# window. The render window interactor captures mouse events and will
# perform appropriate camera or actor manipulation depending on the
# nature of the events.
ren = vtkRenderer()
ren.SetBackground(0.5, 0.5, 0.5)#colors.GetColor3d("BkgColor"))
ren.AddActor(cylinderActor)

renWin = vtkRenderWindow()
renWin.SetSize(300, 300)
renWin.AddRenderer(ren)
renWin.Render()
# renWin.SetWindowName('CylinderExample')


# This allows the interactor to initalize itself. It has to be
# called before an event loop.
iren = vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
# iren.Initialize()
# Start the event loop.
iren.Start()

# We'll zoom in a little by accessing the camera and invoking a "Zoom"
# method on it.
# ren.ResetCamera()
# ren.GetActiveCamera().Zoom(1.5)



