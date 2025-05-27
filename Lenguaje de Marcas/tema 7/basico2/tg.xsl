<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html"/>
        <xsl:template match="/">
            <html>
                <head>
                    <title>Producto Tienda Gaming</title>
                </head>
                <style>
                    table{
                        width: 80%;
                        margin: 20px auto;
                        border-collapse: collapse;
                        font-family: Arial, sans-serif;
                    }
                    th,td{
                        boder: 1px solid #ccc
                        padding: 10px;
                        text-align: center;
                    }
                    th {
                        background-color: #333;
                        color: azure;
                    }
                    tr:nth-chil(even){
                        background-color: #f2f2f2;
                    }
                    h1 {
                        text-align: center;
                        font-family: Arial, sans-serif;
                        color: #444;
                    }  
                </style>

                <body>
                    <h1>Productos de menos de 100 euros</h1>
                    <table>
                        <tr>
                            <th>Nombre</th>
                            <th>Marca</th>
                            <th>Precio</th>
                            <th>Stock</th>
                        </tr>
                        <xsl:for-each select="producto[number(precio) &lt; 100]">
                            <tr>
                                <td><xsl:value-of select="nombre"/></td>
                                <td><xsl:value-of select="marca"/></td>
                                <td><xsl:value-of select="precio"/></td>
                                <td><xsl:value-of select="Stock"/></td>
                            </tr>
                        </xsl:for-each>
                    </table>
                    <xsl:apply-templates/>
                </body>
            </html>

    </xsl:template>
</xsl:stylesheet>