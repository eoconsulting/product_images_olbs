#########################################################################
# Copyright (C) 2009  Sharoon Thomas, Open Labs Business solutions      #
#                                                                       #
#    Module Modified: 2012-06-05                                        #
#    Author: Mariano Ruiz <mrsarm@gmail.com>,                           #
#            Enterprise Objects Consulting                              #
#                                                                       #
#This program is free software: you can redistribute it and/or modify   #
#it under the terms of the GNU General Public License as published by   #
#the Free Software Foundation, either version 3 of the License, or      #
#(at your option) any later version.                                    #
#                                                                       #
#This program is distributed in the hope that it will be useful,        #
#but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#GNU General Public License for more details.                           #
#                                                                       #
#You should have received a copy of the GNU General Public License      #
#along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#########################################################################

{
    "name" : "Product Image Gallery",
    "version" : "0.2 ",
    "author" : "Sharoon Thomas, Open Labs Business Solutions / Modified by Mariano Ruiz, Enterprise Objects Consulting",
    "website" : "http://www.eoconsulting.com.ar",
    "category" : "Added functionality - Product Extension",
    "depends" : ['base','product'],
    "description": """
    This Module implements an Image Gallery for products.
    You can add images against every product.
    
    This module is generic, but built for Magento ERP connector, and
    modified to be compatible with Zoook e-Sale, and OpenERP 6-6.1.
    """,
    "init_xml": [],
    "update_xml": [
        'security/ir.model.access.csv',
        'views/product_images_view.xml',
        'views/company_view.xml'
    ],
    "installable": True,
    "active": False,
}

