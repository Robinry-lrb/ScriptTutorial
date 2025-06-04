from System.Collections.Generic import *

import math
import clr

clr.AddReference("System.Drawing")
from System import String
from System.Drawing import Color

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

def FaceCurves(sel, p1=None, p2=None):
	return DesignFaceExtensions.FaceCurves(sel, p1, p2)

def IsoCurves(sel, u, proportion):
	faces = sel.GetDocObjects()
	curves = List[ITrimmedCurve]()
	for face in faces:
		for curve in DesignFaceExtensions.IsoCurves(face, u, proportion):
			if curve is not None:
				curves.Add(curve)
	return curves

def FacePoint(sel, proportionU, proportionV):
	if not any(sel):
		raise Exception("No face input")
	face = sel.GetDocObjects()[0]
	return DesignFaceExtensions.FacePoint(face, proportionU, proportionV)

def EdgePoint(sel, proportion):
	if not any(sel):
		raise Exception("No edge input")
	edge = sel.GetDocObjects()[0]
	return DesignEdgeExtensions.EdgePoint(edge, proportion)
			
def SelectRounds(desBody, maxRadius):
	part = Window.ActiveWindow.ActiveContext.Root
	if part is None:
		raise Exception("Could not get root part.")
	
	if not type(desBody) is DesignBody:
		raise Exception("Could not get a body from id") 
	
	selection = List[IDocObject]()

	for desFace in desBody.Faces:
		surface = desFace.Shape.Geometry
		if type(surface) is Cylinder:
			if surface.Radius <= maxRadius:
				selection.Add(desFace)

		if type(surface) is Sphere:
			if surface.Radius <= maxRadius:
				selection.Add(desFace)

		if type(surface) is Torus:
			if surface.MinorRadius <= maxRadius:
				selection.Add(desFace)

	if not any(selection):
		raise Exception("No rounds found")

	return selection

def ClearAll():
    part = GetRootPart()
    part.ClearAll()

