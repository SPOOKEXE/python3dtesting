
from __future__ import annotations

import pygame

from OpenGL import GL, GLU

from minecraft import (
	Point3, Direction, Inventory,
	Item, Chest, Furnace, Block,
	Turtle,
	World, WorldAPI,
)

class Colors:
	RED = (1, 0, 0)
	GREEN = (0, 1, 0)
	BLUE = (0, 0, 1)

class EdgesSurfaces:
	CUBE_EDGES = (
		(0,1),
		(0,3),
		(0,4),
		(2,1),
		(2,3),
		(2,7),
		(6,3),
		(6,4),
		(6,7),
		(5,1),
		(5,4),
		(5,7)
	)

	CUBE_SURFACES = (
		(0,1,2,3),
		(3,2,7,6),
		(6,7,5,4),
		(4,5,1,0),
		(1,5,7,2),
		(4,0,3,6)
	)

class OpenGLWrapper:

	@staticmethod
	def draw_rect(
		top_left : tuple[int, int, int],
		bottom_right : tuple[int, int, int],
		outline : tuple | None = None,
		fill : tuple | None = None,
	) -> None:
		pass

class Viewport:
	'''
	Singleton for the Viewport widget.
	'''

	alive : bool = False

	def __init__( self, *args, **kwargs ) -> Viewport:
		pass

	def update( self, dt : float ) -> None:
		raise NotImplementedError

	async def update_async( self, dt : float ) -> None:
		raise NotImplementedError

	def start( self ) -> None:
		self.alive = True

		pygame.init()

	def stop( self ) -> None:
		self.alive = False

class MinecraftViewport(Viewport):
	'''
	Singleton for the Viewport widget - built for the Minecraft workspace.
	'''

	world : World = None

	def __init__(self, *args, **kwargs) -> MinecraftViewport:
		super().__init__(self, *args, **kwargs)

	def draw_cubes( self, cubes : Block ) -> None:
		pass

	def find_non_occulued_blocks( self ) -> list[Block]:
		pass

	def update( self, dt : float ) -> None:
		pass

	async def update_async( self, dt : float ) -> None:
		pass

	def set_world( self, world : World ) -> None:
		self.world = world

	def clear_world( self ) -> None:
		self.world = None
