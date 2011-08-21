# -*- coding: utf-8 -*-
# Copyright 2007-2011 The Hyperspy developers
#
# This file is part of  Hyperspy.
#
#  Hyperspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  Hyperspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  Hyperspy.  If not, see <http://www.gnu.org/licenses/>.

# custom exceptions

class ByteOrderError(Exception):
    def __init__(self, order=''):
	self.byte_order = order

    def __str__(self):
	return repr(self.byte_order)

class DM3FileVersionError(Exception):
    def __init__(self, value=''):
        self.dm3_version = value
    
    def __str__(self):
        return repr(self.dm3_version)    

class DM3TagError(Exception):
    def __init__(self, value=''):
        self.dm3_tag = value
    
    def __str__(self):
        return repr(self.dm3_tag)

class DM3DataTypeError(Exception):
    def __init__(self, value=''):
        self.dm3_dtype = value
    
    def __str__(self):
        return repr(self.dm3_dtype)

class DM3TagTypeError(Exception):
    def __init__(self, value=''):
        self.dm3_tagtype = value
    
    def __str__(self):
        return repr(self.dm3_tagtype)

class DM3TagIDError(Exception):
    def __init__(self, value=''):
        self.dm3_tagID = value
    
    def __str__(self):
        return repr(self.dm3_tagID)

class ImageIDError(Exception):
    def __init__(self, value=''):
        self.image_id = value

    def __str__(self):
        return repr(self.image_id)

class ImageModeError(Exception):
    def __init__(self, value=''):
        self.mode = value

    def __str__(self):
        return repr(self.mode)

class ShapeError(Exception):
    def __init__(self, value):
        self.error = value.shape

    def __str__(self):
        return repr(self.error)