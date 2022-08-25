import math
import vtk

p0 = (0, 0, 0)
p1 = (1, 1, 1)

squaredDist = vtk.vtkMath.Distance2BetweenPoints(p0, p1)
dist = math.sqrt(squaredDist)

print(f'p0 = {p0} & p1 = {p1}\ndistance squared = {squaredDist}\ndistance = {dist}')