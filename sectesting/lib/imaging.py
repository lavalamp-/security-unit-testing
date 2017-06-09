# -*- coding: utf-8 -*-
from __future__ import absolute_import

from PIL import Image
import exifread


class InvalidImageFileException(Exception):
    """
    This is an exception for denoting that the contents of a file do not constitute an image.
    """


class ImageProcessingHelper(object):
    """
    This class contains methods for parsing and processing the contents of an image file.
    """

    # Class Members

    # Instantiation

    def __init__(self, file_reference):
        self._file_ref = file_reference
        self._exif_tags = None
        self._rational_latitude = None
        self._rational_longitude = None
        self._r_lat_retrieved = False
        self._r_long_retrieved = False
        self._longitude_ref = None
        self._latitude_ref = None
        self._long_ref_retrieved = False
        self._lat_ref_retrieved = False
        self._latitude = None
        self._longitude = None
        self.__validate_image()

    # Static Methods

    @staticmethod
    def from_in_memory_uploaded_file(memory_file):
        """
        Create and return an instance of ImageProcessingHelper wrapping the contents of the given
        in-memory file.
        :param memory_file: An InMemoryUploadedFile to process.
        :return: An instance of ImageProcessingHelper configured to process the in-memory file.
        """
        return ImageProcessingHelper(memory_file.file)

    # Class Methods

    # Public Methods

    # Protected Methods

    # Private Methods

    def __convert_instance_to_float(self, instance):
        """
        Convert the contents of the given instance (as retrieved via EXIF data) to a float.
        :param instance: The instance to process.
        :return: A float representing the contents of the instance.
        """
        return float(instance.num) / instance.den

    def __convert_rational_to_decimal(self, rational_list):
        """
        Convert the contents of rational_list to a decimal coordinate.
        :param rational_list: A list containing (1) degrees, (2) minutes, and (3) seconds representing
        a geocoordinate.
        :return: A decimal representing the geocoordinate.
        """
        degrees = self.__convert_instance_to_float(rational_list[0])
        minutes = self.__convert_instance_to_float(rational_list[1])
        seconds = self.__convert_instance_to_float(rational_list[2])
        return degrees + (minutes / 60) + (seconds / 3600)

    def __validate_image(self):
        """
        Validate that the contents of the referenced file constitute a valid image.
        :return: None
        """
        try:
            im = Image.open(self.file_ref)
            if im.format not in ("BMP", "PNG", "JPEG"):
                raise InvalidImageFileException("Not a valid image file (%s format is not supported)." % (im.format,))
        except ImportError:
            raise
        except Exception as e:
            raise InvalidImageFileException("Not a valid image file: %s" % (e.message,))
        self.file_ref.seek(0)

    # Properties

    @property
    def coordinates(self):
        """
        Get a tuple containing (1) the latitude and (2) the longitude for where the picture was taken.
        :return: a tuple containing (1) the latitude and (2) the longitude for where the picture was taken.
        """
        return self.latitude, self.longitude

    @property
    def exif_tags(self):
        """
        Get a dictionary containing key-value pairs representing the EXIF data contained within the image.
        :return: a dictionary containing key-value pairs representing the EXIF data contained within the image.
        """
        if self._exif_tags is None:
            self._exif_tags = exifread.process_file(self.file_ref)
        return self._exif_tags

    @property
    def file_ref(self):
        """
        Get the file reference to the file being processed.
        :return: the file reference to the file being processed.
        """
        return self._file_ref

    @property
    def has_coordinates(self):
        """
        Get whether or not the image has geocoordinates within it.
        :return: whether or not the image has geocoordinates within it.
        """
        return self.latitude is not None and self.longitude is not None

    @property
    def latitude(self):
        """
        Get the latitude where the picture was taken.
        :return: the latitude where the picture was taken.
        """
        if self._latitude is None:
            if self.latitude_ref:
                lat_value = self.__convert_rational_to_decimal(self.rational_latitude.values)
                if self.latitude_ref.values.lower() == "s":
                    lat_value *= -1
                self._latitude = lat_value
        return self._latitude

    @property
    def latitude_ref(self):
        """
        Get the reference direction associated with the image's latitude of such data exists.
        :return: the reference direction associated with the image's latitude of such data exists.
        """
        if not self._lat_ref_retrieved:
            for key, value in self.exif_tags.iteritems():
                if "gpslatituderef" in key.lower():
                    self._latitude_ref = value
            self._lat_ref_retrieved = True
        return self._latitude_ref

    @property
    def longitude(self):
        """
        Get the longitude where the picture was taken.
        :return: the longitude where the picture was taken.
        """
        if self._longitude is None:
            if self.longitude_ref:
                long_value = self.__convert_rational_to_decimal(self.rational_longitude.values)
                if self.longitude_ref.values.lower() == "w":
                    long_value *= -1
                self._longitude = long_value
        return self._longitude

    @property
    def longitude_ref(self):
        """
        Get the reference direction associated with the image's longitude if such data exists.
        :return: the reference direction associated with the image's longitude if such data exists.
        """
        if not self._long_ref_retrieved:
            for key, value in self.exif_tags.iteritems():
                if "gpslongituderef" in key.lower():
                    self._longitude_ref = value
            self._long_ref_retrieved = True
        return self._longitude_ref

    @property
    def rational_latitude(self):
        """
        Get a list of values representing the rational latitude of the image if such data exists.
        :return: a list of values representing the rational latitude of the image if such data exists.
        """
        if not self._r_lat_retrieved:
            for key, value in self.exif_tags.iteritems():
                if key.lower().endswith("gpslatitude"):
                    self._rational_latitude = value
            self._r_lat_retrieved = True
        return self._rational_latitude

    @property
    def rational_longitude(self):
        """
        Get a list of values representing the rational longitude of the image if such data exists.
        :return: a list of values representing the rational longitude of the image if such data exists.
        """
        if not self._r_long_retrieved:
            for key, value in self.exif_tags.iteritems():
                if key.lower().endswith("gpslongitude"):
                    self._rational_longitude = value
            self._r_long_retrieved = True
        return self._rational_longitude

    # Representation and Comparison

    def __repr__(self):
        return "<%s - %s>" % (self.__class__.__name__, self.file_ref)
