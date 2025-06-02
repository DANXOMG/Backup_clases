<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html"/>
    <xsl:template match="/tiendaGaming">
        <html>
            <head>
                <tittle>Tienda <xsl:value-of select="@nombre"/></tittle>
            </head>

            <body>
                <h1>Productos de la tienda <xsl:value-of select="@nombre" /></h1>
                <h2>Productos con precio mayor o igual a 100 euros</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                        <th>Precio</th>
                    </tr>
                    <xsl:apply-templates select="articulo[number(precio) &gt;= 100]"/>
                </table>

                <h2>Productos con precio menor a 100 euros</h2>
                <table>
                    <tr>
                        <th>Nombre</th>
                        <th>Marca</th>
                        <th>Precio</th>
                    </tr>
                    <xsl:apply-templates select="articulo::number(precio) &lt;= 100"/>
                </table>

            </body>
        </html>
        

    </xsl:template>
</xsl:stylesheet>