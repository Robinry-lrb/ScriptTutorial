import math
import clr

clr.AddReference("System.Drawing")
from System.Drawing import Color
from System import String
from System.Collections.Generic import List
from System.Collections.Generic import Dictionary

import SpaceClaim
from SpaceClaim.Api.V18 import Window
from SpaceClaim.Api.V18 import InteractionMode
from SpaceClaim.Api.V18 import Document 
from SpaceClaim.Api.V18 import IDocObject 
from SpaceClaim.Api.V18 import DocObject 
from SpaceClaim.Api.V18 import ImportOptions 
from SpaceClaim.Api.V18 import MixedImportResolution 
from SpaceClaim.Api.V18 import AnalysisType 
from SpaceClaim.Api.V18 import ExportOptions
from SpaceClaim.Api.V18 import StlExportFormat 
from SpaceClaim.Api.V18 import StlFileGranularity 
from SpaceClaim.Api.V18 import Part
from SpaceClaim.Api.V18 import IPart
from SpaceClaim.Api.V18 import Component
from SpaceClaim.Api.V18 import IComponent
from SpaceClaim.Api.V18 import Group
from SpaceClaim.Api.V18 import IGroup
from SpaceClaim.Api.V18 import DrawingViewStyle
from SpaceClaim.Api.V18 import MidSurfaceAspect
from SpaceClaim.Api.V18 import CoordinateAxis
from SpaceClaim.Api.V18 import ICoordinateAxis
from SpaceClaim.Api.V18 import CoordinateSystem
from SpaceClaim.Api.V18 import ICoordinateSystem
from SpaceClaim.Api.V18 import DesignBody
from SpaceClaim.Api.V18 import IDesignBody 
from SpaceClaim.Api.V18 import DesignFace
from SpaceClaim.Api.V18 import IDesignFace 
from SpaceClaim.Api.V18 import DesignEdge
from SpaceClaim.Api.V18 import IDesignEdge  
from SpaceClaim.Api.V18 import DesignCurve
from SpaceClaim.Api.V18 import IDesignCurve
from SpaceClaim.Api.V18 import DesignMesh
from SpaceClaim.Api.V18 import IDesignMesh
from SpaceClaim.Api.V18 import DesignMeshRegion
from SpaceClaim.Api.V18 import IDesignMeshRegion
from SpaceClaim.Api.V18 import DesignMeshTopology
from SpaceClaim.Api.V18 import IDesignMeshTopology
from SpaceClaim.Api.V18 import CircularSense
from SpaceClaim.Api.V18 import MixedImportResolution
from SpaceClaim.Api.V18 import AnalysisType
from SpaceClaim.Api.V18 import IDatumLine
from SpaceClaim.Api.V18 import DatumLine
from SpaceClaim.Api.V18 import IDatumPlane
from SpaceClaim.Api.V18 import DatumPlane
from SpaceClaim.Api.V18 import IDatumPoint
from SpaceClaim.Api.V18 import DatumPoint
from SpaceClaim.Api.V18 import IBeam
from SpaceClaim.Api.V18 import ICurvePoint
from SpaceClaim.Api.V18 import CurvePoint
from SpaceClaim.Api.V18 import IDesignAxis
from SpaceClaim.Api.V18 import DesignAxis
from SpaceClaim.Api.V18 import ISectionCurve
from SpaceClaim.Api.V18 import SectionCurve
from SpaceClaim.Api.V18 import IWireCurve
from SpaceClaim.Api.V18 import WireCurve
from SpaceClaim.Api.V18 import IHole

from SpaceClaim.Api.V18.Modeler import Body
from SpaceClaim.Api.V18.Modeler import Edge
from SpaceClaim.Api.V18.Modeler import Facet
from SpaceClaim.Api.V18.Modeler import MeshFace
from SpaceClaim.Api.V18.Modeler import MeshEdge
from SpaceClaim.Api.V18.Modeler import MeshVertex

from SpaceClaim.Api.V18.Geometry import Direction 
from SpaceClaim.Api.V18.Geometry import IBounded 
from SpaceClaim.Api.V18.Geometry import Box 
from SpaceClaim.Api.V18.Geometry import Curve
from SpaceClaim.Api.V18.Geometry import CurveEvaluation
from SpaceClaim.Api.V18.Geometry import Point
from SpaceClaim.Api.V18.Geometry import PointCurve
from SpaceClaim.Api.V18.Geometry import ProceduralCurve
from SpaceClaim.Api.V18.Geometry import Line 
from SpaceClaim.Api.V18.Geometry import Helix 
from SpaceClaim.Api.V18.Geometry import Cylinder 
from SpaceClaim.Api.V18.Geometry import Sphere 
from SpaceClaim.Api.V18.Geometry import Torus 
from SpaceClaim.Api.V18.Geometry import Plane
from SpaceClaim.Api.V18.Geometry import Circle 
from SpaceClaim.Api.V18.Geometry import Parameterization 
from SpaceClaim.Api.V18.Geometry import Geometry 
from SpaceClaim.Api.V18.Geometry import NurbsSurface 
from SpaceClaim.Api.V18.Geometry import ProceduralSurface
from SpaceClaim.Api.V18.Geometry import Surface
from SpaceClaim.Api.V18.Geometry import SurfaceEvaluation
from SpaceClaim.Api.V18.Geometry import Space 
from SpaceClaim.Api.V18.Geometry import ITrimmedSpace 
from SpaceClaim.Api.V18.Geometry import Cone 
from SpaceClaim.Api.V18.Geometry import Ellipse
from SpaceClaim.Api.V18.Geometry import Polygon 
from SpaceClaim.Api.V18.Geometry import ITrimmedCurve
from SpaceClaim.Api.V18.Geometry import ITrimmedSurface
from SpaceClaim.Api.V18.Geometry import CurveSegment
from SpaceClaim.Api.V18.Geometry import LineSegment
from SpaceClaim.Api.V18.Geometry import Profile
from SpaceClaim.Api.V18.Geometry import NurbsCurve
from SpaceClaim.Api.V18.Geometry import Interval
from SpaceClaim.Api.V18.Geometry import Matrix
from SpaceClaim.Api.V18.Geometry import Vector
from SpaceClaim.Api.V18.Geometry import VectorUV
from SpaceClaim.Api.V18.Geometry import Frame
from SpaceClaim.Api.V18.Geometry import BoxUV
from SpaceClaim.Api.V18.Geometry import DirectionUV
from SpaceClaim.Api.V18.Geometry import Accuracy
from SpaceClaim.Api.V18.Geometry import PointUV

from SpaceClaim.Api.V18.Scripting.Commands import Point2D 

from SpaceClaim.Api.V18.Scripting.Helpers import WindowHelper
from SpaceClaim.Api.V18.Scripting.Helpers import ComponentHelper
from SpaceClaim.Api.V18.Scripting.Helpers import DocumentHelper
from SpaceClaim.Api.V18.Scripting.Helpers import ViewHelper
from SpaceClaim.Api.V18.Scripting.Helpers import ColorHelper
from SpaceClaim.Api.V18.Scripting.Helpers import Beta
from SpaceClaim.Api.V18.Scripting.Helpers import ApplicationHelper
from SpaceClaim.Api.V18.Scripting.Helpers.Units import *
from SpaceClaim.Api.V18.Scripting.Helpers import *

from SpaceClaim.Api.V18.Scripting.Managers import ScriptEventManager

#from SpaceClaim.Api.V18.Scripting import ScriptTool
#from SpaceClaim.Api.V18.Scripting import MeshBuilder

from SpaceClaim.Api.V18.Scripting.Selection import *
from SpaceClaim.Api.V18.Scripting.PersistenceMaps import *
from SpaceClaim.Api.V18.Scripting.PowerSelection import *
from SpaceClaim.Api.V18.Scripting.Commands import *
from SpaceClaim.Api.V18.Scripting.Commands.CommandOptions import *
from SpaceClaim.Api.V18.Scripting.Commands.CommandResults import *
from SpaceClaim.Api.V18.Scripting.Commands.CommandData import *
from SpaceClaim.Api.V18.Scripting.Commands.ProblemAreas import *
from SpaceClaim.Api.V18.Scripting.Internal import SpaceClaimTesting
from SpaceClaim.Api.V18.Scripting.Internal import ValidationExecption
from SpaceClaim.Api.V18.Scripting.ReplayBlocks import ReplayBlockHelper
from SpaceClaim.Api.V18.Scripting.Internal.ReplayBlocks import ReplayInputHelper

clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.DesignEdgeExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.DesignFaceExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.DesignCurveExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.PartExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.MidsurfaceAspectExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.ComponentExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.DesignMeshExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.DesignBodyExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.DocObjectExtensions)
clr.ImportExtensions(SpaceClaim.Api.V18.Scripting.Extensions.HasNameExtensions)

def GetID(object):
	monstr = object.Moniker.ToString()
	s = monstr.split(":")
	t = s[1].split('"')
	return t[0]
	
def GetObject(id):
	entity = GetPart().Find(id)
	if entity is None:
		return None

	return entity
			
def GetActiveWindow():
	window = Window.ActiveWindow
	if window is None:
		return None

	return window

def GetRootPart():
	''' '''
	return DocumentHelper.GetRootPart()

def GetActivePart():
	''' '''
	return DocumentHelper.GetActivePart()

	
def CloseWindow():
	Window.ActiveWindow.Close()
		
def SelectionDebug(sel):
	objects = sel.GetDocObjects()
	for ob in objects:
		ObjectDebug(ob)

def ObjectDebug(object):
	print type(object)
	print "	ID = " + str(GetID(object))
	if type(object) is DesignBody:
		print "	Body Name: " + object.Name
		print "	Faces = " + str(object.Faces.Count)
		print "	Edges = " + str(object.Edges.Count)
	elif type(object) is DesignFace:
		surface = object.Shape.Geometry
		if type(surface) is Cylinder:
			print "	Cylinder"
		elif type(surface) is Sphere:
			print "	Sphere"
		elif type(surface) is Torus:
			print "	Torus"
		elif type(surface) is Plane:
			print "	Plane"
		else:
			print "	Unknown Surface Type" 
		print "	Edges = " + str(object.Edges.Count)
	elif type(object) is DesignEdge:
		edge = object.Shape.Geometry
		if type(edge) is Line:
			print "	Line"
		if type(edge) is Circle:
			print "	Circle"
		if type(edge) is Ellipse:
			print "	Ellipse"
		print "	Smooth = " + str(object.Shape.IsSmooth)
		print "	Concave = " + str(object.Shape.IsConcave)
		print "	Precision = " + str(object.Shape.Precision)
		print "	Faces = " + str(object.Faces.Count)

def ClearAll():
    part = GetRootPart()
    ComponentHelper.SetRootActive()
    part.ClearAllPartData()

def ClearTypes(type):
    part = GetRootPart()
    part.ClearPartData(type)