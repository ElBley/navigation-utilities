"""Container module for the Coordinate class.

Author:
    Pablo Dorrio Vazquez
"""

import numpy as np


class Twodimensional:
    """This class represents a two-dimensional coordinate.

    Attributes:
        x (float): x coordinate.
        y (float): y coordinate.
    """

    def __init__(self, x_coord: float=None, y_coord: float=None) -> None:
        """Initialize the coordinate.

        Args:
            x_coord (float): x coordinate.
            y_coord (float): y coordinate.
        """
        self.__x = x_coord
        self.__y = y_coord

    @property
    def x(self) -> float:
        """Get the x coordinate.

        Returns:
            float: x coordinate.
        """
        return self.__x

    @x.setter
    def x(self, x_coord: float) -> None:
        """Set the x coordinate.

        Args:
            x_coord (float): x coordinate.
        """
        self.__x = x_coord

    @property
    def y(self) -> float:
        """Get the y coordinate.

        Returns:
            float: y coordinate.
        """
        return self.__y

    @y.setter
    def y(self, y_coord: float) -> None:
        """Set the y coordinate.

        Args:
            y_coord (float): y coordinate.
        """
        self.__y = y_coord

    def __str__(self) -> str:
        """Get the string representation of the coordinate.

        Returns:
            str: String representation of the coordinate.
        """
        return f"{self.__x}, {self.__y}"


class Threedimensional:
    """This class represents a three-dimensional coordinate.

    Attributes:
        x (float): x coordinate.
        y (float): y coordinate.
        z (float): z coordinate.
    """

    def __init__(self, x_coord: float=None, y_coord: float=None, z_coord: float=None) -> None:
        """Initialize the coordinate.

        Args:
            x_coord (float): x coordinate.
            y_coord (float): y coordinate.
            z_coord (float): z coordinate.
        """
        self.__x = x_coord
        self.__y = y_coord
        self.__z = z_coord

    @property
    def x(self) -> float:
        """Get the x coordinate.

        Returns:
            float: x coordinate.Coordinate
        """
        return self.__x

    @x.setter
    def x(self, x_coord: float) -> None:
        """Set the x coordinate.

        Args:
            x_coord (float): x coordinate.
        """
        self.__x = x_coord

    @property
    def y(self) -> float:
        """Get the y coordinate.

        Returns:
            float: y coordinate.
        """
        return self.__y

    @y.setter
    def y(self, y_coord: float) -> None:
        """Set the y coordinate.

        Args:
            y_coord (float): y coordinate.
        """
        self.__y = y_coord

    @property
    def z(self) -> float:
        """Get the z coordinate.

        Returns:
            float: z coordinate.
        """
        return self.__z

    @z.setter
    def z(self, z_coord: float) -> None:
        """Set the z coordinate.

        Args:
            z_coord (float): z coordinate.
        """
        self.__z = z_coord

    def to_twodimensional(self) -> Twodimensional:
        """Get the two-dimensional representation of the coordinate.

        Returns:
            Twodimensional: Two-dimensional representation of the coordinate.
        """
        return Twodimensional(self.__y, self.__z)


class TwodimensionalArray:
    """This class represents a two-dimensional array of coordinates.
    
    Attributes:
        x_array (np.ndarray): x array.
        y_array (np.ndarray): y array.
    """

    def __init__(self) -> None:
        """Initialize the array."""
        self.__x_array = []
        self.__y_array = []

    @property
    def x_array(self) -> np.ndarray:
        """Get the x array.

        Returns:
            np.ndarray: x array.
        """
        return self.__x_array

    @property
    def y_array(self) -> np.ndarray:
        """Get the y array.

        Returns:
            np.ndarray: y array.
        """
        return self.__y_array

    def append(self, coordinate: Twodimensional) -> None:
        """Append a coordinate to the array.

        Args:
            coordinate (Twodimensional): Coordinate to append.
        """
        self.__x_array.append(coordinate.x)
        self.__y_array.append(coordinate.y)
