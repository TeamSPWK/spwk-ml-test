import numpy as np
from shapely import geometry, ops, affinity
from matplotlib import pyplot as plt


class PolygonFillEnv():
    """
    Test for ML chapter applicants
    Fill polygon space with polygon patches
    """

    def __init__(self):
        self.__spaces = []
        self.__placed_patches = []
        self.add_space_coords([-10,10,10,-10],[-10,-10,10,10])
        self.__sample_index = 0
        self.__patch = self.coords_to_polygon([-2.5,2.5,2.5,-2.5], [-1.15,-1.15,1.15,1.15])
        self.reset()
        self.add_space_samples()
        self.__new_patch = geometry.Polygon()

    @property
    def spaces(self):
        return [{'shell':np.array(space.exterior), 'holes':[np.array(interior) for interior in space.interiors]} for space in self.__spaces]
            
    @property
    def __placed_patches_mp(self):
        return geometry.MultiPolygon(self.__placed_patches)

    @property
    def placed_patches(self):
        return [np.array(patch.exterior) for patch in self.__placed_patches]

    @property
    def patch(self):
        return np.array(self.__patch.exterior)

    @property
    def __space(self):
        return self.__spaces[self.__sample_index]

    @property
    def space(self):
        return {'shell':np.array(self.__space.exterior), 'holes':[np.array(interior) for interior in self.__space.interiors]} 

    @property
    def new_patch(self):
        if self.__new_patch.is_empty:
            return np.array()
        return np.array(self.__new_patch.exterior)
    
    def add_space_samples(self):
        self.add_space_coords([-10,-3,-3,-10],[-10,-10,10,10])
        self.add_space_coords([-5,5,5,-5],[-5,-5,5,5])
        self.add_space_coords([-10,10,10,-10],[-10,-10,10,10], [[[-5,5,5,-5],[-5,-5,5,5]]])
        self.add_space_coords([0,10,0,-10],[-10,0,10,0])
        self.add_space_coords([0,10,0,-10],[-10,0,10,0],[[[0,3,0,-3],[-3,0,3,0]]])
        self.add_space_coords([-10,10,10,-2,-2,10,10,-10],[-10,-10,-6,-6,6,6,10,10])
        self.add_space_coords([-10,8,10,-10,0],[-10,-10,7,10,-3])
        self.add_space_coords([-10,10,0],[-10,-10,10])
        self.add_space_coords([-10,10,0],[-10,-10,10], [[[-4,4,-2],[-6,-4,2]]])


    def select_space(self, index):
        self.__sample_index = index
        self.reset()

    def reset(self):
        self.__placed_patches = []

    def coords_to_polygon(self, x_coords, y_coords):
        try:
            polyarr = np.swapaxes([x_coords, y_coords], 0, 1)
        except:
            raise ValueError("Coordinates are wrong")
        if (polyarr > 10).any():
            raise ValueError("Coordinates are wrong")
        if (polyarr < -10).any():
            raise ValueError("Coordinates are wrong")
        return geometry.asPolygon(polyarr)

    def arr_to_polygon(self, polyarr):
        return geometry.asPolygon(polyarr)
    
    
    def add_space_coords(self, shell_x_coords, shell_y_coords, holes_coords=None):
        shell = self.coords_to_polygon(shell_x_coords, shell_y_coords)
        if not isinstance(holes_coords, type(None)):
            holes = geometry.MultiPolygon([self.coords_to_polygon(*hole_coords) for hole_coords in holes_coords])
            self.__spaces.append(shell.difference(holes))
        else:
            self.__spaces.append(shell)
        
    def add_space_arr(self, shell_arr, hole_arrs=None):
        shell = self.arr_to_polygon(shell_arr)
        if not isinstance(hole_arrs, type(None)):
            holes = geometry.MultiPolygon([self.arr_to_polygon(hole_arr) for hole_arr in hole_arrs])
            self.__spaces.append(shell.difference(holes))
        else:
            self.__spaces.append(shell)

    def step(self, patch_x, patch_y, patch_angle):
        """[summary]

        Args:
            patch_x (float): Patch centroid position x coordinate
            patch_y (float): Patch centroid position y coordinate
            patch_angle (float): Patch rotation angle (radian)

        Returns:
            [type]: [description]
        """
        if not (isinstance(patch_x, float) or isinstance(patch_x, int)):
            raise TypeError("Type of patch centroid x coordinate must be float")
        if not (isinstance(patch_y, float) or isinstance(patch_y, int)):
            raise TypeError("Type of patch centroid y coordinate must be float")
        if not (isinstance(patch_angle, float) or isinstance(patch_angle, int)):
            raise TypeError("Type of patch rotation angle must be float")

        if not -10 <= patch_x <= 10:
            raise ValueError("Patch centroid x coordinate must be on -10 to 10")
        if not -10 <= patch_y <= 10:
            raise ValueError("Patch centroid y coordinate must be on -10 to 10")
        if not -np.pi/2 <= patch_angle <= np.pi/2:
            raise ValueError("Patch rotation angle must be on -pi/2 to pi/2")

        new_patch = affinity.rotate(self.__patch, patch_angle, origin='centroid', use_radians=True)
        self.__new_patch = affinity.translate(new_patch, xoff=patch_x, yoff=patch_y)

        area_out_of_space = self.__new_patch.difference(self.__space).area
        area_intersect_patches = self.__new_patch.intersection(self.__placed_patches_mp).area
        
        is_valid = (area_out_of_space == 0) and (area_intersect_patches == 0)

        if is_valid:
            self.__placed_patches.append(self.__new_patch)
        
        return {
            'is_valid': is_valid,
            'n_patches': len(self.placed_patches),
            'space': self.space,
            'selected_patch': self.new_patch,
            'placed_patches': self.placed_patches,
            'area_out_of_space': area_out_of_space,
            'area_intersect_patches': area_intersect_patches
        }

    def render(self):
        figure = plt.figure()
        plt.gca().set_aspect('equal')
        plt.xlim(-10,10)
        plt.ylim(-10,10)
        plt.fill(*self.__space.exterior.coords.xy, color='yellow')
        for interior in self.__space.interiors:
            plt.fill(*interior.coords.xy, color='white')
        for placed_patch in self.__placed_patches:
            plt.fill(*placed_patch.exterior.coords.xy, color='green')
        if not self.__new_patch.is_empty:
            plt.fill(*self.__new_patch.exterior.coords.xy, color='red', alpha=0.3)
        plt.show()
